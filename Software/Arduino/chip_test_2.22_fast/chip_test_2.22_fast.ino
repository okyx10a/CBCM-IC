short result = 0;
int N_sample = 1000;

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
  REG_PWM_CDTY0 = PWM_CDTY_CDTY(16);// 80/3% duty cycle
  REG_PWM_ENA = PWM_ENA_CHID0;// enable PWM channel0

  //config phi2, Output pin PC4, Digital pin 36
  REG_PIOC_ABSR |= PIO_ABSR_P4; // Transfer Pin control from PIO to PWM
  REG_PIOC_PDR |= PIO_PDR_P4;   // Set PWM pin to an output
  REG_PWM_CMR1 = PWM_CMR_CPRE_CLKA | PWM_CMR_DTE; //mode congiration for channel 0: clock A, letft aligned, waveform start at high
  REG_PWM_CPRD1 = PWM_CPRD_CPRD(60);//config period for pwm 60/(4MHz)
  REG_PWM_DT1 = PWM_DT_DTL(4); //create the 1us(delay)
  REG_PWM_CDTY1 = PWM_CDTY_CDTY(12);// 80/3% duty cycle
  REG_PWM_ENA = PWM_ENA_CHID1;// enable PWM channel1

  //config phi3, Output pin PC6, Digital pin 38
  REG_PIOC_ABSR |= PIO_ABSR_P6; // Transfer Pin control from PIO to PWM
  REG_PIOC_PDR |= PIO_PDR_P6;   // Set PWM pin to an output
  REG_PWM_CMR2 = PWM_CMR_CPRE_CLKA;//mode congiration for channel 0: clock A, letft aligned, waveform start at low
  REG_PWM_CPRD2 = PWM_CPRD_CPRD(2);//config period for pwm 2/(4MHz)
  REG_PWM_CDTY2 = PWM_CDTY_CDTY(1);//50% duty cycle
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

  pinMode(22, OUTPUT); // Sin
  pinMode(24, OUTPUT); // Sclk
  pinMode(48, OUTPUT); //G1
  pinMode(50, OUTPUT); //G2
  pinMode(52, OUTPUT); //G3
  digitalWrite(48, HIGH);
  digitalWrite(50, HIGH);
  digitalWrite(52, HIGH);
  delay(100);
  digitalWrite(22, LOW);
  digitalWrite(24, LOW);
  //inputSig("00010011");
  digitalWrite(22, LOW);
  digitalWrite(24, LOW);
  delay(10);
}

void inputSig(char testSeq[])
{
  //turn off the phi clock pulses
  REG_PWM_DIS = PWM_DIS_CHID0;
  REG_PWM_DIS = PWM_DIS_CHID1;
  REG_PWM_DIS = PWM_DIS_CHID2;
  delayMicroseconds(1);
  //fully reset the input registers
  for (int i = 13; i > 0 ; i--)
  {
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    delay(1);
    digitalWrite(24, HIGH);
    delay(1);
  }
  //apply input sequences
  for (int i = 0; i <= 7 ; i++)
  {
    if (testSeq[i] == '0')
    {
      digitalWrite(22, LOW);
      digitalWrite(24, LOW);
      delay(1);
      digitalWrite(24, HIGH);
      delay(1);
    }
    else if (testSeq[i] == '1')
    {
      digitalWrite(22, HIGH);
      digitalWrite(24, LOW);
      delay(1);
      digitalWrite(24, HIGH);
      delay(1);
    }
  }
  delayMicroseconds(1);
  digitalWrite(22, LOW);
  digitalWrite(24, LOW);
  //turn the phi pulses back on
  REG_PWM_ENA = PWM_ENA_CHID0;
  REG_PWM_ENA = PWM_ENA_CHID1;
  REG_PWM_CMR2 = 0;
  REG_PWM_CMR2 = PWM_CMR_CPRE_CLKA;
  REG_PWM_CMR2 &= ~PWM_CMR_CPOL;
  REG_PWM_ENA = PWM_ENA_CHID2;
}

void loop() {
  //inputSig("11101010");
  char calin_i[7];
  //Serial.println(1);
  if (Serial.available() > 0)
  {
    //Serial.println(2);
    char temp = Serial.read();
    switch (temp)
    {
      case 'S':
      {
        String N_sample_s = Serial.readStringUntil('\0');
        N_sample = N_sample_s.toInt();
        Serial.println(N_sample);
        break;
      }
      case 'W':
        for (int i = 0; i <= 7; )
        {
          if (Serial.available() > 0)
          {
            calin_i[i] = Serial.read();
            i++;
          }
        }
        //calin_i[7] = '\0';
        //Serial.println(calin_i);
        inputSig(calin_i);
        break;
      case 'G':
      {
        for (int i = 0; i < 3; )
        {
          if (Serial.available() > 0)
          {
            calin_i[i] = Serial.read();
            i++;
          }
          if (calin_i[i] == '1')
            digitalWrite(48 + i, HIGH);
          else
            digitalWrite(48 + i, LOW);
        }
        calin_i[3] = '\0';
        Serial.println(calin_i);
        break;
      }
      case 'R':
        unsigned char buf[N_sample * sizeof(short)];
        for (int i = 0; i < N_sample;)
        {
          if (REG_SPI0_SR & 1)
          {
            result = REG_SPI0_RDR;
            buf[2 * i] = highByte(result);
            buf[2 * i + 1] = lowByte(result);
            i++;
          }
        }
        delay(1);
        Serial.write(buf, N_sample * sizeof(short));
        Serial.flush();
        break;
      default:
        Serial.println("Meow\0");
        break;
    }

  }

}
