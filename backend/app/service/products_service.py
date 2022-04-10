from app.manager import product_manager
import uuid
import os
from flask import current_app

MAPPING_PRODUCT_FIELDS = {"Name": "name", "OldPrice": "old_price", "Price": "price", "TypeId": "type_id",
                          "Vote": "vote", "Image": "image", "DealImage": "deal_image", "BigImage1": "big_image_1",
                          "BigImage2": "big_image_2", "SmallImage1": "small_image_1", "SmallImage2": "small_image_2",
                          "Description": "description", "NotChemical": "chemical", "Organic": "organic",
                          "FromFarm": "from_farm", "Deal": "deal", "FreeShip": "free_ship", "BestSell": "sell",
                          "Feature": "feature"}


def get_all_product():
    return product_manager.get_all_product()


def get_one_product(product_id):
    return product_manager.get_one_product(product_id)


def get_product_by_type(product_type, size):
    return product_manager.get_product_by_type(product_type, size)


def get_latest_product(size):
    return product_manager.get_latest_product(size)


def del_product_by_id(product_id):
    return product_manager.del_product_by_id(product_id)


def add_product(product):
    return product_manager.add_product(product)


def convert_product_to_model(product):
    result = [product[MAPPING_PRODUCT_FIELDS[field]] for field in product_manager.PRODUCT_FIELDS
              if MAPPING_PRODUCT_FIELDS[field] in product]
    return result


def save_image(images):
    result_path = []
    root_path = current_app.config['IMAGES_PATH']
    for image in images:
        new_unique_filename = uuid.uuid4().hex
        path = os.path.join(root_path, new_unique_filename)
        # image.save(new_unique_filename)
        image.save("app/static/" + path)
        result_path.append(path)

    return result_path


def convert_form_data_to_product(data):
    (data['image'], data['deal_image'], data['big_image_1'],
     data['big_image_2'], data['small_image_1'], data['small_image_2']) = save_image([data['image'],
                                                                                      data['deal_image'],
                                                                                      data['big_image_1'],
                                                                                      data['big_image_2'],
                                                                                      data['small_image_1'],
                                                                                      data['small_image_2']])
    for key in data:
        if type(data[key]) == bool:
            data[key] = 1 if data[key] else 0
    return convert_product_to_model(data)
