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
        return [month, math_hs, cs_hs, english_hs, total_study, sport, mean, std, month_days, study_per_day]


def generate_report(month, report_data, mean, std):
    math_hs, cs_hs, english_hs, total_study, sport = report_data
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


def day_stats(month, mean, study_per_day, month_days):
    day_total = study_per_day[-1] # how many min you studied last day of data
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]
    last_day_numb = month_days[-1]
    # see whether you studied enough today
    print(f"\nOn {month_alone} {last_day_numb}, {year_alone}\nYou studied: {day_total} min\nYou need to study: {desired_mean_value} min")
    if day_total < desired_mean_value:
        print(f"You haven't studied enough today. Study {desired_mean_value - day_total} more min")
    else:
        print("Congratulations! You've studied enough! Have some rest")

    print(f"\nYour {month} desired mean value: {desired_mean_value} min\nYour current mean value: {mean} min")
    # see whether you need to study additionaly to reach your goal mean
    if mean < desired_mean_value:
        # find out how many min you need to study to reach your desired mean
        min_to_study = last_day_numb * desired_mean_value - sum(study_per_day)
        print(f"You haven't studied enough this month. Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired mean value for this month! Have some rest")


def main(show_report=True, show_day_stats=True, plot=True, append_path=""):
    data = calculate(path)
    month, *report_data, mean, std, month_days, study_per_day = data
    report = generate_report(month, report_data, mean, std)

    if show_report:
        print(report)
    if show_day_stats:
        day_stats(month, mean, study_per_day, month_days)
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
    desired_mean_value = 252
    main(plot=False)
