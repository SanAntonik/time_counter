## time_counter

Small program to help me keep track of how long I study. 

It loads input from a specified file, makes calculations, prints result to the screen, and appends output to another file.

Input file must be a text file with the following format:

```
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
```


Jun 29, 2023 Update:


GENERAL IDEA:
Time Counter is a program to help me keep track of what I do each day. 

It loads input from a specified file, makes calculations, prints result to the screen, and appends output to another file.


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
  NOTE2: In the third, non-study, block, you can see two-letter-long abbreviations such as 'od' or 'pa' before the actual minutes. They were put there for easier differentiation between different columns in non-study block. To discover what each abbreviation mean, have a look at APPENDIX.

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


PROGRAM FLOW:
The execution starts with setting up constants. Then we go to main func inside time_counter.py... 


PROGRAM STRUCTURE:
time_counter.py - the main file of the program. The script is supposed to run from this file!
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
