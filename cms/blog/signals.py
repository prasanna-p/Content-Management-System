from django.dispatch import receiver
from django.db.models.signals import post_save
from blog.models import post



@receiver(post_save,sender = post)
def set_user_Author(sender,instance,created,signal, **kwargs):
    if created:
        # print("1",sender.__dict__())
        print("2",instance)
        print("3",created)
        print("4",signal.__dict__)