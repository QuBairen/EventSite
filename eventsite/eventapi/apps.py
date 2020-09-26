from django.apps import AppConfig


class EventapiConfig(AppConfig):
    name = 'eventsite.eventapi'

    def ready(self):
        import eventsite.eventapi.signals #noqa
