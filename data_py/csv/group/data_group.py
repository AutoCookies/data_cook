import pandas as pd
import os
import logging

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

    # Validate input arguments
    if (df is None) or (group_column is None):
        raise ValueError("df and group_column cannot be None")
    
    try:
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
                # Generate the filename
                filename = f"{group_column}_{key}.csv"
                filepath = os.path.join(output_dir, filename)

                # Save the group to the CSV file
                group.to_csv(filepath, index=False)
                print(f"Saved group '{key}' to {filepath}")

        # Log the number of groups
        logging(f"Number of groups: {len(groups_dict)}")
        return groups_dict
    
    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred while grouping data: {str(e)}")
