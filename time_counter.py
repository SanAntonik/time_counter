from preparation.prepare_data import prepare_data
from report.append import append_report
from report.generate import generate_report
from feedback.give_feedback import give_feedback
from plotting import plot_data
from constants import PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER


def main(plot=True, append=False):
    rep_data, wide_use_data, feedback_data = prepare_data(PATH, DAY_OFFS,
                                                          DESIRED_MEAN_VALUE)
    month, mean, std, df = wide_use_data
    report = generate_report(month, rep_data,
                             mean, std)

    # print(df)
    print(report)
    give_feedback(feedback_data, month, mean, DESIRED_MEAN_VALUE)
    if append:
        # BEWARE: your 'study data' gets overwritten
        # with a new template if you use append_report!!!
        append_report(report, PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER)
    if plot:
        plot_data(df, mean, std, month)


if __name__ == "__main__":
    DESIRED_MEAN_VALUE = 270
    # pass vacation day numbers
    DAY_OFFS = []
    main(plot=False)
