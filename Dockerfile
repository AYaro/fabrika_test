FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@admin.com
ENV DJANGO_SU_PASSWORD=password1234
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000