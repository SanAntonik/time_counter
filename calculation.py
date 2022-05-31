import numpy as np
import pandas as pd


def calculate_data(df):
    """
    Get last value from the 'Sport' col
    Get summed values from 'Math', 'CS', and 'Eng' cols
    Create col 'Total' where each row is the sum of 'Math', 'CS', and 'Eng'
    Get mean, std, and total_hs from 'Total' col of df

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

    return [math_hs, cs_hs, eng_hs, total_hs, sport, mean, std]
    return [month, math_hs, cs_hs, english_hs, total_study, sport, mean, std, month_days, study_per_day]


# old, non-pandas version of calculate_function
# def calculate(path):
#     with open(path, "r", encoding="utf-8") as f:
#         data = f.read()
#         lines = data.splitlines()
#         month = lines[0]

#         math = 0
#         cs = 0
#         english = 0
#         study_per_day = []
#         for line in lines[1::]:
#             content = line.split(":")
#             if lines[-1] == line:
#                 sport = int(content[2])
#                 month_last_day = int(content[0])

#             study = content[1].split("_")
#             math += int(study[0])
#             cs += int(study[1])
#             english += int(study[2])

#             # calculations for plotting
#             study_per_day.append(int(study[0]) + int(study[1]) + int(study[2]))
#         month_days = [x for x in range(1, month_last_day+1)]
#         sum_subjects = math + cs + english
#         total_study = round(sum_subjects / 60)
#         mean = round(sum_subjects / month_last_day)
#         std = round(np.sqrt(
#             (sum([(day_total - mean)**2 for day_total in study_per_day]))/(month_last_day)))
#         math_hs = round(math / 60)
#         cs_hs = round(cs / 60)
#         english_hs = round(english / 60)
#         return [month, math_hs, cs_hs, english_hs, total_study, sport, mean, std, month_days, study_per_day]
