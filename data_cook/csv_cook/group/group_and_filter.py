import pandas as pd
import logging

def group_and_filter(dataframe: pd.DataFrame, group_by_column, filter_function):
    if (dataframe is None) or (group_by_column is None) or (filter_function is None):
        raise ValueError("dataframe, group_by_column, and filter_function cannot be None")

    try:
        grouped = dataframe.groupby(group_by_column)
        filtered_groups = [group for _, group in grouped if filter_function(group)]

        # Nếu không có nhóm nào được giữ lại, trả về DataFrame rỗng cùng cột
        return pd.concat(filtered_groups) if filtered_groups else pd.DataFrame(columns=dataframe.columns)
    except Exception as error:
        logging.error(f"An error occurred while filtering groups: {str(error)}")
        raise

