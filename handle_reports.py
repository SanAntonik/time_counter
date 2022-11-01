import shutil


# ATTENTION: you can lose your data if you
# use this function several times in a row
# because you overwrite your data in Step 4!!!
def append_report(report, SOURCE_PATH, APPEND_PATH, PREVIOUS_DATA_FOLDER):
    print("\n\nStarted report appending sequence...")
    # Step 1: check if report was added before
    # If yes, give an exception
    report_month = ""
    with open(APPEND_PATH, "r", encoding="utf-8") as f:
        data = f.read()
        # get report month by splitting report to lines
        # remove ':' at the end of the month string
        # finaly, remove whitespaces before the month
        report_month = report.splitlines()[1][:-1].strip()
        # This way it won't be possible to add reports
        # of the same month but with different numerical values
        if report_month in data:
            raise ValueError("You can't add the same monthly report twice")
    # Step 2: APPEND report to other reports in your file of reports
    with open(APPEND_PATH, "a", encoding="utf-8") as f:
        f.write(report)
        print("Your report was appended successfully")
    # Step 3: copy 'study data.txt' to folder with
    # data from previous months. Take the name for
    # freshly copied file from the first row
    destination = f"{PREVIOUS_DATA_FOLDER}{report_month}.txt"
    shutil.copy(SOURCE_PATH, destination)
    print("Data is copied")
    # Step 4: prepare a templete for the next month
    # by overwritting your old data with a fresh template
    with open(SOURCE_PATH, "w", encoding="utf-8") as f:
        next_month_year = month_year_alternating(report_month)
        empty_first_day = "01:0_0_0:0"
        template_text = f"{next_month_year}\n{empty_first_day}"
        f.write(template_text)
    print("Template is written over your old data")
    print("Your 'study data' file is ready for the use again")
    print("Sequence is completed")


# Return next month and year given cur month and year
# Used in creating new 'study data' file
def month_year_alternating(month_year):
    str_months = ["January", "February",
                  "March", "April", "May",
                  "June", "July", "August",
                  "September", "October", "November",
                  "December"]
    month_year_list = month_year.split()
    cur_month = month_year_list[0]
    year = int(month_year_list[1])
    cur_month_index = str_months.index(cur_month)
    next_month_index = cur_month_index + 1
    # handle if cur month is December
    if next_month_index > 11:
        next_month_index = 0
        year += 1
    next_month = str_months[next_month_index]
    return f"{next_month} {year}"


def generate_report(month, report_data, mean, std):
    math_hs, cs_hs, english_hs, total_study, sport = report_data
    return f"""
    {month}:
        Math: {math_hs} hours.
        CS: {cs_hs} hours.
        English: {english_hs} hours.
        Total study time: {total_study} hours.
        Arithmetic mean: {mean} minutes.
        Standart deviation: {std} minutes.
        Sport: {sport} times.\n"""
