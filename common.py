def convert_to_dict(cursor, result_set):
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in result_set]