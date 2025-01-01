import pandas as pd


# possible new name for modified prepare_data func
def prepare_initial_df(PATH):
    """
    Summary:
        Here data goes through initial preparation
    Args:
        PATH (str, constant): path to your data
    Returns:
        month (str): month when the data was taken
        df (df): DataFrame

    Cols meaning:
    - Day - day of the month
    - DKind - day kind
    - EC - exercise count
    - EI - exercise intensity - has six levels
    from 0 - didn't exercise to 5 - hard exercise
    (More info in a separate message)
    - OD - outdoor
    - RN - running
    - GM - gaming

    Explanation about all possible Exercise Intensity levels:
    - 0 - you didn't exercise
    - 1 - easy
    - 2 - between easy and moderate
    - 3 - moderate
    - 4 - between moderate and hard
    - 5 - hard
    """
    # Create list of colnames
    colnames = ["Day", "DKind", "Math", "CS", "Eng", "EC", "EI", "OD", "RN", "GM"]
    # Load data into df with sep equal to ':', '_', and '-'
    df = pd.read_csv(
        filepath_or_buffer=PATH,
        sep="[:_-]",
        names=colnames,
        header=None,
        engine="python",
    )
    # Create var 'month' with df data from row 0 and col 0
    month = df.iloc[0][0]
    # Drop the row 0 where 'month' was
    df.drop(index=0, inplace=True)
    # Reset index, so it again starts with 0
    df = df.reset_index(drop=True)
    # in the cols below first two symbols are for easier
    # identification while writing the data. Many thanks
    # to https://stackoverflow.com/a/42349635/11749578
    cols_to_shorten = ["EC", "OD", "RN", "GM"]
    for col in cols_to_shorten:
        df[col] = df[col].str[2:]
    # Convert col dtypes to int64
    cols_to_int = df.columns.difference(["DKind"])
    df[cols_to_int] = df[cols_to_int].astype("int64")
    # Expand 'w' with 'word' and 'r' with 'relax'
    # in the 'DKind' column
    df["DKind"] = df["DKind"].replace({"w": "work", "r": "relax"})
    return month, df
