import numpy as np
import os

def data_split_by_group(df, group_column, train_size=0.7, test_size=0.3, validation_size=None, is_save=False, output_dir='.', random_state=None):
    """
    Split the dataset into training, testing, and optionally validation sets based on groups.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        group_column (str): The name of the column representing the groups.
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

    # Get unique groups
    groups = df[group_column].unique()
    np.random.shuffle(groups)

    # Calculate sizes
    train_end = int(train_size * len(groups))
    if validation_size is not None:
        validation_end = train_end + int(validation_size * len(groups))
        train_groups = groups[:train_end]
        validation_groups = groups[train_end:validation_end]
        test_groups = groups[validation_end:]
    else:
        train_groups = groups[:train_end]
        test_groups = groups[train_end:]

    # Split the data
    train = df[df[group_column].isin(train_groups)]
    test = df[df[group_column].isin(test_groups)]
    if validation_size is not None:
        validation = df[df[group_column].isin(validation_groups)]

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
    else:
        return train, test