from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives, mail_managers
from django.template.loader import render_to_string
from .models import New, Author

@receiver(post_save, sender=New)
def notify_new(sender, instance, created, **kwargs):
     if created:
        subject = f'Добавлена новость:{instance.header} от {instance.date_time.strftime( "%d %m %Y" )}'
     else:
         subject = f'Изменена новость:{instance.header} от {instance.date_time.strftime( "%d %m %Y" )}'

     try:
         mail_managers(
            subject=subject,
             message=f'{instance.header} http://127.0.0.1/news/{instance.id}'
         )
     except Exception:
         print('ошибка отправки сообщения')
