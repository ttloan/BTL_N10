import pandas as pd


def exec_query(cnn, sql, params=[]):
    if (cnn is None) or (not sql):
        return pd.DataFrame()
    data = pd.read_sql(sql=sql, con=cnn, params=params)
    cnn.close()
    return data


def exec_no_query(cnn, sql, params=[]):
    if (cnn is None) or (not sql):
        return False
    cursor = cnn.cursor()
    cursor.fast_executemany = True
    cursor.executemany(sql, params)
    return True


def exec_insert_one(cnn, sql, params=[]):
    if (cnn is None) or (not sql) or (len(params) == 0):
        return False
    cursor = cnn.cursor()
    cursor.fast_executemany = True
    cursor.execute(sql, params)
    cnn.commit()
    cnn.close()
    return True


def exec_insert_many(cnn, table, df: pd.DataFrame):
    if (cnn is None) or (not table) or df.empty:
        return False
    # cursor = cnn.cursor()
    # cursor.fast_executemany = True
    # cursor.executemany(sql, df.to_dict('records'))
    df.to_sql('table', cnn)
    cnn.commit()
    cnn.close()
    return True


def exec_delete(cnn, sql, params=[]):
    if (cnn is None) or (not sql):
        return False
    cursor = cnn.cursor()
    cursor.execute(sql, params)
    cnn.commit()
    cnn.close()
    return True
