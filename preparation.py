import pandas as pd


def prepare_data(PATH, DAY_OFFS):
    """
    Summary:
        Prepare data for further operations

    Args:
        PATH (str, constant): path to your data
        DAY_OFFS (int list constant): days when you relax

    Returns:
        _type_: _description_
        month (str): month when data was taken
        df (df): DataFrame with study data
    """
    # Create list of colnames
    colnames = ["Day", "Math", "CS", "Eng", "Sport"]
    # Load data into df with sep equal to ':' and '_'
    df = pd.read_csv(
        filepath_or_buffer=PATH, sep="[:_]", names=colnames,
        header=None, engine="python")
    # Create var 'month' with df data from row 0 and col 0
    month = df.iloc[0][0]
    # Drop the row 0 where 'month' was
    df.drop(index=0, inplace=True)
    # Reset index, so it again starts with 0
    df = df.reset_index(drop=True)
    # Convert all col dtypes to int64
    df[colnames] = df[colnames].astype("int64")
    # Create a new col with info about whether
    # you work or relax on a particular day
    df["Kind"] = df.apply(lambda row: categorise(row, DAY_OFFS), axis=1)
    # Create two day_offs vars for generate_report
    # func. With these two vars, reports will
    # provide a more detailed picture of the month
    day_offs_count = len(DAY_OFFS)
    if day_offs_count > 0:
        day_offs_str = ', '.join(map(str, DAY_OFFS))
    else:
        day_offs_str = "you studied every day"
    # Rearrange order of cols
    cols = df.columns.tolist()
    cols = [cols[0]] + [cols[-1]] + cols[1:-1]
    return month, df[cols], day_offs_count, day_offs_str


# small func used in lambda expression
def categorise(row, DAY_OFFS):
    if row["Day"] in DAY_OFFS:
        return "relax"
    return "work"
