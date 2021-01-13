from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from PIL import Image
from django.conf import settings

User = get_user_model()

class ManagerUser(models.Model):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now)
    profile_pic=models.ImageField(default='default.png',
                                  null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customer')
    username=models.CharField(max_length=191, null=True, blank=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    address=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    img=models.ImageField(default='default.png', upload_to='media/user_image')

    def __str__(self):
        return self.customer.username
    
    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        image = Image.open(self.img.path)
        if image.height > 360 or image.width > 240:
            resize = (360, 240)
            image.thumbnail(resize)
            image.save(self.img.path)

            