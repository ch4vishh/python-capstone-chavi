# python-capstone-chavi
campus-energy-dashboard

# Campus Energy-Use Dashboard  
### Capstone Project – Programming for Problem Solving Using Python  

**Name:** Chavi Jaiswal  
**Roll No.:** 2501410011  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Project Introduction  
This is my Python capstone project.  
In this project, I made a simple energy-use dashboard for different buildings on a campus.  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Project Structure  
python-capstone/
│
├── data/                : CSV files for each building
├── output/              : Program output files
├── dashboard.png        : Final graph dashboard
├── energy_dashboard.py  : Main Python code
└── README.md            : This file
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## What the Program Does  

### 1. Reads CSV Files  
The program reads all the CSV files inside the **data** folder.  
Each file contains:
- Date  
- kWh (energy used)  

### 2. Uses Python Classes  
I used OOP concepts:
- **MeterReading** : stores one reading  
- **Building** : stores all readings for a building  
- **CampusManager** : manages all buildings  

### 3. Calculates Energy Usage  
The program calculates:
- Daily total energy  
- Weekly total energy  
- Total campus consumption  
- Highest consuming building  
- Min/Max/Average usage for each building  

### 4. Creates Graphs  
It makes three graphs:
- Line graph (daily usage)  
- Bar graph (average usage per building)  
- Scatter plot (peak loads)  

These are saved in **dashboard.png**.

### 5. Generates Output Files  
Inside the **output** folder, these files are created:
- cleaned_energy_data.csv  
- daily_totals.csv  
- weekly_totals.csv  
- summary.txt  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## How to Run the Program  

1. Add all CSV files to the **data** folder  
2. Run this command:

3. After running, check the **output** folder and **dashboard.png**  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Conclusion  
This project helped me understand:
- How to read CSV files in Python  
- How OOP works  
- How to use Pandas and Matplotlib  
- How to analyze data and create graphs  

This completes my capstone project for the PPS Python course.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

