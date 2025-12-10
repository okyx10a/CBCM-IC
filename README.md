# CBCM-IC Testing Platform
**Full-stack mixed-signal test fixture for Charge-Based Capacitance Measurement ICs**  
Designed, fabricated, and validated at York University (2018–2019)

![Test board](Photos/0.JPGE)
(Photos/1.JPGE)
(Photos/2.JPG)
*4-layer mixed-signal test board with separated analog/digital ground planes*

## Key Features
- 4-layer KiCad design with proper analog/digital ground splitting 
- SAM3X8E ARM Cortex-M3 (Arduino Due core) for real-time pattern generation and data acquisition
- Interfaces: SPI (20 MHz), UART
- SMT soldering down to 0603 passives and QFN packages (hand-soldered prototype)
- Automated measurement and data logging via Python + PyQt GUI
- Full test reports with statistical analysis 
