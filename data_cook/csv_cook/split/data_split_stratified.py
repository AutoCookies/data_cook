import os
import pandas as pd
import numpy as np

def data_split_stratified(df, target_column, train_size=0.7, test_size=0.3, validation_size=None, is_save=False, random_state=None, output_dir='.'):
    """
    Split the dataset into training, testing, and optionally validation sets using stratified sampling.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        target_column (str): The name of the target column for stratified sampling.
        train_size (float, optional): The proportion of the dataset to include in the train split. Defaults to 0.7.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.3.
        validation_size (float, optional): The proportion of the dataset to include in the validation split. Defaults to None.
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.
        random_state (int, optional): Random seed for reproducibility. Defaults to None.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        tuple: A tuple containing the train, test, and validation dataframes (if validation_size is not None).
    """
    # Validate input sizes
    if validation_size is not None:
        if train_size + test_size + validation_size != 1:
            raise ValueError('train_size + test_size + validation_size must equal 1')
    else:
        if train_size + test_size != 1:
            raise ValueError('train_size + test_size must equal 1')

    # Set random seed for reproducibility
    if random_state is not None:
        np.random.seed(random_state)

    # Initialize empty dataframes for splits
    train, test, validation = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    # Group by the target column to ensure stratified sampling
    grouped = df.groupby(target_column)

    for _, group in grouped:
        # Shuffle the group
        group = group.sample(frac=1, random_state=random_state).reset_index(drop=True)

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
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        train.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        if validation_size is not None:
            validation.to_csv(os.path.join(output_dir, 'validation.csv'), index=False)

    # Return splits
    if validation_size is not None:
        return train, test, validation
    else:
        return train, test
