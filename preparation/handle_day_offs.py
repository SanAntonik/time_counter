def handle_day_offs(DAY_OFFS):
    # Create two day_offs vars for generate_report
    # func. With these two vars, reports will
    # provide a more detailed picture of the month
    day_offs_count = len(DAY_OFFS)
    if day_offs_count > 0:
        day_offs_str = ', '.join(map(str, DAY_OFFS))
    else:
        day_offs_str = "you studied every day"
    return day_offs_count, day_offs_str
