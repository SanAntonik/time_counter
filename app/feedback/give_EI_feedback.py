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
