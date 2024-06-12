def get_EI_dicts(df):
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
        EI_last dict
        EI_count dict
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
