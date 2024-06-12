# see whether you need to study additional min to
# reach your desired MONTHLY mean value
def check_month_mean(month, mean, DESIRED_MEAN_VALUE, min_to_study):
    print(
        f"""Your {month} desired mean value: {DESIRED_MEAN_VALUE} min
Your current mean value: {mean} min"""
    )
    if mean < DESIRED_MEAN_VALUE:
        print("You haven't studied enough this month.", end=" ")
        print(f"Study {min_to_study} more min")
    else:
        print("Congratulations! You've achieved your desired", end=" ")
        print("mean value for this month! Have some rest")
