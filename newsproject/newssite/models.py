from django.db import models
from django.urls import reverse


class New(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
    )

    name = models.CharField(
        max_length=100000,
        unique=True,
    )
    description = models.TextField()


    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:50000]}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])







class Author(models.Model):

    name = models.CharField(max_length=100000, unique=True)

    def __str__(self):
        return self.name.title()