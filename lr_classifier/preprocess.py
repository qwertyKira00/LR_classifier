from tensorflow.keras.preprocessing.sequence import pad_sequences
from django.apps import apps


class Preprocess:
    tokenizer = None
    max_sequence_length = None

    def preprocess_text(self, text):
        text_sequences = self.tokenizer.texts_to_sequences(text)
        text_padded = pad_sequences(
            text_sequences,
            maxlen=self.max_sequence_length
        )
        return text_padded


class PreprocessMoral(Preprocess):
    tokenizer = apps.get_app_config('lr_classifier').tokenizer_moral
    max_sequence_length = apps.get_app_config('lr_classifier').max_sequence_length_moral


class PreprocessType(Preprocess):
    tokenizer = apps.get_app_config('lr_classifier').tokenizer_type
    max_sequence_length = apps.get_app_config('lr_classifier').max_sequence_length_type


