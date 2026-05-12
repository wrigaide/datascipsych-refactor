"""Example code library."""

from pathlib import Path
import polars as pl


def get_sample_data():
    """Get a sample DataFrame for demonstration purposes."""
    df = pl.DataFrame(
        {
            'trial': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            'condition': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            'correct': [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
        }
    )
    return df


def convert_excel_to_csv(excel_file, csv_file = None):
    """
    Convert an Excel file to a CSV file.

    Args:

      excel_file: Path to an Excel file.

      csv_file: Path to a CSV file. If not specified, the path to the CSV file 
        will be the same as the Excel file but with a .csv file extension.
    """
    df=pl.read_excel(excel_file)
    if csv_file is None:
        csv_file=Path(excel_file).with_suffix(".csv")
    df.write_csv(csv_file)
