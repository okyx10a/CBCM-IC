# CBCM-IC Testing Platform
**Full-stack mixed-signal test fixture for Charge-Based Capacitance Measurement ICs**  
Designed, fabricated, and validated at York University (2018–2019)

(photos/0.jpg)
(photos/1.jpg)
(photos/2.jpg)
*4-layer mixed-signal test board with separated analog/digital ground planes*

## Why This Project Matters for Employers
- Complete ownership: schematic → layout → fabrication → assembly → bring-up → automated testing
- Real-world mixed-signal challenges solved: ground separation, SPI
- Production-style documentation and version control (exactly what aerospace/nuclear employers want)

## Key Features
- 4-layer KiCad design with proper analog/digital ground splitting and stitching vias
- SAM3X8E ARM Cortex-M3 (Arduino Due core) for real-time pattern generation and data acquisition
- Interfaces: SPI (20 MHz), I²C, UART, precision analog front-end
- SMT soldering down to 0402 passives and QFN packages (hand-soldered prototype)
- Automated measurement and data logging via Python + PyQt GUI
- Full test reports with statistical analysis (repeatability, noise floor, yield calculation)
