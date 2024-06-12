from .utils.check_month_mean import check_month_mean
from .utils.check_day_mean import check_day_mean
from .utils.give_EI_feedback import give_EI_feedback
from .utils.weekly_EI3plus_count import weekly_EI3plus_count


def give_feedback(feedback_data, month, mean, DESIRED_MEAN_VALUE):
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]
    EI_last, EI3plus_count, first_day = feedback_data[:3]
    min_to_study, last_day_total, last_day = feedback_data[3:]
    print()
    print("DAY-TO-DAY FEEDBACK MODULE STARTS...")
    check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study)
    # Maybe group check_day_mean, give_EI_feedback,
    # and weekly_EI3plus_count into a subpackage because
    # they are daily stats
    check_day_mean(
        month_alone, last_day, year_alone, last_day_total, DESIRED_MEAN_VALUE
    )
    give_EI_feedback(EI_last, last_day)
    weekly_EI3plus_count(month_alone, last_day, first_day, EI3plus_count)
