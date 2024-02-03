def handle_day_offs(df):
    """
    Summary:
        Calculate and handle days off in the DataFrame.
        Generates information about the count and specific
        days of relaxation.
    Args:
        df (DataFrame): Input DataFrame containing daily data.
            Must have a 'DKind' column indicating work or relax days.
    Returns:
        day_offs_count (int): Count of relaxation days.
        day_offs_str (str): String containing the specific days of
            relaxation, or a message indicating studying every day.
    """
    # Find the days on which you relaxed
    day_offs = df[df["DKind"] == "relax"]["Day"].to_list()
    # Create two variables for the generate_report function
    # These variables will provide a more detailed picture of the month
    day_offs_count = len(day_offs)
    if day_offs_count > 0:
        day_offs_str = ", ".join(map(str, day_offs))
    else:
        day_offs_str = "you studied every day"
    return day_offs_count, day_offs_str
