from django.db import models
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user


class UsersSubscriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.ForeignKey(newsproject.newssite.models.Author, on_delete=models.CASCADE)


class SubscribeMail(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    text = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200, default='none')


class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
