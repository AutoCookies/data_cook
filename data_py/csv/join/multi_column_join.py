from typing import List
import pandas as pd

def join_on_multiple_columns(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    columns: List[str],
    join_type: str = 'inner'
) -> pd.DataFrame:
    """
    Join two dataframes based on multiple common columns.

    Args:
        df1 (pd.DataFrame): The left dataframe.
        df2 (pd.DataFrame): The right dataframe.
        columns (List[str]): The list of columns to join on.
        join_type (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    # Ensure that both inputs are DataFrames
    if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
        raise ValueError("Both df1 and df2 must be pandas DataFrames.")
    
    # Validate that 'columns' is a list of strings
    if not isinstance(columns, list) or not all(isinstance(col, str) for col in columns):
        raise ValueError("columns must be a list of strings.")
    
    # Check if the join type is valid
    if join_type not in ['inner', 'outer', 'left', 'right']:
        raise ValueError("Invalid join type. Valid options are 'inner', 'outer', 'left', 'right'.")
    
    # Set the specified columns as the index for both dataframes
    # This is necessary for joining on multiple columns
    df1_set_index = df1.set_index(columns)
    df2_set_index = df2.set_index(columns)
    
    # Perform the join operation using the specified join type
    # The join is performed on the indices, which are the columns we set earlier
    merged = pd.merge(df1_set_index, df2_set_index, how=join_type)
    
    # Reset the index to bring the joined columns back to the dataframe's columns
    merged.reset_index(inplace=True)
    
    # Return the merged dataframe
    return merged
