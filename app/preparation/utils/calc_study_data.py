def calc_study_data(df, DESIRED_MEAN_VALUE):
    """
    Summary:
        complete all the study data calculations
        in the program. Study data cols are:
        Day, DKind, Math, CS, and Eng
        (Day and DKind are used to identify
        workdays and day offs)
    Args:
        df: pandas dataframe with study data
        DESIRED_MEAN_VALUE (str, constant): how
        many min you want to study per work day
    Returns:
        list of data
    """
    # get summed values from 'Math', 'CS', and 'Eng' cols
    math_hs, cs_hs, eng_hs = (
        df[["Math", "CS", "Eng"]].sum(axis=0).div(60).round().astype(int)
    )
    # create col 'Total' where each row is the sum
    # of 'Math', 'CS', and 'Eng' cols
    df = df.assign(Total=df[["Math", "CS", "Eng"]].sum(axis=1))
    total_per_day = df["Total"]
    # with full data mean it's easier to compare the
    # change of your study time because number of
    # day offs per months differ from month to month
    mean_full_data = round(total_per_day.mean())
    # find how many hours you studied this month
    total_hs = round(total_per_day.sum() / 60)
    # handle vacation days. Your mean and std
    # must not include data from vacation days.
    if "relax" in df["DKind"].values:
        df_removed_day_offs = df[~df["DKind"].str.contains("relax")]
        total_per_day = df_removed_day_offs["Total"]
    mean = round(total_per_day.mean())
    std = round(total_per_day.std(ddof=0))
    min_to_study = calc_req_study_time(total_per_day, DESIRED_MEAN_VALUE)
    # pack several values
    wide_use_data = [df, mean, std, min_to_study]
    return [wide_use_data, math_hs, cs_hs, eng_hs, total_hs, mean_full_data]


# small func to calculate how many more min you need to
# study to achieve your desired monthly mean
def calc_req_study_time(total_per_day, DESIRED_MEAN_VALUE):
    req_min = DESIRED_MEAN_VALUE * len(total_per_day)
    studied_min = sum(total_per_day)
    return req_min - studied_min
