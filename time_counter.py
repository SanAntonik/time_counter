def calculate(PATH):
    with open(PATH, "r") as f:
        data = f.read()
        lines = data.splitlines()
        month = lines[0]

        math = 0
        computer_science = 0
        english = 0
        for line in lines[1::]:
            content = line.split(":")
            if lines[-1] == line:
                sport = int(content[2])
                month_last_day = int(content[0])

            study = content[1].split("_")
            math += int(study[0])
            computer_science += int(study[1])
            english += int(study[2])
        total_study_time = (math + computer_science + english) // 60
        mean = total_study_time / month_last_day

        return [month, math//60, computer_science//60, english//60, total_study_time, mean, sport]


def main(show=True, plot=True, append_PATH=""):
    month, math, computer_science, english, total_study_time, mean, sport = calculate(PATH)
    result = f"""
    {month}:
        Math: {math} hours.
        CS: {computer_science} hours.
        English: {english} hours.
        Total study time: {total_study_time} hours.
        Arithmetic mean: {mean} hours.
        Sport: {sport} times.\n"""

    if show:
        print(result)
    if append_PATH:
        with open(append_PATH, "a") as f:
            f.write(result)
    if plot:
        pass


if __name__ == '__main__':
    """
    This program takes text file input where data is organized in the following format:

        Month Year
        0:1_2_3:4 per row

        where
        0 - Day of the month (from 1 to 31); 
        1 - how many min you studied math;
        2 - how many min you studied computer science;
        3 - how many min you studied English;
        4 - if you exercised that day, update counter by +1;

        Part of March 2022 file as an example:
        March 2022
        01:125_80_10:0
        02:0_0_10:0
        03:2_133_60:1
        ...
        30:150_50_75:13
        31:115_41_80:13
    """
    # PATH = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    PATH = "C:/Users/San/Documents/inf/time monitoring/studying time.txt"
    append_PATH = "C:/Users/San/Documents/inf/time monitoring/2022 - studies time monitoring.txt"
    main(PATH)
