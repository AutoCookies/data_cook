import pandas as pd
import logging

def group_and_split(df: pd.DataFrame, group_column, train_size=0.7, random_state=None):
    """
    Group the dataframe by a column and split each group into train and test sets.

    This function splits the dataframe into groups based on the given column(s).
    Then, for each group, it randomly splits the data into two subsets: training and testing.
    The training set will contain a proportion of data determined by the train_size argument.
    The remaining data will be included in the testing set.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        train_size (float): The proportion of the dataset to include in the train split.
        random_state (int): Random seed for reproducibility.

    Returns:
        tuple: A tuple containing the train and test dataframes.
    """
    try:
        # Check for bugs
        if df is None or group_column is None:
            raise ValueError("df and group_column cannot be None")
        if train_size > 1 or train_size < 0:
            raise ValueError("train_size must be between 0 and 1")
        if random_state is not None and not isinstance(random_state, int):
            raise ValueError("random_state must be an integer")
        
        # Group the dataframe by the given column(s)
        grouped = df.groupby(group_column)
        # Initialize lists to store the train and test dataframes
        train_list, test_list = [], []
        # Iterate over each group
        for _, group in grouped:
            # Calculate the size of the training set
            train_end = int(train_size * len(group))
            # Append the training and testing sets to the lists
            train_list.append(group.iloc[:train_end])
            test_list.append(group.iloc[train_end:])
        # Log the result
        logging.info(f"Split {len(df)} groups into {len(train_list)} train groups and {len(test_list)} test groups.")
        # Return the concatenated training and testing dataframes
        return pd.concat(train_list), pd.concat(test_list)
    except Exception as e:
        # Log any errors
        logging.error(f"An error occurred while splitting groups: {str(e)}")
    