from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# установить модуль настроек Django по умолчанию для программы «сельдерей».
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mamontov.settings')

app = Celery('mamontov')
# Использование строки здесь означает, что работник не должен сериализовать
# объект конфигурации для дочерних процессов.
# - namespace = 'CELERY' означает все связанные с сельдереем ключи конфигурации
# должен иметь префикс `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Загружать модули задач из всех зарегистрированных конфигов приложения Django.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))