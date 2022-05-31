def append_report(report, append_path):
    # check if report was added before. If yes, give an exception
    with open(append_path, "r", encoding="utf-8") as f:
        data = f.read()
        if report in data:
            raise ValueError(
                "Report is already present. You can't add the same report twice")

    with open(append_path, "a", encoding="utf-8") as f:
        f.write(report)
        print("Appended successfully")


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
