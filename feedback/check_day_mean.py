# see whether you studied enough TODAY
def check_day_mean(month_alone, last_day, year_alone, day_total, DESIRED_MEAN_VALUE):
    print(
        f"""\nToday ({month_alone} {last_day}, {year_alone})
You studied: {day_total} min
You need to study: {DESIRED_MEAN_VALUE} min"""
    )
    if day_total < DESIRED_MEAN_VALUE:
        print("You haven't studied enough today.", end=" ")
        print(f"Study {DESIRED_MEAN_VALUE - day_total} more min")
    else:
        print("Congratulations! You've studied enough today! Have some rest")
