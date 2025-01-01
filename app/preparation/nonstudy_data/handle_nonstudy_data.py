from .utils.get_EI_dicts import get_EI_dicts
from .utils.get_EIL3plus_count import get_EIL3plus_count


def handle_nonstudy_data(df, first_day):
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
    EI3plus_count = get_EIL3plus_count(df[["Day", "EI"]], first_day)
    cols = ["OD", "RN", "GM"]
    # find total in hours for the selected above cols
    hs_total_per_col = df[cols].sum(axis=0).div(60).round(2).to_list()
    # count how many days you pursued selected activities
    day_count_per_col = [(df[col] != 0).sum() for col in cols]
    # pack values
    report_data = [cols, ex_count, hs_total_per_col, day_count_per_col, EI_count]
    feedback_data = [EI_last, EI3plus_count, first_day]
    return [feedback_data, report_data]
