from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.template.loader import render_to_string, get_template
from django.template import Context

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Спасибо! Мы получили от Вас письмо!'
    #message = f'Уважаемый(ая)  {order.first_name},\n\nВы успешно оформили заказ.\n\Номер вашего заказа {order.id}.'
    ctx = {'user': order.name,
            'phone': order.phone,
            'email': order.email,
            'text': order.text}
    message = get_template('email.html').render(ctx)   

    mail_sent = send_mail(subject,
                          message,
                          'mamontov-stroy@ya.ru',
                           [order.email],
                           html_message=message)
    return mail_sent

@shared_task
def order_created_2(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Новое сообщение от клиента {order.name}'
    #message = f'Уважаемый(ая)  {order.first_name},\n\nВы успешно оформили заказ.\n\Номер вашего заказа {order.id}.'
    ctx = {'user': order.name,
            'phone': order.phone,
            'email': order.email,
            'text': order.text}
    message = get_template('email_2.html').render(ctx)   

    mail_sent = send_mail(subject,
                          message,
                          'mamontov-stroy@ya.ru',
                           ['mamontov-stroy@ya.ru'],
                           html_message=message)
    return mail_sent
