from django.apps import AppConfig


class DjParserConfig(AppConfig):
    name = 'dj_parser'

    def ready(self):
        import dj_parser.signals
