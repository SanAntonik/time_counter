def handle_nonstudy_data(df):
    """
    Summary:
        Here you do operations with nonstudy data
    Args:
        df: df containing non-study data
    Returns:
        list of data
    """
    cur_day = df["Day"].iloc[-1]
    # get last value from the 'EC' col
    ex_count = df["EC"].iloc[-1]
    EI_last, EI_count = handle_EI(df)
    cols = ["OD", "LE", "JG", "GM"]
    # find total in hours for the selected above cols
    hs_total_per_col = df[cols].sum(
        axis=0).div(60).round(2).to_list()
    # count how many days you pursued selected activities
    day_count_per_col = [(df[col] != 0).sum() for col in cols]
    return [cur_day, ex_count, EI_last, EI_count, cols,
            hs_total_per_col, day_count_per_col]


def handle_EI(df):
    """
    Summary:
        Get two EI dictionaries
        'EI_last' shows the most recent
        day when you had an exercise of a particular
        intensity (used in daily stats)
        'EI_count' returns exercise count per
        intensity (used in montly stats and reports)
    Args:
        df of nonstudy data
    Returns:
        EI_last dir
        EI_count dir
    Important:
        If value equals '100' in EI_last, it means you
        didn't have exercise of that particular intensity
    """
    EI_last = {}
    EI_count = {}
    # move from intensity level 1 to 5
    for i in range(1, 6):
        try:
            data = df[df["EI"] == i]
            EI_last[i] = data["Day"].iloc[-1]
            EI_count[i] = len(data)
        except IndexError:
            # print(
            #     f"This month doesn't have data for EI level '{i}'")
            # put 100, so later you'll get a negative number to spot
            # that you didn't have exercise of that particular level
            EI_last[i] = 100
            EI_count[i] = 0
    return EI_last, EI_count
