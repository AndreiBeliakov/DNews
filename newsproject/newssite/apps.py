from django.apps import AppConfig


class NewssiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newssite'

    def ready(self):
        import newssite.signals
        #from newsproject.newssite.tasks import send_message
        #from .schenduler import new_schenduler
        #print('started')

        #new_schenduler.add_job(
            #id='send mail',
            #func=lambda : print('123'),
            #trigger='interval',
            #seconds=10,
        #)
        #new_schenduler.start()
