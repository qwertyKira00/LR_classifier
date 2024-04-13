from .preprocess import preprocess_text
from django.apps import apps

classifier = apps.get_app_config('lr_classifier').classifier


def predict(text):
    preprocessed_text = preprocess_text(text)
    predictions = classifier.predict(preprocessed_text)

    return predictions
