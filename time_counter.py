import matplotlib as plt
import numpy as np


def calculate(path):
    with open(path, "r") as f:
        data = f.read()
        lines = data.splitlines()
        month = lines[0]

        math = 0
        cs = 0
        english = 0
        study_per_day = []
        for line in lines[1::]:
            content = line.split(":")
            if lines[-1] == line:
                sport = int(content[2])
                month_last_day = int(content[0])

            study = content[1].split("_")
            math += int(study[0])
            cs += int(study[1])
            english += int(study[2])

            # calculations for plotting
            study_per_day.append(int(study[0]) + int(study[1]) + int(study[2]))
        month_days = [x for x in range(1, month_last_day+1)]
        plot_data = (month_days, study_per_day)
        print(month_days)
        print(study_per_day)
        print(plot_data)

        print(sum(study_per_day), (sum(study_per_day)//60), round((sum(study_per_day)/60)), sum(study_per_day)/60)
        sum_subjects = math + cs + english
        print(sum_subjects)
        total_study = sum_subjects // 60
        print(total_study, sum_subjects / 60)
        total_study = round(sum_subjects / 60)
        print(total_study)

        mean = round(sum_subjects / month_last_day)
        std = round(np.sqrt(
            (sum([(day_total - mean)**2 for day_total in study_per_day]))/(month_last_day)))
        print("standart deviation", std)
        math_hs = round(math / 60)
        cs_hs = round(cs / 60)
        english_hs = round(english / 60)
        print(math_hs, cs_hs, english_hs)


        return [month, math_hs, cs_hs, english_hs, total_study, mean, std, sport, plot_data]


def main(path, show=True, plot=True, append_path=""):
    month, math_hs, cs_hs, english_hs, total_study, mean, std, sport, plot_data = calculate(path)
    result = f"""
    {month}:
        Math: {math_hs} hours.
        CS: {cs_hs} hours.
        English: {english_hs} hours.
        Total study time: {total_study} hours.
        Arithmetic mean: {mean} minutes.
        Standart deviation: {std} minutes.
        Sport: {sport} times.\n"""

    if show:
        print(result)
    if append_path:
        with open(append_path, "a") as f:
            f.write(result)
    if plot:
        pass


if __name__ == '__main__':
    """
    This program takes text file input where data is organized in the following format:

        Month Year
        0:1_2_3:4 per row

        where
        0 - Day of the month (from 1 to 31); 
        1 - how many min you studied math;
        2 - how many min you studied computer science;
        3 - how many min you studied English;
        4 - if you exercised that day, update counter by +1;

        Part of March 2022 file as an example:
        March 2022
        01:125_80_10:0
        02:0_0_10:0
        03:2_133_60:1
        ...
        30:150_50_75:13
        31:115_41_80:13
    """
    # path = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    path = "C:/Users/San/Documents/inf/time monitoring/studying time.txt"
    append_path = "C:/Users/San/Documents/inf/time monitoring/2022 - studies time monitoring.txt"
    main(path)
