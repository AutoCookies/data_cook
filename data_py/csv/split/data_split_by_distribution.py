import pandas as pd
import os
import numpy as np

def data_split_by_distribution(df, target_column, train_size=0.7, test_size=0.3, validation_size=None, is_save=False, output_dir='.', random_state=None):
    """
    Split the dataset into training, testing, and optionally validation sets while preserving the distribution of a target column.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        target_column (str): The name of the target column to preserve the distribution.
        train_size (float, optional): The proportion of the dataset to include in the train split. Defaults to 0.7.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.3.
        validation_size (float, optional): The proportion of the dataset to include in the validation split. Defaults to None.
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.
        random_state (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        tuple: A tuple containing the train, test, and validation dataframes (if validation_size is not None).
    """
    if random_state is not None:
        np.random.seed(random_state)

    # Group by the target column to preserve distribution
    grouped = df.groupby(target_column)

    # Initialize empty dataframes for splits
    train, test, validation = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    for _, group in grouped:
        # Shuffle the group
        group = group.sample(frac=1).reset_index(drop=True)

        # Calculate sizes for each split
        train_end = int(train_size * len(group))
        if validation_size is not None:
            validation_end = train_end + int(validation_size * len(group))
            train = pd.concat([train, group[:train_end]])
            validation = pd.concat([validation, group[train_end:validation_end]])
            test = pd.concat([test, group[validation_end:]])
        else:
            train = pd.concat([train, group[:train_end]])
            test = pd.concat([test, group[train_end:]])

    # Save to CSV if required
    if is_save:
        os.makedirs(output_dir, exist_ok=True)
        train.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        if validation_size is not None:
            validation.to_csv(os.path.join(output_dir, 'validation.csv'), index=False)

    # Return splits
    if validation_size is not None:
        return train, test