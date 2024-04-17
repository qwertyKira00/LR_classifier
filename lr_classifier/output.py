from .constants import MORAL, TYPE


def get_dom_index(predictions):
    return int(predictions.argmax(axis=0))


def get_dom_name_by_index(predictions, moral=False):
    index = get_dom_index(predictions)
    return MORAL[index] if moral else TYPE[index]


def convert_predictions_to_output(text, moral_predictions, type_predictions):
    return {
        'mainInformation': {                                # Основная информация о норме, для основной части
            'text': text,                                   # Текст нормы
            'profile': get_dom_name_by_index(               # Доминирующее моральное основание нормы
                moral_predictions[0], moral=True),
            'id_profile': get_dom_index(                    # id морального основания
                moral_predictions[0]
            ) + 1,
            'type': get_dom_name_by_index(                  # Тип нормы
                type_predictions[0]
            ),
            'id_type': get_dom_index(                       # id типа
                type_predictions[0]
            ) + 1,
        },
        'additionalInformation': {
            'profiles':  [                                  # Информация обо всех остальных моральных основаниях для дополнительной части
                {                                           # Объект с информацией по конкретному моральному основанию
                    'profile': 'Забота',                    # Название морального основания
                    'id_profile': 1,                        # id морального основания
                    'prob': round(                          # Значение соответствия данному моральному основанию
                        moral_predictions[0][0] * 100, 2    # относительно всех остальных моральных оснований
                    ),
                },
                {
                    'profile': 'Справедливость',
                    'id_profile': 2,
                    'prob': round(
                        moral_predictions[0][1] * 100, 2
                    ),
                },
                {
                    'profile': 'Лояльность',
                    'id_profile': 3,
                    'prob': round(
                        moral_predictions[0][2] * 100, 2
                    ),
                },
                {
                    'profile': 'Авторитет',
                    'id_profile': 4,
                    'prob': round(
                        moral_predictions[0][3] * 100, 2
                    ),
                },
                {
                    'profile': 'Чистота',
                    'id_profile': 5,
                    'prob': round(
                        moral_predictions[0][4] * 100, 2
                    ),
                },
                {
                    'profile': 'Нет эмоциональной окраски',
                    'id_profile': 6,
                    'prob': round(
                        moral_predictions[0][5] * 100, 2
                    ),
                },
            ],
            'types': [                                      # Информация обо всех остальных типах для дополнительной части
                {                                           # Объект с информацией по конкретному моральному основанию
                    'type': 'Дозволение',                   # Название типа
                    'id_type': 1,                           # id типа
                    'prob': round(                          # Значение соответствия данному типу
                        type_predictions[0][0] * 100, 2     # относительно всех остальных типов
                    ),
                },
                {
                    'type': 'Обязанность',
                    'id_type': 2,
                    'prob': round(
                        type_predictions[0][1] * 100, 2
                    ),
                },
                {
                    'type': 'Запрет',
                    'id_type': 3,
                    'prob': round(
                        type_predictions[0][2] * 100, 2
                    ),
                },
                {
                    'type': 'Дефиниция',
                    'id_type': 4,
                    'prob': round(
                        type_predictions[0][3] * 100, 2
                    ),
                },
                {
                    'type': 'Декларация',
                    'id_type': 5,
                    'prob': round(
                        type_predictions[0][4] * 100, 2
                    ),
                },
                {
                    'type': 'Цель',
                    'id_type': 6,
                    'prob': round(
                        type_predictions[0][5] * 100, 2
                    ),
                },
                {
                    'type': 'Иное',
                    'id_type': 7,
                    'prob': round(
                        type_predictions[0][6] * 100, 2
                    ),
                },
            ]
        }
    }

