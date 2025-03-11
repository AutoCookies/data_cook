import logging
import pandas as pd

def group_and_transform(df: pd.DataFrame, group_column, transform_column, transform_func):
    """
    Group the dataframe by a column and apply a transformation to each group.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        transform_column (str): The column to apply the transformation to.
        transform_func (function): The transformation function.

    Returns:
        pd.DataFrame: A dataframe with the transformed column.
    """
    try:
        df[f'transformed_{transform_column}'] = df.groupby(group_column)[transform_column].transform(transform_func)
        logging("All groups transformed")
        return df
    except Exception as e:
        logging.error(f"An error occurred while grouping and transforming data: {str(e)}")