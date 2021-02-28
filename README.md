# paprika-server

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в формате `ПЕРЕМЕННАЯ = значение`.

Доступные переменные:

- `DEBUG` — режим отладки. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — список доменов/хостов, на которых будет работать сайт. Подробнее в [документации Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

Пример:

```env
DEBUG = True
SECRET_KEY = 1rr!a(+$-8sf(9+sc)a-k2q%cqswc39qto#ba%wjv!or75h0k3
ALLOWED_HOSTS = localhost,127.0.0.1,example.com,www.example.com
```
