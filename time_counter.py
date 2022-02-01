input = "01:0_240_35:0\n\
02:0_65_15:0\n\
03:20_180_10:1\n\
04:120_0_10:2\n\
05:120_60_60:3\n\
06:0_0_20:3\n\
07:140_60_40:4\n\
08:120_0_100:4\n\
09:0_0_10:4\n\
10:0_0_15:4\n\
11:91_30_40:5\n\
12:0_0_6:5\n\
13:20_70_10:6\n\
14:100_20_22:7\n\
15:0_0_75:8\n\
16:95_80_31:9\n\
17:80_270_10:9\n\
18:0_130_11:10\n\
19:0_270_10:10\n\
20:100_180_21:10\n\
21:0_170_10:10\n\
22:30_75_34:11\n\
23:90_140_25:11\n\
24:28_130_12:12\n\
25:33_60_10:12\n\
26:0_150_10:13\n\
27:0_0_26:13\n\
28:50_60_90:13\n\
29:0_110_120:14\n\
30:0_70_110:14\n\
31:80_160_135:15"


def time_counter(input):
    input_splitted = input.splitlines()
    math = 0
    computer_science = 0
    english = 0
    for line in input_splitted:
        line_seperated_by_colon = line.split(":")
        spent_time_on_study = line_seperated_by_colon[1].split("_")
        math += int(spent_time_on_study[0])
        computer_science += int(spent_time_on_study[1])
        english += int(spent_time_on_study[2])
        if input_splitted[-1] == line:
            sport = int(line_seperated_by_colon[2])
    return f"""
            Math: {math//60} hours.\n\
            CS: {computer_science//60} hours.\n\
            English: {english//60} hours.\n\
            Total study time: {math//60 + computer_science//60 + english//60} hours.\n\
            Sport: {sport} times.
            """


print(time_counter(input))