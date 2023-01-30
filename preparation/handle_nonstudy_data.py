import numpy as np
import pandas as pd


# at least, get here how much you exercised during the month
# then think about how to handle other nonstudy data
def handle_nonstudy_data(df):
    """
    Summary:
        Here you do operations with nonstudy data
    Args:
        df: df containing non-study data
    Returns:
        list of data
    """
    # get last value from the 'Sport' col
    sport = df["Sport"].iloc[-1]
    return sport
