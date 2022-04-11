from app.repos.mssql import get_cnn
from app.repos import exec_query, exec_delete, exec_insert_one


def get_all_category():
    cnn = None
    ok = True
    result = None
    try:
        cnn = get_cnn()
        sql = 'select * from Category'
        result = exec_query(cnn, sql)
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        result = inst
    return ok, result
