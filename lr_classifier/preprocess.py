from tensorflow.keras.preprocessing.sequence import pad_sequences
from django.apps import apps


def preprocess_text(text, moral=False):
    if moral:
        tokenizer = apps.get_app_config('lr_classifier').tokenizer_moral
        max_sequence_length = apps.get_app_config('lr_classifier').max_sequence_length_moral
    else:
        tokenizer = apps.get_app_config('lr_classifier').tokenizer_type
        max_sequence_length = apps.get_app_config('lr_classifier').max_sequence_length_type

    text_sequences = tokenizer.texts_to_sequences(text)
    text_padded = pad_sequences(
        text_sequences,
        maxlen=max_sequence_length
    )

    return text_padded

