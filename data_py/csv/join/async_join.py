import pandas as pd
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def async_join(df1, df2, on_column, tolerance):
    """
    Join two dataframes based on the closest values in a column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to join on.
        tolerance (float): The maximum allowed difference between values.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    try:
        # Check if df1 and df2 are pandas DataFrames
        if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
            raise ValueError("Both df1 and df2 must be pandas DataFrames.")

        # Check if the on_column exists in both DataFrames
        if on_column not in df1.columns or on_column not in df2.columns:
            raise ValueError(f"Column '{on_column}' must exist in both DataFrames.")

        # Sort the DataFrames by the on_column
        df1 = df1.sort_values(by=on_column)
        df2 = df2.sort_values(by=on_column)

        logging.info("Data sorted and ready for joining.")

        # Perform the join
        result = pd.merge_asof(
            df1, df2, on=on_column,
            direction='nearest',
            tolerance=tolerance
        )

        logging.info("Data joined successfully.")

        return result

    except Exception as e:
        # Log the error and return None
        logging.error(f"An error occurred while joining data: {str(e)}")
        return None
