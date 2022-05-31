import pandas as pd


def prepare_data(path):
    """Create list of colnames
    Load data into df with sep equal to ':' and '_'
    Create var 'month' with df data from row 0 and col 0
    Drop the row 0 where 'month' was
    Reset index, so it again starts with 0
    Convert all col dtypes to int64

    Args:
        path (str): path to your data

    Returns:
        _type_: _description_
        month (str): month when data was taken
        df (df): DataFrame with study data
    """
    colnames = ["Day", "Math", "CS", "Eng", "Sport"]
    df = pd.read_csv(
        filepath_or_buffer=path, sep="[:_]", names=colnames,
        header=None, engine="python")
    month = df.iloc[0][0]
    df.drop(index=0, inplace=True)
    df = df.reset_index(drop=True)
    df[colnames] = df[colnames].astype("int64")
    return month, df