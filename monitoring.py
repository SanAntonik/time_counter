# see whether you studied enough today
def check_day_mean(month_alone, last_day_numb,
                   year_alone, day_total, DESIRED_MEAN_VALUE):
    print(f"""\nPer {month_alone} {last_day_numb}, {year_alone}
You studied: {day_total} min
You need to study: {DESIRED_MEAN_VALUE} min""")
    if day_total < DESIRED_MEAN_VALUE:
        print("You haven't studied enough today.", end=" ")
        print(f"Study {DESIRED_MEAN_VALUE - day_total} more min")
    else:
        print("Congratulations! You've studied enough today! Have some rest")


# MAYBE THIS FUNC NEEDS TO BE MORE CONNECTED TO THE MONTLY STATS
# THINK HOW TO REGROUP THIS STUFF
# see whether you need to study additional min to
# reach your desired montly mean value
def check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study):
    print(
        f"""Your {month} desired mean value: {DESIRED_MEAN_VALUE} min
Your current mean value: {mean} min""")
    if mean < DESIRED_MEAN_VALUE:
        print("You haven't studied enough this month.", end=" ")
        print(f"Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired", end=" ")
        print("mean value for this month! Have some rest")


# that's monitoring stuff - daily stats
def give_EI_feedback(EI_dir, current_day):
    print("Regarding Exercise Intensity...")
    for key, value in EI_dir.items():
        # for every EI, count how many days passed since
        # the last time you had exercise of that intensity
        difference = current_day - value
        print(f"    EI level '{key}': last exercised", end=" ")
        # handle negative values (no data for this particular
        # month), 0 (exercised today) etc
        if difference < 0:
            print("not this month")
        elif difference == 0:
            print("today")
        elif difference == 1:
            print("1 day ago")
        elif difference > 1:
            print(f"{difference} days ago")


def cur_stats(df, month, mean, min_to_study,
              DESIRED_MEAN_VALUE, EI_last):
    # how many min you studied
    # during last recorded day of the month
    day_total = df["Total"].iloc[-1]
    last_day_numb = df["Day"].iloc[-1]
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]

    check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study)
    check_day_mean(month_alone, last_day_numb,
                   year_alone, day_total, DESIRED_MEAN_VALUE)
    give_EI_feedback(EI_last, last_day_numb)
