import os
from sklearn.model_selection import KFold

def data_split_cross_validation(df, n_splits=5, is_save=False, output_dir='.'):
    """
    Generate cross-validation folds from the dataset.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        n_splits (int, optional): The number of folds. Defaults to 5.
        is_save (bool, optional): Whether to save the folds to CSV files. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        list: A list of tuples containing the train and test dataframes for each fold.
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    folds = []

    for fold, (train_index, test_index) in enumerate(kf.split(df)):
        train = df.iloc[train_index]
        test = df.iloc[test_index]

        if is_save:
            os.makedirs(output_dir, exist_ok=True)
            train.to_csv(os.path.join(output_dir, f'train_fold_{fold + 1}.csv'), index=False)
            test.to_csv(os.path.join(output_dir, f'test_fold_{fold + 1}.csv'), index=False)

        folds.append((train, test))

    return folds