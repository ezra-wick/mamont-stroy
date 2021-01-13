from django.contrib.auth.models import User, Group
from .models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_Customer(sender, instance, created, **kwards):
    if created:
        group = Group.objects.get(name='customers')
        instance.groups.add(group)
        Customer.objects.create(customer=instance,
                                username=instance.username,
                                first_name=instance.first_name,
                                last_name=instance.last_name,
                                email=instance.email
                                )


@receiver(post_save, sender=User)
def save_Customer(sender, instance, **kwards):
    instance.customer.save()





