import os

def data_split_by_condition(df, condition, is_save=False, output_dir='.'):
    """
    Split the dataset into two subsets based on a condition.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        condition (pd.Series): A boolean series representing the condition.
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        tuple: A tuple containing the two subsets (df_true, df_false).
    """
    df_true = df[condition]
    df_false = df[~condition]

    # Save to CSV if required
    if is_save:
        os.makedirs(output_dir, exist_ok=True)
        df_true.to_csv(os.path.join(output_dir, 'true_subset.csv'), index=False)
        df_false.to_csv(os.path.join(output_dir, 'false_subset.csv'), index=False)

    return df_true, df_false
