from preparation import prepare_data
from calculation import calculate_data
from handle_reports import generate_report, append_report
from monitoring import cur_stats
from plotting import plot_data


def main(show_report=True, show_stats=True, plot=True, append=False):
    month, df = prepare_data(PATH, DAY_OFFS)
    *report_data, mean, std, min_to_study = calculate_data(df, DESIRED_MEAN_VALUE)
    report = generate_report(month, report_data, mean, std)

    print(month)
    print(df)

    if show_report:
        print(report)
    if show_stats:
        cur_stats(df, month, mean, min_to_study,
                  DESIRED_MEAN_VALUE)
    if append:
        # BEWARE: your 'study data' gets overwritten
        # with a new template if you use append_report!!!
        append_report(report, PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER)
    if plot:
        plot_data(df, mean, std, month)


if __name__ == '__main__':
    # path, append_path, previous_data_folder,
    # desired_mean_value, and day_offs are all constants
    # I should handle them better somehow
    PATH = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    APPEND_PATH = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2022 - study reports.txt"
    PREVIOUS_DATA_FOLDER = "C:/Users/San/Documents/inf/time monitoring/monthly data/"
    DESIRED_MEAN_VALUE = 240
    # pass vacation day numbers
    DAY_OFFS = [2, 7, 16, 23, 30]

    # # data for tests and such
    # PATH = "C:/Users/San/Documents/inf/time monitoring/monthly data/September 2022.txt"
    # DESIRED_MEAN_VALUE = 180
    # DAY_OFFS = [3, 4, 11, 18]

    main()
