FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "sleep 10 && python manage.py makemigrations api --noinput && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]