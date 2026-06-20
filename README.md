# AI Smart Traffic Management System using VLSI and Python

## Project Overview

The AI Smart Traffic Management System is an intelligent traffic control project developed using Verilog (VLSI backend) and Python (GUI frontend). The system simulates a smart city traffic junction that dynamically manages traffic signals using traffic density, pedestrian requests, emergency vehicle handling, AI prediction, and real-time analytics.

This project combines concepts of VLSI design, Finite State Machines (FSM), Python GUI development, databases, and AI techniques.

---

## Features

### VLSI Backend Features

✔ Finite State Machine (FSM) based traffic controller

✔ Traffic signal timing control

✔ Pedestrian crossing support

✔ Emergency vehicle priority

✔ Traffic density sensors

✔ Countdown timer

✔ Statistics counters

✔ Safety logic and error detection

---

### Python Frontend Features

✔ Modern Smart City dashboard

✔ Four-way traffic junction simulation

✔ Horizontal and vertical moving vehicles

✔ Traffic signal visualization

✔ Emergency mode button

✔ Pedestrian button

✔ Traffic density slider

✔ AI traffic prediction

✔ Live statistics display

✔ Database logging

✔ Real-time analytics support

---

## Technologies Used

### Programming Languages

- Verilog
- Python

### Python Libraries

- tkinter
- sqlite3
- random
- pandas
- matplotlib
- scikit-learn
- opencv-python

### Simulation Tools

- Icarus Verilog
- GTKWave
- VS Code

---

## Project Structure

```text
Smart-Traffic-System/

│
├── rtl/
│      traffic_controller.v
│
├── tb/
│      traffic_tb.v
│
├── traffic_dashboard.py
│
├── database.py
│
├── analytics.py
│
├── ai_prediction.py
│
├── vehicle_detection.py
│
├── traffic.db
│
├── README.md
│
└── screenshots/
```

---

## Installation

### Step 1: Install Icarus Verilog

Download:

https://bleyer.org/icarus/

---

### Step 2: Install GTKWave

Download:

https://gtkwave.sourceforge.net/

---

### Step 3: Install Python Libraries

Open terminal:

```bash
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install opencv-python
```

Or install all:

```bash
pip install pandas matplotlib scikit-learn opencv-python
```

---

## Running Verilog Simulation

Move to project folder:

```bash
iverilog -o traffic rtl/traffic_controller.v tb/traffic_tb.v

vvp traffic

gtkwave traffic.vcd
```

Add signals inside GTKWave:

```text
clk
reset
pedestrian
emergency
veh_NS
veh_EW
NS
EW
WALK
ERROR
DUT.state
DUT.count
```

---

## Running Smart Dashboard

Run:

```bash
python traffic_dashboard.py
```

---

## Running Analytics

Run:

```bash
python analytics.py
```

---

## Running AI Prediction

Run:

```bash
python ai_prediction.py
```

---

## Running Vehicle Detection

Run:

```bash
python vehicle_detection.py
```

---

## System Workflow

```text
Traffic Sensors
        ↓
Traffic Controller FSM
        ↓
Signal Decision Logic
        ↓
Emergency/Pedestrian Handling
        ↓
Database Logging
        ↓
AI Prediction
        ↓
Dashboard Visualization
```

---

## Future Improvements

- Real camera integration
- IoT sensor integration
- Cloud database support
- Mobile application
- Traffic heatmaps
- Route optimization
- Deep learning traffic prediction

---
## Screenshots 
<img width="1366" height="768" alt="Screenshot 2026-06-18 234105" src="https://github.com/user-attachments/assets/c712da8c-555f-455c-9111-a0f82fa77327" />
<img width="1366" height="768" alt="Screenshot 2026-06-18 234120" src="https://github.com/user-attachments/assets/e5462c95-bcec-4792-9e03-34cd56aebb55" />
<img width="1366" height="768" alt="Screenshot 2026-06-18 234139" src="https://github.com/user-attachments/assets/5a26eac3-6283-4465-87af-8384463f665c" />

## Learning Outcomes

Through this project, the following concepts are learned:

- Finite State Machines
- Sequential Logic
- Counters
- Traffic Signal Design
- VLSI Design Flow
- Testbench Creation
- Python GUI Development
- Database Management
- Machine Learning Basics
- Smart City Applications

---
## Author

Tanisha Mittal



## License

This project is developed for educational and learning purposes.
