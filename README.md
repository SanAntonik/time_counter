# time_counter

Small program to help me keep track of how long I study. 
It loads input from a specified file, makes calculations, prints result to the screen, and appends output to another file.

Input file must be a text file with the following format:

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
