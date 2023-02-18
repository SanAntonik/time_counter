from preparation.prepare_data import prepare_data
from report.append import append_report
from report.generate import generate_report
from monitoring import cur_stats
from plotting import plot_data
from constants import PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER


def main(show_report=True, show_stats=True, plot=True, append=False):
    report_data, wide_use_data = prepare_data(PATH, DAY_OFFS,
                                              DESIRED_MEAN_VALUE)
    month, mean, std, min_to_study, df, EI_last = wide_use_data
    report = generate_report(month, report_data,
                             mean, std)

    print(month)
    print(df)
    if show_report:
        print(report)
    if show_stats:
        cur_stats(df, month, mean, min_to_study,
                  DESIRED_MEAN_VALUE, EI_last)
    if append:
        # BEWARE: your 'study data' gets overwritten
        # with a new template if you use append_report!!!
        append_report(report, PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER)
    if plot:
        plot_data(df, mean, std, month)


if __name__ == "__main__":
    DESIRED_MEAN_VALUE = 240
    # pass vacation day numbers
    DAY_OFFS = [2, 4, 12, 13]
    main()
