import pandas as pd


# possible new name for modified prepare_data func
def prepare_initial_df(PATH, DAY_OFFS):
    """
    Summary:
        Here data goes through initial preparation
    Args:
        PATH (str, constant): path to your data
        DAY_OFFS (int list, constant): days when you relax
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
    - LE - left-eye reading
    - JG - juggling
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
    colnames = ["Day", "Math", "CS", "Eng", "EC",
                "EI", "OD", "LE", "JG", "GM"]
    # Load data into df with sep equal to ':', '_', and '-'
    df = pd.read_csv(
        filepath_or_buffer=PATH, sep="[:_-]", names=colnames,
        header=None, engine="python")
    # Create var 'month' with df data from row 0 and col 0
    month = df.iloc[0][0]
    # Drop the row 0 where 'month' was
    df.drop(index=0, inplace=True)
    # Reset index, so it again starts with 0
    df = df.reset_index(drop=True)
    # in the cols below first two symbols are for easier
    # identification while writing the data. Many thanks
    # to https://stackoverflow.com/a/42349635/11749578
    cols_to_shorten = ["EC", "OD", "LE", "JG", "GM"]
    for col in cols_to_shorten:
        df[col] = df[col].str[2:]
    # Convert col dtypes to int64
    df[colnames] = df[colnames].astype("int64")
    # Create a new col with info about whether
    # you work or relax on a particular day
    df["DKind"] = df.apply(lambda row: categorise(row, DAY_OFFS),
                           axis=1)
    # Rearrange order of cols, so col 'DKind'
    # goes after col 'Day'
    cols = df.columns.tolist()
    cols = [cols[0]] + [cols[-1]] + cols[1:-1]
    return month, df[cols]


# this small func is used in lambda
# expression in prepare_initial_df function
def categorise(row, DAY_OFFS):
    if row["Day"] in DAY_OFFS:
        return "relax"
    return "work"
