short result = 0;
int N_sample = 1000;
char Cs = '0'; // NEW
byte freq_scale = 0; // NEW
char calin_i[8] = {'0', '0', '0', '0', '0', '0', '0', '0'}; // Taken out from voide loop
char calin_g[3] = {'0', '0', '0'}; //// Taken out from voide loop

void setup() {
  Serial.begin(115200);

  // put your setup code here, to run once:
  REG_PMC_PCER1 |= PMC_PCER1_PID36;// Power up PWM clock
  REG_PWM_WPCR = PWM_WPCR_WPCMD(0);//Unlock user interface for PWM
  REG_PWM_CLK = PWM_CLK_PREA(0) | PWM_CLK_DIVA(21); //config the PWM clock generator: clock A, 84/21 = 4MHz
  REG_PWM_SCM = PWM_SCM_SYNC0 | PWM_SCM_SYNC1; //Synchronize phi1 and phi2 for they have the same frequency

  //config phi1, Output pin PC2, Digital pin 34
  REG_PIOC_ABSR |= PIO_ABSR_P2; // Transfer Pin control from PIO to PWM
  REG_PIOC_PDR |= PIO_PDR_P2;   // Set PWM pin to an output
  REG_PWM_CMR0 = PWM_CMR_CPRE_CLKA; //mode congiration for channel 0: clock A, letft aligned, waveform start at high
  REG_PWM_CPRD0 = PWM_CPRD_CPRD(60);//config period for pwm 60/(4MHz)
  REG_PWM_CDTY0 = PWM_CDTY_CDTY(16);// 80/3% duty cycle(16)
  REG_PWM_ENA = PWM_ENA_CHID0;// enable PWM channel0

  //config phi2, Output pin PC4, Digital pin 36
  REG_PIOC_ABSR |= PIO_ABSR_P4; // Transfer Pin control from PIO to PWM
  REG_PIOC_PDR |= PIO_PDR_P4;   // Set PWM pin to an output
  REG_PWM_CMR1 = PWM_CMR_CPRE_CLKA | PWM_CMR_DTE; //mode congiration for channel 0: clock A, letft aligned, waveform start at high
  REG_PWM_CPRD1 = PWM_CPRD_CPRD(60);//config period for pwm 60/(4MHz)
  REG_PWM_DT1 = PWM_DT_DTL(4); //create the 1us(delay)
  REG_PWM_CDTY1 = PWM_CDTY_CDTY(12);// 80/6% duty cycle(12)
  REG_PWM_ENA = PWM_ENA_CHID1;// enable PWM channel1

  //config phi3, Output pin PC6, Digital pin 38
  REG_PIOC_ABSR |= PIO_ABSR_P6; // Transfer Pin control from PIO to PWM
  REG_PIOC_PDR |= PIO_PDR_P6;   // Set PWM pin to an output
  REG_PWM_CMR2 = PWM_CMR_CPRE_CLKA;//mode congiration for channel 0: clock A, letft aligned, waveform start at low |PWM_CMR_CALG
  REG_PWM_CPRD2 = PWM_CPRD_CPRD(4);//config period for pwm 2/(4MHz)
  REG_PWM_CDTY2 = PWM_CDTY_CDTY(2);//50% duty cycle(1)
  REG_PWM_ENA = PWM_ENA_CHID2;// enable PWM channel2

  //SPI serial recieve
  REG_PMC_PCER0 |= PMC_PCER0_PID24;// Power up SPI clock
  REG_SPI0_WPMR = 0 << SPI_WPMR_WPEN; //Unlock user interface for SPI

  //Instance SPI0, MISO: PA25, (MISO), MOSI: PA26, (MOSI), SCLK: PA27, (SCLK), NSS: PA28, Digital pin 10
  REG_PIOA_ABSR |= PIO_ABSR_P25; // Transfer Pin control from PIO to SPI
  REG_PIOA_PDR |= PIO_PDR_P25;   // Set MISO pin to an output

  REG_PIOA_ABSR |= PIO_ABSR_P26; // Transfer Pin control from PIO to SPI
  REG_PIOA_PDR |= 0 << PIO_PDR_P26; // Set MOSI pin to an input

  REG_PIOA_ABSR |= PIO_ABSR_P27; // Transfer Pin control from PIO to SPI
  REG_PIOA_PDR |= 0 << PIO_PDR_P27; // Set SCLK pin to an input

  REG_PIOA_ABSR |= PIO_ABSR_P28; // Transfer Pin control from PIO to SPI
  REG_PIOA_PDR |= 0 << PIO_PDR_P28; // Set NSS pin to an input

  //REG_ISER0 = 1<<24; //Enable interrupt controller
  REG_SPI0_CR = 1; // Enable SPI
  REG_SPI0_MR = 0; // Slave mode
  REG_SPI0_IER = 1 << SPI_IER_RDRF | 1 << SPI_IER_OVRES | 1 << SPI_IER_NSSR; //Enable interrupts
  SPI0->SPI_CSR[0] = SPI_CSR_BITS_12_BIT; // Capture on falling edge and transfer 12 bits.
  pinMode(46, OUTPUT); //Cs
  pinMode(22, OUTPUT); // Sin
  pinMode(24, OUTPUT); // Sclk
  pinMode(48, OUTPUT); //G1
  pinMode(50, OUTPUT); //G2
  pinMode(52, OUTPUT); //G3
  digitalWrite(48, HIGH);
  digitalWrite(50, HIGH);
  digitalWrite(52, HIGH);
  delay(100);
}

void inputSig(char testSeq[])
{
  //turn off the phi clock pulses
  REG_PWM_DIS = PWM_DIS_CHID0;
  REG_PWM_DIS = PWM_DIS_CHID1;
  REG_PWM_DIS = PWM_DIS_CHID2;
  delayMicroseconds(5);
  //fully reset the input registers
  for (int i = 13; i > 0 ; i--)
  {
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    delayMicroseconds(5);
    digitalWrite(24, HIGH);
    delayMicroseconds(5);
  }
  //apply input sequences
  for (int i = 0; i <= 7 ; i++)
  {
    if (testSeq[i] == '0')
    {
      digitalWrite(22, LOW);
      digitalWrite(24, LOW);
      delayMicroseconds(5);
      digitalWrite(24, HIGH);
      delayMicroseconds(5);
    }
    else if (testSeq[i] == '1')
    {
      digitalWrite(22, HIGH);
      digitalWrite(24, LOW);
      delayMicroseconds(5);
      digitalWrite(24, HIGH);
      delayMicroseconds(5);
    }
    else
    {
      digitalWrite(22, LOW);
      digitalWrite(24, LOW);
      delayMicroseconds(10);
    }
  }
  digitalWrite(22, LOW);
  digitalWrite(24, LOW);
  delayMicroseconds(5);
  //turn the phi pulses back on
  REG_PWM_ENA = PWM_ENA_CHID0;
  REG_PWM_ENA = PWM_ENA_CHID1;
  REG_PWM_CMR2 = 0;
  REG_PWM_CMR2 = PWM_CMR_CPRE_CLKA;
  REG_PWM_CMR2 &= ~PWM_CMR_CPOL;
  REG_PWM_ENA = PWM_ENA_CHID2;
  delayMicroseconds(20);
}

void loop() {

  if (Serial.available() > 0)
  {
    //Serial.println(2);
    char cmd = Serial.read();
    switch (cmd)
    {
      case 'S':
        {
          String N_sample_s = Serial.readStringUntil('\0');
          N_sample = N_sample_s.toInt();
          Serial.println(N_sample);
          break;
        }
      case 'G':
        {
          for (int i = 0; i < 3; )
          {
            if (Serial.available() > 0)
            {
              calin_g[i] = Serial.read();
              if (calin_g[i] == '1')
                digitalWrite(48 + 2 * i, HIGH);
              else
                digitalWrite(48 + 2 * i, LOW);
              i++;
            }
          }
          calin_g[3] = '\0';
          Serial.println(calin_g);
          break;
        }
      case 'W':
        {
          for (int i = 0; i <= 7; )
          {
            if (Serial.available() > 0)
            {
              calin_i[i] = Serial.read();
              i++;
            }
          }
          if (calin_i[7] == ' ')
          {
            digitalWrite(46, LOW);
          }
          else
          {
            digitalWrite(46, HIGH);
          }

          inputSig(calin_i);
          calin_i[8] = '\0';
          Serial.println(calin_i);
          break;
        }
      case 'R':
        {
          unsigned char buf[N_sample * sizeof(short)];
          for (int i = 0; i < N_sample;)
          {
            if (REG_SPI0_SR & 1)
            {
              result = REG_SPI0_RDR;
              //Serial.print(String(result,BIN)+" "+result+"\n");
              buf[2 * i] = highByte(result);
              buf[2 * i + 1] = lowByte(result);
              i++;
            }
          }
          delay(1);
          Serial.write(buf, N_sample * sizeof(short));
          Serial.flush();
          break;
        }


      // NEW
      case 'C':

        { char Side = Serial.read();
          if (Side == '0') // scan of the left side

          {
            // a function for sending the measured data in scan mode that sends out 128 measured points, equivalant to a scan curve. Left Side.

            unsigned char scan_buf[128 * sizeof(short)];
            for (int k = 0; k < 128; k++)
            {
              decToBinary_Char(k);  // sending i to be converted to an 8-bit binary array representation and be kept in count
              inputSig(calin_i);  // updates the calibration value
              digitalWrite(46, LOW); // select left side of the chip as output
              if (REG_SPI0_SR & 1)
              {
                result = REG_SPI0_RDR;
                scan_buf[2 * k] = highByte(result);
                scan_buf[2 * k + 1] = lowByte(result);

              }
            }
            delay(1);
            Serial.write(scan_buf, 128 * sizeof(short) );
            Serial.flush();

          }


          else if (Side == '1') // scan of the right side
          {
            unsigned char scan_buf[128 * sizeof(short)];
            for (int k = 0; k < 128; k++)
            {
              decToBinary_Char(k);  // sending i to be converted to a 8-bit binary array representation and be kept in count
              if (Serial.available() > 0)
              {
                Cs = Serial.read();
              }
              if (Cs == '1')
              {
                {
                  calin_i[8] = '1';
                }
                inputSig(calin_i);  // updates the calibration value
                digitalWrite(46, HIGH);
              } // select left side of the chi as output
              if (REG_SPI0_SR & 1)
              {
                result = REG_SPI0_RDR;
                scan_buf[2 * k] = highByte(result);
                scan_buf[2 * k + 1] = lowByte(result);

              }
            }
            delay(1);
            Serial.write(scan_buf, 128 * sizeof(short) );
            Serial.flush();

          }
          break;
        }

      // NEW
      case 'F':  // phi1, phi2, phi3 Frequency setup
        {

          if (Serial.available() > 0)
          {
            freq_scale = Serial.read();
          }

          if (freq_scale < 5)
          {
            REG_PWM_CLK = PWM_CLK_PREA(freq_scale) | PWM_CLK_DIVA(21); //if ferq_scale=1 then phi1=phi2=33.33 kHz and phi3=500 kHz, if ferq_scale=2 then phi1=phi2=16.66 kHz and phi3=250 kHz,
          }
          //if ferq_scale=3 then phi1=phi2=8.33 kHz and phi3=125 kHz , if ferq_scale=4 then phi1=phi2=4.166 kHz and phi3=62.5 kHz
          // page 976 of the SAM Manual
          else if (freq_scale == 5)
          {
            REG_PWM_CLK = PWM_CLK_PREA(0) | PWM_CLK_DIVA(10); // if ferq_scale=5 then phi1=phi2=140 kHz and phi3=2.1 MHz
          }

          else if (freq_scale == 6)
          {
            REG_PWM_CLK = PWM_CLK_PREA(0) | PWM_CLK_DIVA(5); // if ferq_scale=6 then phi1=phi2=280 kHz and phi3=4.2 MHz
          }


          break;
        }


      default:
        {
          Serial.println("Meow\0");
          break;
        }


    }

  }

}

// NEW
//////////////////Added
// To convert decimal to binary
void decToBinary_Char(int n)
{
  // array to store binary number
  byte  binaryNum[8];
  // counter for binary array
  int i = 0;
  while (n > 0) {

    // storing remainder in binary array
    binaryNum[i] = n % 2;
    if (binaryNum[i] == 0)
    {
      calin_i[i] = '0';
    }
    else if (binaryNum[i] == 1)
    {
      calin_i[i] = '1';
    }
    n = n / 2;
    i++;
  }

}
///////////////////////////
