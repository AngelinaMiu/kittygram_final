FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

FROM nginx:1.22.1

COPY nginx.conf /etc/nginx/templates/default.conf.template

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]

ENV PIP_ROOT_USER_ACTION=ignore
