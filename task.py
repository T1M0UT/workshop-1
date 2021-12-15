import datetime

def today_goal(lst):
    """
    returns a list of tasks for today
    """
    result = []
    lengths = []
    for i in lst:
        if i[0][:10] == datetime.datetime.today().strftime('%d.%m.%Y'):
            lengths.append(len(i[0]))
            result.append(" ".join(i[:-2]))
    return "\n".join(result)

