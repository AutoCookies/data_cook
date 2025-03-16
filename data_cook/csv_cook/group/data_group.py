import pandas as pd
import os
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def data_group(df: pd.DataFrame, group_column, is_save=False, output_dir='.'):
    """
    Group the dataset by a specific column and optionally save each group to a separate CSV file.

    Args:
        df (pd.DataFrame): The input dataframe to be grouped.
        group_column (str): The name of the column to group by.
        is_save (bool, optional): Whether to save each group to a CSV file. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        dict: A dictionary where keys are the unique values in the group column, and values are the corresponding dataframes.
    """

    if df is None or group_column is None:
        raise ValueError("df and group_column cannot be None")

    if group_column not in df.columns:
        raise KeyError(f"Column '{group_column}' not found in DataFrame")

    try:
        grouped = df.groupby(group_column)
        groups_dict = {key: group for key, group in grouped}

        if is_save:
            os.makedirs(output_dir, exist_ok=True)

            for key, group in groups_dict.items():
                filename = f"{group_column}_{key}.csv"
                filepath = os.path.join(output_dir, filename)
                group.to_csv(filepath, index=False)
                logging.info(f"Saved group '{key}' to {filepath}")

        logging.info(f"Number of groups: {len(groups_dict)}")
        return groups_dict

    except Exception as e:
        logging.error(f"An error occurred while grouping data: {str(e)}")
        raise  # Ném lại lỗi để unittest có thể bắt lỗi đúng cách
