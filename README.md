# CBCM-IC Testing Platform
**Full-stack mixed-signal test fixture for Charge-Based Capacitance Measurement ICs**  
Designed, fabricated, and validated at York University (2018–2019)

(Photos/0.JPEG)
(Photos/1.JPEG)
(Photos/2.JPEG)
(Photos/3.JPEG)
*4-layer mixed-signal test board with separated analog/digital ground planes*

## Directory Structure
├── Hardware/                       → Altium project
├── Software/                       → Arduino code + PyQt GUI
├── Photos/                         → Assembly
├── Test results/                   → Raw data and measurement data
├── CBCM project summery.docx       → Test fixture construction explanation
├── Tools chain setup.txt           → Note for succeeding developer
└── README.md

## Key Features
- 4-layer KiCad design with proper analog/digital ground splitting
- SAM3X8E ARM Cortex-M3 (Arduino Due core) for real-time pattern generation and data acquisition
- Interfaces: SPI (20 MHz), UART
- SMT soldering down to 0603 passives and QFN packages (hand-soldered prototype)
- Automated measurement and data logging via Python + PyQt GUI

