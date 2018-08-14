FROM 176.122.188.100:16000/django_base_image:0.2

COPY ./src/the_project/ /var/www/project/app/backend/

EXPOSE 8000

CMD ["python3", "/var/www/project/app/backend/manage.py", "runserver", "0.0.0.0:8000"]