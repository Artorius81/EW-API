import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model(r'C:\Users\Artorius\PycharmProjects\model\EW-API\model\clean_or_messy.h5')

# списко ссылок на тестовые изображения (грязные и чистые комнатыы
urls = ["https://eakcon.com/images/service/cleanrooms.jpg",
        "https://sc01.alicdn.com/kf/H23515f01345f462e986d056d6f09aad9R.jpg",
        "https://www.cleanroom-industries.com/media/tz_portfolio/article/cache/design-and-construction-cleanroom-standards-414_L.jpg",
        "https://static.wixstatic.com/media/ead031_9462c3edbb6044039ef98e7fc2f838e3~mv2_d_3888_2592_s_4_2.jpeg/v1/fill/w_2500,h_1666,al_c/ead031_9462c3edbb6044039ef98e7fc2f838e3~mv2_d_3888_2592_s_4_2.jpeg",
        "https://100light.ru/upload/iblock/6a2/tax8vbhh5u5vl71e9g19oshq2ia3z7wo.jpg",
        "https://poloandtweed.com/wp-content/uploads/2019/10/Messy-Room-e1611765506181.jpg",
        "https://media.musely.com/u/62ecc59d-a96c-4530-a692-0e4c06320e92.jpg",
        "https://mykaleidoscope.ru/uploads/posts/2021-10/1634004250_12-mykaleidoscope-ru-p-tvorcheskii-besporyadok-v-komnate-interer-12.jpg",
        "https://na-dache.pro/uploads/posts/2022-01/1643473290_4-na-dache-pro-p-bardak-v-komnate-foto-5.jpg",
        "https://en.idei.club/uploads/posts/2023-08/1691286643_en-idei-club-p-messy-room-asthetic-dizain-vkontakte-22.png"]
