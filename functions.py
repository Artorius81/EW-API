import os
from io import BytesIO

import certifi
import cv2
import numpy as np
import requests
from PIL import Image
from flask import jsonify

from CONST import model


# функция для скачивания изображения по ссылке в "link"
def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


# конвертируем изображение в numpy массив нужной длины
def convert(path):
    test_path = []
    X_test = []

    for filename in os.listdir(r"C:/Users/Artorius/PycharmProjects/model/EW-API/images"):
        test_path.append("C:/Users/Artorius/PycharmProjects/model/EW-API/images/" + filename)
    for path in test_path:
        image = cv2.imread(path)
        image = cv2.resize(image, (100, 100))
        X_test.append(image)
    X_test = np.array(X_test)
    X_test = X_test.astype('float32')
    X_test /= 255
    return X_test


def predict(X_test):
    classes = model.predict(X_test)
    predicted_class = np.argmax(classes, axis=1)[0]
    if predicted_class == 0:
        result = {
            "output": 'Слишком чисто для свинарника'
        }
    else:
        result = {
            "output": 'Зачетный свинарник!'
        }
    return jsonify(result)


def download_images(url, directory='images'):
    response = requests.get(url, stream=True, verify=certifi.where())
    response.raise_for_status()

    ext = url.split('.')[-1]
    file_path = os.path.join(directory, f'image.{ext}')

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(8192):
            f.write(chunk)
    path = r"C:/Users/Artorius/PycharmProjects/model"
    return path + r"/EW-API/" + file_path
