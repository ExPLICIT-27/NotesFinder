from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.sessions.models import Session

@receiver(post_migrate)
def clear_sessions_onStart(sender, **kwargs):
    if sender.name == 'books':
        Session.objects.all().delete()
        