from .preprocess import PreprocessMoral, PreprocessType
from django.apps import apps

classifier_moral = apps.get_app_config('lr_classifier').classifier_moral
classifier_type = apps.get_app_config('lr_classifier').classifier_type


def predict(text):
    preprocess_moral = PreprocessMoral()
    preprocessed_text_moral = preprocess_moral.preprocess_text(text)
    moral_predictions = classifier_moral.predict(preprocessed_text_moral)

    preprocess_type = PreprocessType()
    preprocessed_text_type = preprocess_type.preprocess_text(text)
    type_predictions = classifier_type.predict(preprocessed_text_type)

    return moral_predictions, type_predictions

