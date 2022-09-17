import pandas as pd


def prepare_data(path, day_offs):
    """
    Summary:
        Prepare data for further operations

    Args:
        path (str): path to your data

    Returns:
        _type_: _description_
        month (str): month when data was taken
        df (df): DataFrame with study data
    """
    # Create list of colnames
    colnames = ["Day", "Math", "CS", "Eng", "Sport"]
    # Load data into df with sep equal to ':' and '_'
    df = pd.read_csv(
        filepath_or_buffer=path, sep="[:_]", names=colnames,
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
    df["Kind"] = df.apply(lambda row: categorise(row, day_offs), axis=1)
    # Rearrange order of cols
    cols = df.columns.tolist()
    cols = [cols[0]] + [cols[-1]] + cols[1:-1]
    return month, df[cols]


# small func used in lambda expression
def categorise(row, day_offs):
    if row["Day"] in day_offs:
        return "relax"
    return "work"
