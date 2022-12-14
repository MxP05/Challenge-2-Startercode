# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import fire
from pathlib import Path
import questionary


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
    
def save_csv(bankdata, csvpath, header):
    """Saves the CSV file from path provided.

        Args:
        csv (Path): The CSV file path.
        bankdata (list of lists): A list of the rows of data for the CSV file.
        header (list): An optional header for the CSV.

        """
        #opens write mode, path points out location of files
    with open(csvpath, "w", newline ="") as csvfile:
        #writes  csvfile according to data supplied
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)

        #loop through bankdata
        for loan in bankdata:
                csvwriter.writerow(loan)