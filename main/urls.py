from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('about/', views.about, name='about-name'),
    path('uslugi/', views.uslugi, name='uslugi'),
    path('prices/', views.prices, name='prices'),
    path('enter_post/', views.text_enter, name='text_enter'),
    path('update_post/<int:id>/<str:title_name>/', views.prices_enter, name='prices_enter'),
    path('enter/', views.prices_enter, name='prices_enter'),
    path('list/', views.all_text, name='all_text'),
    path('text_edit/<str:title>/<int:id>/', views.text_edit, name="text_edit"),
   # path("prices/<int:id>/edit/", views.category_edit, name="category_edit"),
    path("prices/<int:id>/delete/", views.category_delete, name="category_delete"),
    path("prices/<int:id>/<str:name>/edit/", views.product_edit, name="product_edit"),
    path("prices/<int:id>/<str:name>/delete/", views.product_delete, name="product_delete"),
    path('', views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)