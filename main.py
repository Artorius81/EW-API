from flask import Flask, request
from functions import *
from CONST import *

app = Flask(__name__)


# метод для предсказания класса изображения
@app.route('/predict', methods=['POST'])
def main():
    url = []
    url.append(request.get_json()["link"])
    img_to_convert = download_images(url[0])
    images_final = convert(img_to_convert)
    return predict(images_final)


# метод для получения инфы по модели
@app.route('/get_info', methods=['POST'])
def get_info():
    msg = request.get_json()["message"]
    if msg == 'success':
        result = {
            "name": "clean_or_messy",
            "format": ".h5",
            "purpose": "Модель машинного обучения классифицирует по картинке грязная или убранная комната",
            "model_size": "199 MB",
            "accuracy": "80%"
        }
    else:
        result = {
            "message": "Что-то пошло не так"
        }
    return jsonify(result)


# метод для получения рандомной ссылке изображения
@app.route('/get_test_image', methods=['POST'])
def get_image():
    msg = request.get_json()["message"]
    if msg == 'success':
        result = {
            "url": download_images(urls)
        }
    else:
        result = {
            "message": "Что-то пошло не так"
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, port=8888)
