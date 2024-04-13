from tensorflow.keras.preprocessing.sequence import pad_sequences
from django.apps import apps

tokenizer = apps.get_app_config('lr_classifier').tokenizer
max_sequence_length = apps.get_app_config('lr_classifier').max_sequence_length


def preprocess_text(text):
    text_sequences = tokenizer.texts_to_sequences(text)
    text_padded = pad_sequences(
        text_sequences,
        maxlen=max_sequence_length
    )

    return text_padded


def convert_predictions_to_output(predictions):
    print(round(predictions[0][0] * 100, 2))
    return {
        'Authority': round(predictions[0][0] * 100, 2),
        'Fairness': round(predictions[0][1] * 100, 2),
        'Care': round(predictions[0][2] * 100, 2),
        'Loyalty': round(predictions[0][3] * 100, 2),
        'Purity': round(predictions[0][4] * 100, 2),
    }
