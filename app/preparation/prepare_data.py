import pandas as pd

from .utils.initial_preparation import prepare_initial_df
from .utils.calc_study_data import calc_study_data
from .utils.handle_day_offs import handle_day_offs
from .nonstudy_data.handle_nonstudy_data import handle_nonstudy_data


def prepare_data(PATH, DESIRED_MEAN_VALUE):
    """
    Summary:
        Centerpiece of the package. Here all
        prep and calc funcs are used to
        prepare data for future operations
    Args:
        PATH (str, constant): path to the txt file with data
        DESIRED_MEAN_VALUE (str, constant): desired amount of study time
            per work day
    Returns:
        three lists of data
    """
    # in_df means initial_df; st_df means study_df
    month, in_df = prepare_initial_df(PATH)
    wide_use_data, *st_rep_data = calc_study_data(
        in_df[["Day", "DKind", "Math", "CS", "Eng"]], DESIRED_MEAN_VALUE
    )
    # unpack wide_use_data
    st_df, mean, std, min_to_study = wide_use_data
    # combine st_df with nonstudy cols starting with 'Sport' col
    nonstudy_df = in_df[["Day", "EC", "EI", "RN"]]
    # concatenate study and nonstudy dfs to create the final df
    # drop 'Day' col in nonstudy_df to avoid dublicate col
    # ('Day' col is already present in st_df)
    out_df = pd.concat([st_df, nonstudy_df.drop("Day", axis=1)], axis=1)
    # Create vars for mostly feedback code
    last_day_total = out_df["Total"].iloc[-1]
    last_day = out_df["Day"].iloc[-1]
    # you subtrack 6 here to get a week interval that will be used to
    # discover how many EIL3+ exercises you had from the last recorded
    # day to 7 days before
    first_day = last_day - 6
    feedback_data, nonst_rep_data = handle_nonstudy_data(nonstudy_df, first_day)
    # pack values before returning them
    st_rep_data += handle_day_offs(out_df)
    report_data = st_rep_data, nonst_rep_data
    feedback_data += min_to_study, last_day_total, last_day
    wide_use_data = [month, mean, std, out_df]
    return report_data, wide_use_data, feedback_data
