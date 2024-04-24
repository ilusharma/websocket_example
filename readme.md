# Websocket example

## install Dependencies
```bash
pip install -r requirements.txt
```

## Run the server
```bash
daphne socketExample.asgi:application
```

## Run celery worker
```bash
 celery -A socketExample worker --loglevel=info
```

## Run celery beat
```bash
celery -A socketExample beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
