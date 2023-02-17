import pandas as pd

from .initial_preparation import prepare_initial_df
from .calc_study_data import calc_study_data
from .handle_day_offs import handle_day_offs
from .handle_nonstudy_data import handle_nonstudy_data


def prepare_data(PATH, DAY_OFFS, DESIRED_MEAN_VALUE):
    """
    Summary:
        Centerpiece of the package. Here all
        prep and calc funcs are used to
        prepare data for future operations
    Args:
        PATH (str, constant): path to the txt file with data
        DAY_OFFS (int list, constant): days offs
        DESIRED_MEAN_VALUE (str, constant): how
        many min you want to study per work day
    Returns:
        two lists of data
    """
    # in_df means initial_df; st_df means study_df
    month, in_df = prepare_initial_df(PATH, DAY_OFFS)
    wide_use_data, *st_rep_data = calc_study_data(in_df[["Day", "DKind",
                                                         "Math", "CS",
                                                         "Eng"]],
                                                  DESIRED_MEAN_VALUE)
    # unpack wide_use_data
    st_df, mean, std, min_to_study = wide_use_data
    # combine st_df with nonstudy cols starting with 'Sport' col
    nonstudy_df = in_df[["Day", "EC", "EI", "OD", "LE", "JG", "GM"]]
    # concat dfs to create final df
    # drop 'Day' col in nonstudy_df to avoid dublicate col
    # ('Day' col is already present in st_df)
    out_df = pd.concat([st_df, nonstudy_df.drop("Day", axis=1)], axis=1)
    cur_day, EI_last, nonst_rep_data = handle_nonstudy_data(nonstudy_df)
    day_offs_count, day_offs_str = handle_day_offs(DAY_OFFS)
    # pack values before returning them
    st_rep_data += [day_offs_count, day_offs_str]
    report_data = st_rep_data, nonst_rep_data
    wide_use_data = [month, mean, std, min_to_study,
                     out_df, cur_day, EI_last]
    return report_data, wide_use_data
