from django.apps import AppConfig



class StorefrontConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storefront'


    def ready(self):
        from storefront.schedule import api_refresh_schedule
        api_refresh_schedule()
