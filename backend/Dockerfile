FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]