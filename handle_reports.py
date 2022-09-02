def append_report(report, append_path):
    # check if report was added before. If yes, give an exception
    with open(append_path, "r", encoding="utf-8") as f:
        data = f.read()
        # get report month by splitting report to lines
        # then remove ':' at the end of the month string
        report_month = report.splitlines()[1][:-1]
        # This way it won't be possible to add reports
        # of the same month but with different numerical values
        if report_month in data:
            raise ValueError("You can't add the same monthly report twice")

    with open(append_path, "a", encoding="utf-8") as f:
        f.write(report)
        print("\nYour report was appended successfully\n")


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
