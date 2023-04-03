from .check_month_mean import check_month_mean
from .check_day_mean import check_day_mean
from .give_EI_feedback import give_EI_feedback
from preparation.nonstudy_data.get_EIL3plus_count import get_EIL3plus_count


def give_feedback(df, month, mean, min_to_study,
                  DESIRED_MEAN_VALUE, EI_last):
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]
    # how many min you studied
    # during last recorded day of the month
    day_total = df["Total"].iloc[-1]
    last_day = df["Day"].iloc[-1]
    first_day = 1
    print()
    print("DAY-TO-DAY FEEDBACK MODULE STARTS...")
    print(get_EIL3plus_count(df[["Day", "EI"]], first_day))
    check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study)
    check_day_mean(month_alone, last_day,
                   year_alone, day_total, DESIRED_MEAN_VALUE)
    give_EI_feedback(EI_last, last_day)
