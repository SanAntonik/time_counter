import numpy as np
import pandas as pd


def calculate_data(df, day_offs):
    """
    Get last value from the 'Sport' col
    Get summed values from 'Math', 'CS', and 'Eng' cols
    Create col 'Total' where each row is the sum of 'Math', 'CS', and 'Eng'
    Get mean, std, and total_hs from 'Total' col of df
    Convert cols 'Total' and 'Day' to lists

    Args:
        df: pandas dataframe

    Returns:
        list of data
    """
    sport = df["Sport"].iloc[-1]
    total_per_subject = df[["Math", "CS", "Eng"]].sum(
        axis=0).div(60).round().astype(np.int64)
    math_hs, cs_hs, eng_hs = total_per_subject

    total_per_day = df[["Math", "CS", "Eng"]].sum(axis=1)
    df["Total"] = total_per_day
    total_hs = round(total_per_day.sum() / 60)

    # handle vacation days. Your mean and std must not
    # include data from vacation days
    if len(day_offs) > 0:
        last_recorded_day = df["Day"].iloc[-1]
        passed_day_offs = [day for day in day_offs if day <= last_recorded_day]
        df_removed_day_offs = df.loc[~df["Day"].isin(passed_day_offs)]
        total_per_day = df_removed_day_offs["Total"]
    mean = round(total_per_day.mean())
    std = round(total_per_day.std(ddof=0))

    study_per_day = df["Total"].tolist()
    month_days = df["Day"].tolist()
    return [math_hs, cs_hs, eng_hs, total_hs, sport, mean, std, month_days, study_per_day]
