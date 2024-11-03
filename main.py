import argparse
import json
from datetime import datetime
import os

# File to store the data
DATA_FILE = "time_data.json"

def save_data(time_str, text):
    # Validate military time format
    try:
        datetime.strptime(time_str, "%H:%M")
    except ValueError:
        print("Invalid time format. Use military time (HH:MM).")
        return
    
    # Load existing data if the file exists
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    # Append new entry
    data.append({"time": time_str, "text": text})
    
    # Save updated data
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Data saved: Time - {time_str}, Text - {text}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Store time and text data.")
    parser.add_argument("time", type=str, help="Time in military format (HH:MM)")
    parser.add_argument("text", type=str, help="Text to store")
    
    args = parser.parse_args()
    
    # Save the data
    save_data(args.time, args.text)

if __name__ == "__main__":
    main()

