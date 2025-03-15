import os

def data_split_time_series(df, date_column, train_size=0.7, test_size=0.3, validation_size=None, is_save=False, output_dir='.'):
    """
    Split the dataset into training, testing, and optionally validation sets based on time.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        date_column (str): The name of the date column for time-based splitting.
        train_size (float, optional): The proportion of the dataset to include in the train split. Defaults to 0.7.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.3.
        validation_size (float, optional): The proportion of the dataset to include in the validation split. Defaults to None.
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.
        output_dir (str, optional): The directory to save the output files. Defaults to '.'.

    Returns:
        tuple: A tuple containing the train, test, and validation dataframes (if validation_size is not None).
    """
    if validation_size is not None:
        if train_size + test_size + validation_size > 1:
            raise ValueError('train_size + test_size + validation_size must be less than or equal to 1')
        
        # Sort the dataframe by date
        df = df.sort_values(by=date_column).reset_index(drop=True)
        
        # Calculate the sizes
        train_end = int(train_size * len(df))
        validation_end = train_end + int(validation_size * len(df))
        
        # Split the data
        train = df[:train_end]
        validation = df[train_end:validation_end]
        test = df[validation_end:]
        
        if is_save:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            train.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
            validation.to_csv(os.path.join(output_dir, 'validation.csv'), index=False)
            test.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        
        return train, test, validation
    else:
        if train_size + test_size > 1:
            raise ValueError('train_size + test_size must be less than or equal to 1')
        
        # Sort the dataframe by date
        df = df.sort_values(by=date_column).reset_index(drop=True)
        
        # Calculate the sizes
        train_end = int(train_size * len(df))
        
        # Split the data
        train = df[:train_end]
        test = df[train_end:]
        
        if is_save:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            train.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
            test.to_csv(os.path.join(output_dir, 'test.csv'), index=False)
        
        return train, test