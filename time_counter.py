from preparation import prepare_data
from calculation import calculate_data
from handle_reports import generate_report, append_report
from monitoring import cur_stats
from plotting import plot_data


def main(show_report=True, show_day_stats=True, plot=True, append_path=""):
    month, df = prepare_data(path)
    *report_data, mean, std, month_days, study_per_day = calculate_data(df, day_offs)
    report = generate_report(month, report_data, mean, std)

    print(month)
    print(df)

    if show_report:
        print(report)
    if show_day_stats:
        cur_stats(month, mean, month_days, study_per_day, desired_mean_value)
    if append_path:
        append_report(report, append_path)
    if plot:
        plot_data(month_days, study_per_day, mean, std, month)


if __name__ == '__main__':
    path = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    # path = "C:/Users/San/Documents/inf/time monitoring/monthly data/June 2022 data.txt"
    append_path = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2022 - study reports.txt"
    desired_mean_value = 180
    # pass vacation day numbers
    day_offs = [3, 4, 11, 18, 24, 25]
    # day_offs = []
    main()
