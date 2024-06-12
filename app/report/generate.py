# for reference: 'w/' stands for 'with'
# and 'w/o' stands for 'without'
def generate_study_report(report_data, mean, std):
    math_hs, cs_hs, english_hs = report_data[:3]
    total_study, mean_full_data = report_data[3:5]
    day_offs_count, day_offs_str = report_data[5:]
    return f"""    Math: {math_hs} hours
    CS: {cs_hs} hours
    English: {english_hs} hours
    Total time: {total_study} hours
    Mean w/ day offs: {mean} minutes
    Mean w/o day offs: {mean_full_data} minutes
    Day offs count: {day_offs_count} days
    Day offs: {day_offs_str}
    Standart deviation: {std} minutes"""


def generate_nonstudy_report(report_data):
    cols, ex_count, hs_total_per_col = report_data[:3]
    day_count_per_col, EI_count = report_data[3:]
    output = "    Exercise\n"
    output += "        Total:\n"
    output += f"            {ex_count}\n"
    output += "        EI count:\n"
    for key, value in EI_count.items():
        output += f"            {key}: {value}\n"
    for i in range(len(cols)):
        if cols[i] == "OD":
            output += "    Outdoor\n"
        elif cols[i] == "LE":
            output += "    LE reading\n"
        elif cols[i] == "RN":
            output += "    Running\n"
        elif cols[i] == "GM":
            output += "    Gaming\n"
        output += f"        Total hours: {hs_total_per_col[i]}\n"
        output += f"        Days count: {day_count_per_col[i]}\n"
    return output


def generate_report(month, report_data, mean, std):
    """
    Summary:
        Generate one big monthly report using
        generate study and nonstudy report
        funcs
    """
    st_rep_data, nonst_rep_data = report_data
    return f"""
{month}:
{generate_study_report(st_rep_data, mean, std)}
{generate_nonstudy_report(nonst_rep_data)}"""
