from django.apps import AppConfig


class VehicleListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicle_list'
    def ready(self):
        import vehicle_list.signals
