import numpy as np
import os

def data_split_custom_ratio(df, ratios = 3, is_save=False, output_dir='.', random_state=None):
    """
    Split the dataset into multiple subsets based on custom ratios.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        ratios (list of float): A list of ratios for each subset (e.g., [0.6, 0.3, 0.1]).
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.
        random_state (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        list: A list of dataframes corresponding to each ratio.
    """
    if abs(sum(ratios) - 1.0) > 1e-6:
        raise ValueError('The sum of ratios must equal 1.0')

    if random_state is not None:
        np.random.seed(random_state)

    # Shuffle the dataframe
    df = df.sample(frac=1).reset_index(drop=True)

    # Calculate split indices
    splits = []
    start = 0
    for ratio in ratios:
        end = start + int(ratio * len(df))
        splits.append(df[start:end])
        start = end

    # Save to CSV if required
    if is_save:
        os.makedirs(output_dir, exist_ok=True)
        for i, split in enumerate(splits):
            split.to_csv(os.path.join(output_dir, f'split_{i + 1}.csv'), index=False)

    return splits