from preparation import prepare_data
from calculation import calculate_data
from handle_reports import generate_report, append_report
from monitoring import cur_stats
from plotting import plot_data


def main(show_report=True, show_stats=True, plot=True, append_path=""):
    month, df = prepare_data(path, day_offs)
    *report_data, mean, std, min_to_study = calculate_data(df, desired_mean_value)
    report = generate_report(month, report_data, mean, std)

    print(month)
    print(df)

    if show_report:
        print(report)
    if show_stats:
        cur_stats(df, month, mean, min_to_study,
                  desired_mean_value)
    if append_path:
        append_report(report, append_path)
    if plot:
        plot_data(df, mean, std, month)


if __name__ == '__main__':
    path = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    append_path = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2022 - study reports.txt"
    desired_mean_value = 240
    # pass vacation day numbers
    day_offs = [2, 7, 16, 23, 30]

    # # data for tests and such
    # path = "C:/Users/San/Documents/inf/time monitoring/monthly data/September 2022.txt"
    # desired_mean_value = 180
    # day_offs = [3, 4, 11, 18]

    main()
