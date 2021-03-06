def cur_stats(month, mean, month_days, study_per_day, desired_mean_value):
    day_total = study_per_day[-1]  # how many min you studied last day of data
    last_day_numb = month_days[-1]
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]

    check_day_mean(month, month_alone, last_day_numb,
                   year_alone, day_total, desired_mean_value, mean)
    check_month_mean(mean, desired_mean_value, last_day_numb, study_per_day)


# see whether you studied enough today
def check_day_mean(month, month_alone, last_day_numb, year_alone, day_total, desired_mean_value, mean):
    print(f"""\nOn {month_alone} {last_day_numb}, {year_alone}
You studied: {day_total} min
You need to study: {desired_mean_value} min""")
    if day_total < desired_mean_value:
        print(
            f"You haven't studied enough today. Study {desired_mean_value - day_total} more min")
    else:
        print("Congratulations! You've studied enough today! Have some rest")

    print(
        f"\nYour {month} desired mean value: {desired_mean_value} min\nYour current mean value: {mean} min")


# see whether you need to study additionaly to reach your goal mean
def check_month_mean(mean, desired_mean_value, last_day_numb, study_per_day):
    if mean < desired_mean_value:
        # find out how many min you need to study to reach your desired mean
        min_to_study = last_day_numb * desired_mean_value - sum(study_per_day)
        print(
            f"You haven't studied enough this month. Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired mean value for this month! Have some rest")
