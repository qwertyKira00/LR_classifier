from django.apps import AppConfig
import pickle
import tensorflow as tf


class LegalRuleClassificationAppConfig(AppConfig):
    name = 'lr_classifier'
    classifier = None
    tokenizer = None
    max_sequence_length= None

    def ready(self):
        self.classifier = tf.keras.models.load_model("model/legal_rule_classifier_moral.keras")
        with open('model/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.max_sequence_length = 10691
