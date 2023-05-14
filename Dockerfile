FROM nginx:stable-alpine
RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools

RUN ln -sf python3 /usr/bin/python \
    && ln -sf pip3 /usr/bin/pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
RUN python manage.py collectstatic --noinput 
EXPOSE 80
CMD gunicorn siteproject.wsgi:application --bind 127.0.0.1:8000 & nginx -g 'daemon off;'
