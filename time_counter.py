def time_counter(PATH):
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

            study = content[1].split("_")
            math += int(study[0])
            computer_science += int(study[1])
            english += int(study[2])

        return [month, math//60, computer_science//60, english//60, sport]


def handler(info, show=True, append_PATH=""):
    month, math, computer_science, english, sport = info
    result = f"""
    {month}:
        Math: {math} hours.
        CS: {computer_science} hours.
        English: {english} hours.
        Total study time: {math + computer_science + english} hours.
        Sport: {sport} times.\n"""

    if show:
        print(result)
    if append_PATH:
        with open(append_PATH, "a") as f:
            f.write(result)


if __name__ == '__main__':
    PATH = "C:/Users/San/Documents/inf/time monitoring/studying time.txt"
    append_PATH = "C:/Users/San/Documents/inf/time monitoring/2022 studies time monitoring.txt"
    handler(time_counter(PATH))
