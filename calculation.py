import numpy as np
import pandas as pd


def calculate_data(df, DESIRED_MEAN_VALUE):
    """
    Summary:
        complete all the required calculations in the program

    Args:
        df: pandas dataframe

    Returns:
        list of data
    """
    # get last value from the 'Sport' col
    sport = df["Sport"].iloc[-1]
    # get summed values from 'Math', 'CS', and 'Eng' cols
    total_per_subject = df[["Math", "CS", "Eng"]].sum(
        axis=0).div(60).round().astype(np.int64)
    math_hs, cs_hs, eng_hs = total_per_subject

    # create col 'Total' where each row is the sum
    # of 'Math', 'CS', and 'Eng' cols
    total_per_day = df[["Math", "CS", "Eng"]].sum(axis=1)
    df["Total"] = total_per_day
    # find how many hours you studied this month
    total_hs = round(total_per_day.sum() / 60)

    # handle vacation days. Your mean and std
    # must not include data from vacation days
    if "relax" in df["Kind"].values:
        df_removed_day_offs = df[~df["Kind"].str.contains("relax")]
        total_per_day = df_removed_day_offs["Total"]
    mean = round(total_per_day.mean())
    std = round(total_per_day.std(ddof=0))
    min_to_study = calc_req_study_time(total_per_day, DESIRED_MEAN_VALUE)
    return [math_hs, cs_hs, eng_hs, total_hs, sport,
            mean, std, min_to_study]


# small func to calculate how many more min you need to
# study to achieve your desired monthly mean
def calc_req_study_time(total_per_day, DESIRED_MEAN_VALUE):
    req_min = DESIRED_MEAN_VALUE * len(total_per_day)
    studied_min = sum(total_per_day)
    return req_min - studied_min
