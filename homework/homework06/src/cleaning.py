import pandas as pd


def fill_missing_median(df, columns):
    """
    Fill missing values in selected numeric columns with each column's median.
    """
    result = df.copy()

    for col in columns:
        result[col] = result[col].fillna(result[col].median())

    return result


def drop_missing(df, threshold=0.5):
    """
    Drop columns whose proportion of missing values is greater than threshold.
    """
    result = df.copy()
    missing_ratio = result.isna().mean()

    columns_to_drop = missing_ratio[missing_ratio > threshold].index
    return result.drop(columns=columns_to_drop)


def normalize_data(df, columns):
    """
    Min-max normalize selected numeric columns to the range [0, 1].
    """
    result = df.copy()

    for col in columns:
        col_min = result[col].min()
        col_max = result[col].max()

        if col_max != col_min:
            result[col] = (result[col] - col_min) / (col_max - col_min)

    return result
