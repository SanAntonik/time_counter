import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from preparation import prepare_data
from calculation import calculate_data
from handle_reports import generate_report, append_report
from monitoring import day_stats


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
    month, df = prepare_data(path)
    *report_data, mean, std = calculate_data(df)
    report = generate_report(month, report_data, mean, std)

    print(month)
    print(df)

    if show_report:
        print(report)
    if show_day_stats:
        day_stats(month, mean, df, desired_mean_value)
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
