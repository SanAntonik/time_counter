def get_EIL3plus_count(df, first_day):
    """
    Summary:
        Here we select days after the first day of
        the interval AND days when EIL3+ exercises
        happened. Then we count how many rows of df
        meet the above requirements

        Note: EIL3+ stands for
        Exercise Intensity Level 3 (+) plus
    Args:
        df: df with 'Day' and 'EI' cols
    Returns:
        count of rows
    """
    return len(df.loc[(df["Day"] >= first_day) & (df["EI"] >= 3)])
