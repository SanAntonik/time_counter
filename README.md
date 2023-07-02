# time_counter


GENERAL IDEA:
Time Counter is a program to help you keep track of what you do each day, so you have a better understanding of how and on what you spend your time

This app loads input from a specified file, makes calculations, prints result to the screen, and appends output to another file.


HOW TO RUN THIS PROJECT:
Before launching the program, we need to check if constants are correctly set up. Rarely changed constants such as file paths lie in constants.py while more frequently updated ones (DESIRED_MEAN_VALUE and DAY_OFFS) can be changed in time_counter.py. 

Also, main function can take the following parameters:
- plot - by default, set to True - show graph of how long you studied each day and whether that day was a working day or a day off
- append - by default, set to False - append your montly report and reset 'study_data.txt' (!). Usualy, this operation is done at the beginning of every new month. Be cautious when using this feature because you can lose your data

After making sure constants have proper values and with what parameters to run main func, we run 'time_counter.py' file. This file is the main file of the entire application and is the only file you're supposed to run.


INPUT:
Input .txt file must be called 'study_data.txt' (also, check if PATH constants are correct!) and have the following format:

"""
  Month Year
  0:1_2_3:pa4-5_od6_le7_jg8_gm9 per row

  where
  0 - Day of the month (from 1 to 31);
  1 - how many min you studied math;
  2 - how many min you studied computer science;
  3 - how many min you studied English;
  4 - if you exercised that day, update counter by +1 (pa);
  5 - difficulty of the performed exercise from 1 (easy) to 5 (hard). For more info, have a look at APPENDIX;
  6 - how many min you spent outdoor (od);
  7 - how many min you read with your left eye (le);
  8 - how many min you juggled (jg);
  9 - how many min you played computer games (gm);

  NOTE1: Colons ':' separate different blocks of daily input. The first block (0) just gives day number. The second block (1-3) contains study-related data. The third block (4-8) is about non-study data.
  NOTE2: In the third, non-study, block, you can see two-letter-long abbreviations such as 'od' or 'pa' before the actual minutes. They were put there for easier differentiation between different columns in non-study block. To discover what each abbreviation means, have a look at APPENDIX.

  Part of May 2023 text file as an example:
  May 2023
  01:0_165_130:pa1-2_od65_le0_jg0_gm0
  02:0_251_18:pa2-3_od105_le0_jg0_gm245
  03:0_230_40:pa3-4_od35_le0_jg0_gm112
  ...
  30:0_250_10:pa22-4_od170_le10_jg15_gm0
  31:0_250_6:pa22-0_od90_le0_jg0_gm90
"""


OUTPUT:
a bunch of basic statistics + plot


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


USED THIRD-PARTY LIBRARIES:
- matplotlib
- seaborn
- pandas


PROGRAM STRUCTURE:
time_counter.py - the main file of the program. The script is supposed to run only from this file!
playground.ipynb - the jupyter notebook where it's more comfortable to test new features
.gitignore
README.md - documentation file
plotting.py - file containing plotting-related funcs


APPENDIX:

All possible Exercise Intensity (EI) levels:
- 0 - you didn't exercise
- 1 - easy
- 2 - between easy and moderate
- 3 - moderate
- 4 - between moderate and hard
- 5 - hard

Meaning of abbreviations in non-study block:
- pa - phycical activity
- od - outdoor
- le - left eye reading
- jg - juggling
- gm - gaming
