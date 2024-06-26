# This script collects, analyzes, and interprets experimental data 
# for Rae's EIS-based immunoassay device. Summer 2024, Gnulab @ Georgetown.

import csv  # for reading and writing CSV files
import numpy as np  # for numerical operations
import matplotlib.pyplot as plt  # for creating plots
from datetime import datetime  # for handling date and time

def collect_sample_data():
    sample_id           = input("Enter sample ID: ")
    analyte             = input("Enter analyte: ")
    electrolyte         = input("Enter electrolyte: ")
    electrode_material  = input("Enter electrode material: ")
    electrode_area      = float(input("Enter electrode area (cm^2): "))
    cell_volume         = float(input("Enter cell volume (mL): "))
    applied_potential   = float(input("Enter applied potential (V): "))
    temperature         = float(input("Enter temperature (°C): "))
    reference_potential = float(input("Enter reference electrode potential (V): "))
    timestamp           = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")

    measurements = [] # initialize empty list for measurements for an input potential
    while True:
        frequency           = float(input("Enter frequency (Hz): "))
        recorded_current    = float(input("Enter recorded current (A): "))
        phase_angle         = float(input("Enter phase angle (degrees): "))
        measurements.append({
            "frequency": frequency,
            "recorded_current": recorded_current,
            "phase_angle": phase_angle
        })
        cont = input("Add another measurement? (y/n): ") 
        if cont.lower() != 'y':
            break

    sample_data = { # full data dictionary that includes multiple frequency measurements
        "sample_id": sample_id,                    
        "analyte": analyte,                          
        "electrolyte": electrolyte,
        "cell_specs": {
            "electrode_material": electrode_material,
            "electrode_area": electrode_area,
            "cell_volume": cell_volume
        },
        "applied_potential": applied_potential,
        "temperature": temperature,
        "reference_potential": reference_potential,
        "measurements": measurements,
        "timestamp": timestamp
    }

    return sample_data

def store_sample_data(sample_data, filename="eis_data.csv"): # save collected data in CSV
    fieldnames = ["sample_id", 
                  "analyte", 
                  "electrolyte", 
                  "electrode_material", 
                  "electrode_area", 
                  "cell_volume", 
                  "applied_potential", 
                  "temperature", 
                  "reference_potential", 
                  "frequency",
                  "recorded_current", 
                  "phase_angle", 
                  "timestamp"]
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:  # write header only if file is empty
            writer.writeheader()
        for measurement in sample_data["measurements"]:
            row = {
                "sample_id": sample_data["sample_id"],
                "analyte": sample_data["analyte"],
                "electrolyte": sample_data["electrolyte"],
                "electrode_material": sample_data["cell_specs"]["electrode_material"],
                "electrode_area": sample_data["cell_specs"]["electrode_area"],
                "cell_volume": sample_data["cell_specs"]["cell_volume"],
                "applied_potential": sample_data["applied_potential"],
                "temperature": sample_data["temperature"],
                "reference_potential": sample_data["reference_potential"],
                "frequency": measurement["frequency"],
                "recorded_current": measurement["recorded_current"],
                "phase_angle": measurement["phase_angle"],
                "timestamp": sample_data["timestamp"]
            }
            writer.writerow(row)