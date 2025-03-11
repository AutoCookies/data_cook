import pandas as pd
import logging

def group_and_split(df: pd.DataFrame, group_column, train_size=0.7, random_state=None):
    """
    Group the dataframe by a column and split each group into train and test sets.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        train_size (float): The proportion of the dataset to include in the train split.
        random_state (int): Random seed for reproducibility.

    Returns:
        tuple: A tuple containing the train and test dataframes.
    """
    train_list, test_list = [], []
    
    try:
        grouped = df.groupby(group_column)
        for _, group in grouped:
            group = group.sample(frac=1, random_state=random_state).reset_index(drop=True)
            train_end = int(train_size * len(group))
            train_list.append(group[:train_end])
            test_list.append(group[train_end:])
        logging(f"Split {len(df)} groups into {len(train_list)} train groups and {len(test_list)} test groups.")
        return pd.concat(train_list), pd.concat(test_list)
    except Exception as e:
        logging.error(f"An error occurred while splitting groups: {str(e)}")
    