"""def french_date_to_sql_date(french_date):  # retrieve an array or a list
    date_split = french_date.split('/')
    day = date_split[0]
    month = date_split[1]
    year = date_split[2]
    sql_date = year + "-" + month + "-" + day
    return sql_date"""


"""def sql_date_to_french_date(sql_date):
    date_split = sql_date.split('-')
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]
    french_date = day + "/" + month + "/" + year
    return french_date"""


def message_to_date(message):
    date_obtained = message.content
    date_split_added = date_obtained.split()
    date_split = date_split_added[1]
    date_split2 = date_split.split('/')
    return date_split2





