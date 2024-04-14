from django.apps import AppConfig
import pickle
import tensorflow as tf


class LegalRuleClassificationAppConfig(AppConfig):
    name = 'lr_classifier'
    classifier_moral = None
    classifier_type = None
    tokenizer_moral = None
    tokenizer_type = None
    max_sequence_length_moral = None
    max_sequence_length_type = None

    def ready(self):
        self.classifier_moral = tf.keras.models.load_model(
            "model/legal_rule_classifier_moral.keras"
        )
        self.classifier_type = tf.keras.models.load_model(
            "model/legal_rule_classifier_type.keras"
        )

        with open('model/tokenizer_moral.pickle', 'rb') as handle:
            self.tokenizer_moral = pickle.load(handle)
        with open('model/tokenizer_type.pickle', 'rb') as handle:
            self.tokenizer_type = pickle.load(handle)

        self.max_sequence_length_moral = 10691
        self.max_sequence_length_type = 22042
