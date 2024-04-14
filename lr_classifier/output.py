from .constants import MORAL, TYPE


def get_dom_name_by_index(predictions, moral=False):
    index = predictions.argmax(axis=0)
    return MORAL[index] if moral else TYPE[index]


def convert_predictions_to_output(text, moral_predictions, type_predictions):
    return {
        'mainInformation': {                                # Основная информация о норме, для основной части
            'text': text,                                   # Текст нормы
            'Профиль_нормы': get_dom_name_by_index(         # Доминирующее моральное основание нормы
                moral_predictions[0], moral=True),
            'Тип_нормы': get_dom_name_by_index(             # Тип нормы
                type_predictions[0]
            ),
        },
        'additionalInformation': [                          # Информация обо всех остальных моральных основаниях для дополнительной части
            {                                               # Объект с информацией по конкретному моральному основанию
                'Профиль': 'Авторитет',                     # Название морального основания
                'Процент': round(                           # Значение соответствия данному моральному основанию
                    moral_predictions[0][0] * 100, 2        # относительно всех остальных моральных оснований
                ),
            },
            {
                'Профиль': 'Справедливость',
                'Процент': round(
                    moral_predictions[0][1] * 100, 2
                ),
            },
            {
                'Профиль': 'Забота',
                'Процент': round(
                    moral_predictions[0][2] * 100, 2
                ),
            },
            {
                'Профиль': 'Лояльность',
                'Процент': round(
                    moral_predictions[0][3] * 100, 2
                ),
            },
            {
                'Профиль': 'Чистота',
                'Процент': round(
                    moral_predictions[0][4] * 100, 2
                ),
            },
        ]
    }

