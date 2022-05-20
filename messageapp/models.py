from django.db import models
from django.contrib.auth.models import User

class Msg(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_usr = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name= "Message"
        verbose_name_plural = "Messages"
        ordering = ['created_at']

    def __str__(self):
        return self.message
