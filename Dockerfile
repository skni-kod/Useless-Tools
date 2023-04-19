FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --update --no-cache nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN python manage.py collectstatic --noinput 
EXPOSE 80
CMD nginx -g 'daemon off;' & gunicorn siteproject.wsgi:application --bind 0.0.0.0:8000

