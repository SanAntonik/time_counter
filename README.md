# time_counter


GENERAL IDEA:
Time Counter is a program to help you keep track of what you do each day, so you have a better understanding of how and on what you spend your time

This app loads input from a specified file, makes calculations, prints result to the screen, and appends output to another file.


HOW TO RUN THIS PROJECT:
1) In constants.py, change PATH variable to where your input .txt file is placed. For the format of input file (study_data.txt or whatever you named it), have a look at INPUT section. Other constants in constants.py (APPEND_PATH and PREVIOUS_DATA_FOLDER) you can leave unchanged because they are only used if you run time_counter.py/main with the parameter 'append=True'. Inside time_counter.py, there are other two constants (DESIRED_MEAN_VALUE and DAY_OFFS). However, for the program to run, you don't need to change them.
2) Run 'time_counter.py/main' with the default parameters. That is with 'plot=True' and 'append=False'.
NOTE1: You can pass the following parameters to 'time_counter.py/main' function:
- plot - by default, set to True - show graph of how long you studied each day and whether that day was a working day or a day off
- append - by default, set to False - append your montly report and reset 'study_data.txt' (!). Usualy, this operation is done at the beginning of every new month. Be cautious when using this feature because you can lose your data


INPUT:
Input .txt file must be called 'study_data.txt' (also, check if PATH constants are correct!) and have the following format:
"""
  Month Year
  0:1_2_3:pa4-5_od6_le7_jg8_gm9 per row
"""
  where
    0 - Day of the month (from 1 to 31);
    1 - how many min you studied math;
    2 - how many min you studied computer science;
    3 - how many min you studied English;
    4 - if you exercised that day, update counter by +1 (pa);
    5 - difficulty of the performed exercise from 1 (easy) to 5 (hard). For more info, have a look at NOTE3;
    6 - how many min you spent outdoor (od);
    7 - how many min you read with your left eye (le);
    8 - how many min you juggled (jg);
    9 - how many min you played computer games (gm);

Part of May 2023 text file as an example:
    May 2023
    01:0_165_130:pa1-2_od65_le0_jg0_gm0
    02:0_251_18:pa2-3_od105_le0_jg0_gm245
    03:0_230_40:pa3-4_od35_le0_jg0_gm112
    ...
    30:0_250_10:pa22-4_od170_le10_jg15_gm0
    31:0_250_6:pa22-0_od90_le0_jg0_gm90

NOTE1: Colons ':' separate different blocks of daily input. The first block (0) just gives day number. The second block (1-3) contains study-related data. The third block (4-8) is about non-study data.
NOTE2: In the third, non-study, block, you can see two-letter-long abbreviations such as 'od' or 'pa' before the actual minutes. They were put there for easier differentiation between different columns in non-study block. To discover what each abbreviation means, have a look at NOTE4.
NOTE3: All possible Exercise Intensity (EI) levels:
- 0 - you didn't exercise
- 1 - easy
- 2 - between easy and moderate
- 3 - moderate
- 4 - between moderate and hard
- 5 - hard
NOTE4: Meaning of abbreviations in non-study block:
- pa - phycical activity
- od - outdoor
- le - left eye reading
- jg - juggling
- gm - gaming


OUTPUT:
Output can be separated into terminal output and plot output:
- terminal output - consists of
    - print of entire df
    - report part - here we can see hour count for math, CS, and English, their total (math+cs+eng), mean value with and without day offs, standart deviation, exercise total count and per exercise intensity (EI). After that, there are hour and day count for the four categories: outdoor, LE reading, juggling, and gaming
    - day-to-day feedback module
        - monthly stats - here can be seen montly desired mean value, montly current mean value, and how many more min you need to study to achieve montly desired mean value
        - daily stats - see here how many min you studied that particular day, your desired daily mean goal, and how many more min you need to study to achieve desired daily mean goal. After that, you can see how many days passed since you last had exercise of each intensity. Finaly, there is EI3+ count for the last seven days
- plot output - per each day of the month, see study total + current montly mean value +- standart deviation


ORDER OF CALLS (if using all the features)
time_counter.py/main()
    1) preparation/prepare_data.py/prepare_data()
        1.1) initial_preparation.py/prepare_initial_df()
            1.1.1) categorise()
        1.2) calc_study_data.py/calc_study_data()
            1.2.1) calc_req_study_time()
        1.3) nonstudy_data/handle_nonstudy_data.py/handle_nonstudy_data()
            1.3.1) get_EI_dicts.py/get_EI_dicts()
            1.3.2) get_EIL3plus_count.py/get_EIL3plus_count()
        1.4) handle_day_offs.py/handle_day_offs()
    2) report/generate.py/generate_report()
        2.1) generate_study_report()
        2.2) generate_nonstudy_report()
    3) feedback/give_feedback.py/give_feedback()
        3.1) check_month_mean.py/check_month_mean()
        3.2) check_day_mean.py/check_day_mean()
        3.3) give_EI_feedback.py/give_EI_feedback()
        3.4) weekly_EI3plus_count.py/weekly_EI3plus_count()
    4) report/append.py/append_report()
        4.1) month_year_alternating()
    5) plotting.py/plot_data()
        5.1) mean_std()


PROGRAM STRUCTURE:
- time_counter.py - the main file of the program. The script is supposed to run only from this file!
- constants.py - here lie rarely changed PATH variabless
- playground.ipynb - the jupyter notebook where it's more comfortable sometimes to test new features
- .gitignore - what files git should ignore
- README.md - documentation file
- plotting.py - file containing plotting-related funcs
- feedback package
    - give_feedback.py - the centerpiece of the package where the other four package files (check_day_mean, check_month_mean etc) are used
    - check_day_mean.py - tells you whether you studied enough or not TODAY
    - check_month_mean.py - tells you whether you studied enough or not THIS MONTH
    - give_EI_feedback.py - tells you how many days passed since you had exercise of a particular intensity per each exercise intensity
    - weekly_EI3plus_count.py - tells you how many times you had exercises of EI3+ (exercise intensity three or more) in the last seven days
- preparation package
    - prepare_data.py - the centerpiece of the package where the rest files and one package (nonstudy_data) are used
    - initial_preparation.py - first step in data preparation process
    - calc_study_data.py - here study-related data is handled
    - nonstudy_data package
        - handle_nonstudy_data.py - the centerpiece of this subpackage where the other two files (get_EI_dicts and get_EIL3plus_count) are used
        - get_EI_dicts.py - get two EI-related dicts that are gonna be used later
        - get_EIL3plus_count.py - get how many times you had EI3+ exercises in 7-day period. If it's the beginning of the month, the interval will be smaller
        - handle_day_offs.py - return your day offs count and the day numbers
- report package
    - append.py - here's realized 'append' parameter of main func in time_counter.py
    - generate.py - here are generated one main report from a study and nonstudy one


USED THIRD-PARTY LIBRARIES:
- matplotlib
- seaborn
- pandas
