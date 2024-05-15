web: uvicorn gymception.asgi:application --host 0.0.0.0 --port $PORT --workers 4 --log-level info
worker: celery -A gymception worker -l info
beat: celery -A gymception beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
