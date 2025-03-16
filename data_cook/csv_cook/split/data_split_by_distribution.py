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

    # Split the dataframe into groups
    groups = df.groupby(target_column)

    # Calculate the number of samples for each split
    train_samples = int(train_size * len(df))
    test_samples = int(test_size * len(df))
    validation_samples = int(validation_size * len(df)) if validation_size is not None else 0

    # Initialize empty dataframes for splits
    train, test, validation = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    for name, group in groups:
        # Calculate the number of samples for each group
        group_train_samples = int(train_size * len(group))
        group_test_samples = int(test_size * len(group))
        group_validation_samples = int(validation_size * len(group)) if validation_size is not None else 0

        # Append the samples to the splits
        train = pd.concat([train, group.sample(n=group_train_samples, replace=False)])
        test = pd.concat([test, group.sample(n=group_test_samples, replace=False)])
        if validation_size is not None:
            validation = pd.concat([validation, group.sample(n=group_validation_samples, replace=False)])

    # Save to CSV if required
    if is_save:
        os.makedirs(output_dir, exist_ok=True)
        train.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        if validation_size is not None:
            validation.to_csv(os.path.join(output_dir, 'validation.csv'), index=False)

    # Return splits
    if validation_size is not None:
        return train, test, validation
