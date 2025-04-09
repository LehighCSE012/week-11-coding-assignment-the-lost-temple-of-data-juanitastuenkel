""" Week 11 Assignment Juanita Stuenkel"""

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """Reads artifact data from a specific sheet ('Main Chamber') in an Excel file. """
    try:
        df_artifact = pd.read_excel(excel_filepath, sheet_name="Main Chamber", skiprows=3)
        return df_artifact
    except FileNotFoundError:
        print(f"File not found at '{excel_filepath}'")
        return None

def load_location_notes(tsv_filepath):
    """Reads location data from a Tab-Separated Value (TSV) file. """
    try:
        df_location = pd.read_csv(tsv_filepath, sep = '\t')
        return df_location
    except FileNotFoundError:
        print(f"File not found at '{tsv_filepath}'")
        return None

def extract_journal_dates(journal_text):
    """Extracts all dates in MM/DD/YYYY format from the journal text. """
    pattern = r"((0[1-9]|1[012])/(0[1-9]|[12][0-9]|3[01])/\d{4})"
    dates = re.findall(pattern, journal_text)
    return dates

def extract_secret_codes(journal_text):
    """Extracts all secret codes from the journal text."""
    pattern = r"AZMAR-\d{3}"
    codes = re.findall(pattern, journal_text)
    return codes
