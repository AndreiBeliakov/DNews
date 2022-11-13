import os
#from dotenv import load_dotenv
from django.shortcuts import redirect, render, reverse
from newsproject.newssite.models import New, Author
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime, date, timedelta
from newsproject.accounts.models import User, UsersSubscriptions




def send_message(pk_, id_authors_):
    new = New.objects.get(id=pk_)
    emails = User.objects.filter(author__in=id_authors_).values('email').distinct()
    email_list = [item['email'] for item in emails]
    html_content = render_to_string(
        'subscribe_created.html',
        {
            'subscribe': new
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{new.header}',
        body=new.text,
        from_email=os.getenv('EMAIL_GOOGLE_FULL'),
        to=email_list,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def week_news():
    start = datetime.now() - timedelta(7)
    finish = datetime.now()
    authors = Author.objects.all()

    for author_ in authors:
        new_list = New.objects.filter(date_time__range = (start, finish), author=author_.pk)
        print(new_list)
        email_list = []
        print(author_)
        for user_ in User.objects.all():
            user_email = UsersSubscriptions.objects.filter(author=author_.pk, user=user_.pk)
            if user_email and user_email not in email_list:
                email_list.append(user_.email)
        print(email_list)

        if new_list:
            html_content = render_to_string(
                'week_news.html',
                {
                    'news': new_list,
                    'author': author_.author_name
                }
            )
            msg = EmailMultiAlternatives(
                subject="Новости за неделю",
                from_email=os.getenv('EMAIL_GOOGLE_FULL'),
                to=email_list,
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()