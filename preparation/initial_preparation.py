import pandas as pd


# possible new name for modified prepare_data func
def prepare_initial_df(PATH, DAY_OFFS):
    """
    Summary:
        Prepare data for further operations
    Args:
        PATH (str, constant): path to your data
        DAY_OFFS (int list constant): days when you relax
    Returns:
        _type_: _description_
        month (str): month when the data was taken
        df (df): DataFrame
    """
    # Create list of colnames
    colnames = ["Day", "Math", "CS", "Eng", "Sport",
                "SIL", "OD", "LE", "JG", "GMG"]
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
    cols_to_shorten = ["Sport", "OD", "LE", "JG", "GMG"]
    for col in cols_to_shorten:
        df[col] = df[col].str[2:]
    # Convert col dtypes to int64
    df[colnames] = df[colnames].astype("int64")
    # Create a new col with info about whether
    # you work or relax on a particular day
    df["DKind"] = df.apply(lambda row: categorise(row, DAY_OFFS), axis=1)
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
