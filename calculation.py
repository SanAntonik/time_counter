import numpy as np
import pandas as pd


def calculate_data(df):
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
    mean = round(total_per_day.mean())
    std = round(total_per_day.std(ddof=0))
    total_hs = round(total_per_day.sum() / 60)

    study_per_day = df["Total"].tolist()
    month_days = df["Day"].tolist()

    return [math_hs, cs_hs, eng_hs, total_hs, sport, mean, std, month_days, study_per_day]
