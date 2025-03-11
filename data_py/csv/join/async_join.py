import pandas as pd
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def async_join(df1, df2, on_column, tolerance):
    """
    Join two dataframes based on the closest values in a column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to join on.
        tolerance (float): The maximum allowed difference between values.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    try:
        # Kiểm tra đầu vào có phải là DataFrame không
        if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
            raise ValueError("Both df1 and df2 must be pandas DataFrames.")

        # Kiểm tra cột join có tồn tại trong cả hai DataFrame không
        if on_column not in df1.columns or on_column not in df2.columns:
            raise ValueError(f"Column '{on_column}' must exist in both DataFrames.")

        # Sắp xếp DataFrame theo cột join
        df1 = df1.sort_values(by=on_column).reset_index(drop=True)
        df2 = df2.sort_values(by=on_column).reset_index(drop=True)

        logging.info("Data sorted and ready for joining.")

        # Thực hiện join
        result = pd.merge_asof(df1, df2, on=on_column, tolerance=tolerance)
        logging.info("Data joined successfully.")

        return result

    except Exception as e:
        logging.error(f"An error occurred while joining data: {str(e)}")
        return None  # Trả về None nếu có lỗi