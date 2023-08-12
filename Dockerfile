# Use the official Python image as the base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install pipenv
RUN pipenv install django
RUN pip install django
RUN pipenv install django-debug-toolbar
RUN pip install django-debug-toolbar
RUN pip install pillow
RUN pipenv install pillow


# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/
COPY manage.py /app/
COPY . /app/
# Install dependencies using pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your application code into the container
COPY HausaufgabenPlus /app/HausaufgabenPlus  

# Start your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
