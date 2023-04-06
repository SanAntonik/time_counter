def weekly_EI3plus_count(month, last_day, first_day, count):
    if first_day == -5:
        print(f"On {month} 1", end=", ")
    else:
        # Handle the case when new month hasn't accumulated 7+ days
        # Here you'll have a smaller than a week interval
        if first_day <= 0:
            first_day = 1
        print(f"From {month} {first_day} to {month} {last_day}", end=", ")
    print(f"your EIL3+ count equals {count}")
    if count < 2:
        print("You haven't exercised enough this week!")
    elif count == 2:
        print("Well, that's an okay result.", end=" ")
        print("However, try to at least exercise once more")
    elif 3 <= count <= 4:
        print("That's sufficient for this week.", end=" ")
        print("Keep up the good work!")
    elif count > 4:
        print("That's a little too much. Consider having a break!")
