def data_split (df, train_size = 0.7, test_size = 0.3, validation_size = None, is_save = False):
    """_summary_

    Args:
        df (_type_): _description_
        train_size (float, optional): _description_. Defaults to 0.7.
        test_size (float, optional): _description_. Defaults to 0.3.
        validation_size (_type_, optional): _description_. Defaults to None.
        is_save (bool, optional): _description_. Defaults to False.
    """
    if validation_size is not None:
        if train_size + test_size + validation_size > 1:
            raise ValueError('train_size + test_size + validation_size must be less than 1')
        
        train, validation, test = df.sample(frac = train_size), df.sample(frac = validation_size), df.sample(frac = test_size)

        if is_save:
            train.to_csv('train.csv', index = False)
            validation.to_csv('validation.csv', index = False)
            test.to_csv('test.csv', index = False)
            return train, test, validation
    else:
        if train_size + test_size > 1:
            raise ValueError('train_size + test_size must be less than 1')
        
        train, test = df.sample(frac = train_size), df.sample(frac = test_size)

        if is_save:
            train.to_csv('train.csv', index = False)
            test.to_csv('test.csv', index = False)
        return train, test
