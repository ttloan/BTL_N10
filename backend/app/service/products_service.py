import pandas as pd

from app.repos.mssql import get_cnn
from app.repos import exec_query, exec_delete, exec_insert_one


PRODUCT_COLUMNS = ["Name", "OldPrice", "Price", "TypeId", "Vote", "Image", "DealImage",
                   "BigImage1", "BigImage2", "SmallImage1", "SmallImage2", "Description",
                   "NotChemical", "Organic", "FromFarm",  "Deal", "FreeShip", "BestSell", "Feature"]


def get_all_product():
    cnn = None
    ok = True
    result = None
    try:
        cnn = get_cnn()
        sql = 'select * from Product'
        result = exec_query(cnn, sql)
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        result = inst
    return ok, result


def get_one_product(product_id):
    cnn = None
    ok = True
    result = None
    try:
        cnn = get_cnn()
        sql = '''select * from Product where Id = ?'''
        result = exec_query(cnn, sql, [product_id])
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        result = inst
    return ok, result


def get_product_by_type(product_type):
    cnn = None
    ok = True
    result = None
    try:
        cnn = get_cnn()
        sql = '''select * from Product where TypeId = ?'''
        result = exec_query(cnn, sql, [product_type])
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        result = inst
    return ok, result


def del_product_by_id(product_id):
    cnn = None
    ok = True
    error = None
    try:
        cnn = get_cnn()
        sql = '''delete from Product where Id = ?'''
        ok = exec_delete(cnn, sql, [product_id])
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        error = inst
    return ok, error


def add_product(product):
    cnn = None
    ok = True
    error = None
    try:
        cnn = get_cnn()
        sql = '''insert into Product ([Name], OldPrice, Price, TypeId, Vote, [Image], DealImage, 
        BigImage1, BigImage2, SmallImage1, SmallImage2, [Description], NotChemical, Organic, FromFarm, 
        Deal, FreeShip, BestSell, Feature) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        ok = exec_insert_one(cnn, sql, product)
    except Exception as inst:
        if cnn:
            cnn.close()
        ok = False
        error = inst
    return ok, error


def convert_product_to_list(product):
    result = [product[key] for key in PRODUCT_COLUMNS if key in product]
    return result


