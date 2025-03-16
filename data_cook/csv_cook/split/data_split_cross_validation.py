import os
from sklearn.model_selection import KFold
import pandas as pd

def generate_cross_validation_folds(dataframe: pd.DataFrame, num_folds=5, save_to_disk=False, output_directory='.'):
    """
    Generate cross-validation folds from the dataset.

    Args:
        dataframe (pd.DataFrame): The input dataframe to be split.
        num_folds (int, optional): The number of folds. Defaults to 5.
        save_to_disk (bool, optional): Whether to save the folds to CSV files. Defaults to False.
        output_directory (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        list: A list of tuples containing the train and test dataframes for each fold.
    """
    if dataframe is None:
        raise ValueError("dataframe cannot be None")

    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("dataframe must be a pandas DataFrame")

    if num_folds is None or num_folds < 2:
        raise ValueError("num_folds must be at least 2")

    if not isinstance(num_folds, int):
        raise ValueError("num_folds must be an integer")

    if save_to_disk and not isinstance(output_directory, str):
        raise ValueError("output_directory must be a string")

    kf = KFold(n_splits=num_folds, shuffle=True)
    folds = [(dataframe.iloc[train_index], dataframe.iloc[test_index]) for train_index, test_index in kf.split(dataframe)]

    if save_to_disk:
        os.makedirs(output_directory, exist_ok=True)
        for fold, (train_set, test_set) in enumerate(folds):
            train_file_path = os.path.join(output_directory, f'train_fold_{fold + 1}.csv')
            test_file_path = os.path.join(output_directory, f'test_fold_{fold + 1}.csv')
            train_set.to_csv(train_file_path, index=False)
            test_set.to_csv(test_file_path, index=False)

    return folds
