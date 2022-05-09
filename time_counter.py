import matplotlib.pyplot as plt
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

        sum_subjects = math + cs + english
        total_study = round(sum_subjects / 60)
        mean = round(sum_subjects / month_last_day)
        std = round(np.sqrt(
            (sum([(day_total - mean)**2 for day_total in study_per_day]))/(month_last_day)))
        math_hs = round(math / 60)
        cs_hs = round(cs / 60)
        english_hs = round(english / 60)
        return [month, math_hs, cs_hs, english_hs, total_study, mean, std, sport, month_days, study_per_day]


def generate_report(month, math_hs, cs_hs, english_hs, total_study, mean, std, sport):
    return f"""
    {month}:
        Math: {math_hs} hours.
        CS: {cs_hs} hours.
        English: {english_hs} hours.
        Total study time: {total_study} hours.
        Arithmetic mean: {mean} minutes.
        Standart deviation: {std} minutes.
        Sport: {sport} times.\n"""


def append_report(report):
    # check if report was added before. If yes, give an exception
    with open(append_path, "r") as f:
        data = f.read()
        if report in data:
            raise ValueError("Report is already present. You can't add the same report twice")

    with open(append_path, "a") as f:
        f.write(report)


def day_stats():
    pass


def main(path, show_report=True, show_day_stats=True, plot=True, append_path=""):
    data = calculate(path)
    month, math_hs, cs_hs, english_hs, total_study, mean, std, sport, month_days, study_per_day = data
    report = generate_report(month, math_hs, cs_hs, english_hs, total_study, mean, std, sport)

    print(data)
    print(goal_mean)
    print(study_per_day[-1])
    current_day = study_per_day[-1]
    print(current_day)
    if current_day < goal_mean:
        print(f"You haven't studied enough today. Study {goal_mean - current_day} more min")
    else:
        print("Great job! You've studied enough today. Have some rest.")
    print(mean)
    print(month_days[-1] * goal_mean, sum(study_per_day))
    print(month_days[-1] * goal_mean - sum(study_per_day))
    print(goal_mean * 31 / 60, round(goal_mean * 31 / 60))
    if mean < goal_mean:
        print(mean, goal_mean)
    

    if show_report:
        print(report)
    if show_day_stats:
        day_stats()
    if append_path:
        append_report(report)
    if plot:
        plot_data(month_days, study_per_day, mean, std, month)


# plot mean, mean+-standart deviation
def mean_std(ax, mean, std):
    ax.axhline(y=mean-std, color='k', linestyle='-')
    ax.axhline(y=mean, color='r', linestyle='-', label="mean")
    ax.axhline(y=mean+std, color='k', linestyle='-', label="mean+-std")


def plot_data(month_days, study_per_day, mean, std, month):
    fig, ax = plt.subplots()
    fig.suptitle(month)
    ax.bar(month_days, study_per_day, color="purple")
    mean_std(ax, mean, std)
    ax.legend()
    plt.xticks(month_days)
    plt.show()


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

    path = "C:/Users/San/Documents/inf/time monitoring/monthly data/Apr 2022 data.txt"
    path = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    append_path = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2022 - study reports.txt"
    goal_mean = 252
    goal_hs = 130

    main(path)
