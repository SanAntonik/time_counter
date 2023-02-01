from preparation.prepare_data import prepare_data
from handle_reports import generate_report, append_report
from monitoring import cur_stats
from plotting import plot_data


def main(show_report=True, show_stats=True, plot=True, append=False):
    report_data, wide_use_data = prepare_data(PATH, DAY_OFFS,
                                              DESIRED_MEAN_VALUE)
    month, mean, std, min_to_study, df = wide_use_data
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


if __name__ == "__main__":
    # maybe put PATH vars into a separate file called 'constants'(not really sure about the name)
    # since you rarely change them?
    PATH = "C:/Users/San/Documents/inf/time monitoring/study data.txt"
    PATH = "C:/Users/San/Documents/inf/time monitoring/test_data.txt"
    APPEND_PATH = "C:/Users/San/Documents/inf/time monitoring/monthly reports/2023 - study reports.txt"
    PREVIOUS_DATA_FOLDER = "C:/Users/San/Documents/inf/time monitoring/monthly data/"
    DESIRED_MEAN_VALUE = 240
    # pass vacation day numbers
    DAY_OFFS = []
    main()
