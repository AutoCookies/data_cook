def data_split(df, train_size=0.7, test_size=0.3, validation_size=None, is_save=False):
    """
    Split the dataset into training, testing, and optionally validation sets.

    Args:
        df (pd.DataFrame): The input dataframe to be split.
        train_size (float, optional): The proportion of the dataset to include in the train split. Defaults to 0.7.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.3.
        validation_size (float, optional): The proportion of the dataset to include in the validation split. Defaults to None.
        is_save (bool, optional): Whether to save the splits to CSV files. Defaults to False.

    Returns:
        tuple: A tuple containing the train, test, and validation dataframes (if validation_size is not None).
    """
    if validation_size is not None:
        if train_size + test_size + validation_size > 1:
            raise ValueError('train_size + test_size + validation_size must be less than or equal to 1')
        
        # Shuffle the dataframe
        df = df.sample(frac=1).reset_index(drop=True)
        
        # Calculate the sizes
        train_end = int(train_size * len(df))
        validation_end = train_end + int(validation_size * len(df))
        
        # Split the data
        train = df[:train_end]
        validation = df[train_end:validation_end]
        test = df[validation_end:]
        
        if is_save:
            train.to_csv('train.csv', index=False)
            validation.to_csv('validation.csv', index=False)
            test.to_csv('test.csv', index=False)
        
        return train, test, validation
    else:
        if train_size + test_size > 1:
            raise ValueError('train_size + test_size must be less than or equal to 1')
        
        # Shuffle the dataframe
        df = df.sample(frac=1).reset_index(drop=True)
        
        # Calculate the sizes
        train_end = int(train_size * len(df))
        
        # Split the data
        train = df[:train_end]
        test = df[train_end:]
        
        if is_save:
            train.to_csv('train.csv', index=False)
            test.to_csv('test.csv', index=False)
        
        return train, test