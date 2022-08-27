from django.apps import AppConfig
import glob
import datetime
import os


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        drc = 'main\\tmp\\'

        for f in os.listdir(drc):
            file = drc+f
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(file))
            duration = today - modified_date
            if duration.days >= 1:
                os.remove(file)
