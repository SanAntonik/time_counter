from .get_EI_dicts import get_EI_dicts


def handle_nonstudy_data(df):
    """
    Summary:
        Here you do operations with nonstudy data
    Args:
        df: df containing non-study data
    Returns:
        list of data
    """
    # get last value from the 'EC' col
    ex_count = df["EC"].iloc[-1]
    EI_last, EI_count = get_EI_dicts(df[["Day", "EI"]])
    cols = ["OD", "LE", "JG", "GM"]
    # find total in hours for the selected above cols
    hs_total_per_col = df[cols].sum(
        axis=0).div(60).round(2).to_list()
    # count how many days you pursued selected activities
    day_count_per_col = [(df[col] != 0).sum() for col in cols]
    report_data = [cols, ex_count, hs_total_per_col,
                   day_count_per_col, EI_count]
    return [EI_last, report_data]
