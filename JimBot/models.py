from django.db import models

class BotMessage(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)