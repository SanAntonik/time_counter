import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from preparation import prepare_data
from calculation import calculate_data
from handle_reports import generate_report, append_report


def day_stats(month, mean, study_per_day, month_days):
    day_total = study_per_day[-1]  # how many min you studied last day of data
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]
    last_day_numb = month_days[-1]
    # see whether you studied enough today
    print(f"\nOn {month_alone} {last_day_numb}, {year_alone}\nYou studied: {day_total} min\nYou need to study: {desired_mean_value} min")
    if day_total < desired_mean_value:
        print(
            f"You haven't studied enough today. Study {desired_mean_value - day_total} more min")
    else:
        print("Congratulations! You've studied enough today! Have some rest")

    print(
        f"\nYour {month} desired mean value: {desired_mean_value} min\nYour current mean value: {mean} min")
    # see whether you need to study additionaly to reach your goal mean
    if mean < desired_mean_value:
        # find out how many min you need to study to reach your desired mean
        min_to_study = last_day_numb * desired_mean_value - sum(study_per_day)
        print(
            f"You haven't studied enough this month. Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired mean value for this month! Have some rest")


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


def plot_df():
    pass


def main(show_report=True, show_day_stats=True, plot=True, append_path=""):
    # data = calculate(path)
    # month, *report_data, mean, std, month_days, study_per_day = data
    # report = generate_report(month, report_data, mean, std)

    month, df = prepare_data(path)
    *report_data, mean, std = calculate_data(df)
    report = generate_report(month, report_data, mean, std)

    print(month)
    print(df)

    if show_report:
        print(report)
    # if show_day_stats:
    #     day_stats(month, mean, study_per_day, month_days)
    if append_path:
        append_report(report, append_path)
    # if plot:
    #     plot_data(month_days, study_per_day, mean, std, month)


if __name__ == '__main__':
    # path = "C:/Users/San/Documents/inf/time monitoring/monthly data/Apr 2022 data.txt"
    path = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    append_path = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2022 - study reports.txt"
    desired_mean_value = 280
    main()
