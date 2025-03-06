import pandas as pd
import os

def data_group(df, group_column, is_save=False, output_dir='.'):
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
    # Group the dataframe by the specified column
    grouped = df.groupby(group_column)

    # Create a dictionary to store the groups
    groups_dict = {key: group for key, group in grouped}

    # Save each group to a CSV file if is_save is True
    if is_save:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Save each group to a separate CSV file
        for key, group in groups_dict.items():
            filename = f"{group_column}_{key}.csv"
            filepath = os.path.join(output_dir, filename)
            group.to_csv(filepath, index=False)
            print(f"Saved group '{key}' to {filepath}")

    return groups_dict