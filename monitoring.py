def cur_stats(df, month, mean, min_to_study,
              DESIRED_MEAN_VALUE):
    # how many min you studied
    # during last recorded day of the month
    day_total = df["Total"].iloc[-1]
    last_day_numb = df["Day"].iloc[-1]
    month_year_list = month.split()
    month_alone = month_year_list[0]
    year_alone = month_year_list[1]

    check_day_mean(month_alone, last_day_numb,
                   year_alone, day_total, DESIRED_MEAN_VALUE)
    check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study)


# see whether you studied enough today
def check_day_mean(month_alone, last_day_numb,
                   year_alone, day_total, DESIRED_MEAN_VALUE):
    print(f"""\nOn {month_alone} {last_day_numb}, {year_alone}
You studied: {day_total} min
You need to study: {DESIRED_MEAN_VALUE} min""")
    if day_total < DESIRED_MEAN_VALUE:
        print("You haven't studied enough today.", end=" ")
        print(f"Study {DESIRED_MEAN_VALUE - day_total} more min")
    else:
        print("Congratulations! You've studied enough today! Have some rest")


# see whether you need to study additional min to
# reach your desired montly mean value
def check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study):
    print(
        f"""\nYour {month} desired mean value: {DESIRED_MEAN_VALUE} min
Your current mean value: {mean} min""")
    if mean < DESIRED_MEAN_VALUE:
        print("You haven't studied enough this month.", end=" ")
        print(f"Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired", end=" ")
        print("mean value for this month! Have some rest")
