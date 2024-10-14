#!/usr/bin/env python3

import argparse
from datetime import datetime
import calendar

def generate_dates(year):
    # List for all dates
    date_list = []

    # Loop through all months and days in the year
    for month in range(1, 13):
        # Use monthrange to get the number of days in the month
        _, days_in_month = calendar.monthrange(year, month)
        
        for day in range(1, days_in_month + 1):
            current_date = datetime(year, month, day)
            
            # Create different date formats
            yyyymmdd = current_date.strftime('%Y%m%d')  # YYYYMMDD
            yyyyddmm = current_date.strftime('%Y%d%m')  # YYYYDDMM
            yymmdd = current_date.strftime('%y%m%d')    # YYMMDD
            yyddmm = current_date.strftime('%y%d%m')    # YYDDMM
            ddmmyyyy = current_date.strftime('%d%m%Y')  # DDMMYYYY
            ddmmyy = current_date.strftime('%d%m%y')    # DDMMYY
            mmddyyyy = current_date.strftime('%m%d%Y')  # MMDDYYYY
            mmddyy = current_date.strftime('%m%d%y')    # MMDDYY

            # Add all formats as a group to the list
            date_list.append((current_date, [yyyymmdd, yyyyddmm, yymmdd, yyddmm, ddmmyyyy, ddmmyy, mmddyyyy, mmddyy]))

    return date_list

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Generate dates of a year in various formats.")
    parser.add_argument('-y', '--year', type=int, required=True, help="The year for which to generate the dates")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Generate dates
    dates = generate_dates(args.year)
    
    # Sort the dates by datetime
    dates.sort(key=lambda x: x[0])  # Sort by the datetime object

    # Display all records one below the other
    for _, formats in dates:
        for date_string in formats:
            print(date_string)

if __name__ == "__main__":
    main()
