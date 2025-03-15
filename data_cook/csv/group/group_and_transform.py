import logging
import pandas as pd

def group_and_transform_data(
    data: pd.DataFrame, group_by_column: str, transform_column: str, transform_function
) -> pd.DataFrame:
    """
    Group the dataframe by a column and apply a transformation to each group.

    Args:
        data (pd.DataFrame): The input dataframe.
        group_by_column (str): The column to group by.
        transform_column (str): The column to apply the transformation to.
        transform_function (function): The transformation function.

    Returns:
        pd.DataFrame: A dataframe with the transformed column.
    """
    if data is None:
        raise ValueError("data cannot be None")
    if group_by_column is None:
        raise ValueError("group_by_column cannot be None")
    if transform_column is None:
        raise ValueError("transform_column cannot be None")
    if transform_function is None:
        raise ValueError("transform_function cannot be None")

    try:
        # Apply the transformation function directly using groupby and transform
        if transform_column not in data.columns:
            raise ValueError(
                f"transform_column '{transform_column}' does not exist in the dataframe"
            )
        data[f"{transform_column}_transformed"] = data.groupby(group_by_column)[
            transform_column
        ].transform(transform_function)
        return data
    except Exception as error:
        logging.error(f"Error during grouping and transformation: {str(error)}")
        raise
