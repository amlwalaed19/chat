from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your models here.


class Massage(models.Model):
    author = models.ForeignKey(user, related_name='author_massages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_massages(self):
        return Massage.objects.order_by('-timestamp').all()[:10]
