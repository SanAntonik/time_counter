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
    wide_use_data, *report_data = calc_study_data(in_df[["Day", "DKind",
                                                         "Math", "CS",
                                                         "Eng"]],
                                                  DESIRED_MEAN_VALUE)
    # unpack wide_use_data
    st_df, mean, std, min_to_study = wide_use_data
    # combine st_df with nonstudy cols starting with 'Sport' col
    nonstudy_df = in_df.iloc[:, -6:]
    # get how many times you exercised that month and
    # two day offs vars
    sport = handle_nonstudy_data(nonstudy_df)
    day_offs_count, day_offs_str = handle_day_offs(DAY_OFFS)
    # add day offs vars and 'sport' var to report_data
    report_data += [day_offs_count, day_offs_str, sport]
    # concat dfs to create final df
    out_df = pd.concat([st_df, nonstudy_df], axis=1)
    # pack values before returning them
    wide_use_data = [month, mean, std, min_to_study, out_df]
    return report_data, wide_use_data
