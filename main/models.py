from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    categorian = models.CharField(max_length=200, db_index=True)
    
    def __str__(self):
        return self.categorian

    def get_products(self):
        return Job.objects.filter(category__categorian=self.categorian)


class Job(models.Model):
    category = models.ForeignKey(Category,
    related_name='jobs',
    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    measure = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(max_length=200, db_index=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    text = models.TextField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

class Post_Category(models.Model):
    INDEX = 'Главная'
    PRODUCTS = 'Специализция'
    ABOUT = 'О компании'
    PAGES = [(INDEX, 'Главная страница'), (PRODUCTS, 'Страница специализации'), 
              (ABOUT, 'О нас'),  ]
    title = models.CharField(max_length=20,
    choices=PAGES,
    default=INDEX,
    db_index=True)

    def __str__(self):
        return self.title

    def get_products(self):
        return Post.objects.filter(title_name__title=self.title)

class Post(models.Model):
    title_name = models.ManyToManyField(Post_Category,
    related_name='post',)
    text_one = RichTextField( db_index=True, null=True, blank=True,)
    text_second = RichTextField(db_index=True, null=True, blank=True)
    text_third = RichTextField(db_index=True, null=True,  blank=True)
    text_four = RichTextField(db_index=True, null=True,  blank=True)

    def __str__(self):
        return str(self.title_name)


        
    

