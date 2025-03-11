import pandas as pd
import logging

def group_and_filter(dataframe: pd.DataFrame, group_by_column, filter_function):
    """
    Group the dataframe by a column and filter groups based on a condition.

    This function takes a dataframe, a column to group by, and a filter function as input.
    It groups the dataframe by the specified column, applies the filter function to each group,
    and returns a new dataframe containing only the filtered groups.

    Args:
        dataframe (pd.DataFrame): The input dataframe.
        group_by_column (str or list): The column(s) to group by.
        filter_function (function): A function to filter groups. It should return a boolean.

    Returns:
        pd.DataFrame: A dataframe containing only the filtered groups.
    """
    if (dataframe is None) or (group_by_column is None) or (filter_function is None):
        raise ValueError("dataframe, group_by_column, and filter_function cannot be None")

    try:
        # Group the dataframe by the specified column
        grouped = dataframe.groupby(group_by_column)

        # Filter groups based on the filter function
        filtered_groups = [group for _, group in grouped if filter_function(group)]

        # Concatenate the filtered groups into a new dataframe
        return pd.concat(filtered_groups)
    except Exception as error:
        # Log any errors that occur
        logging.error(f"An error occurred while filtering groups: {str(error)}")
        raise
