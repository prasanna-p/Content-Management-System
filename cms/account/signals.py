from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import User
from django.contrib.auth.models import Group


@receiver(post_save,sender = User)
def set_user_group(sender,instance,created, **kwargs):
    if created:
        group = Group.objects.get(name='User')
        instance.groups.add(group)

