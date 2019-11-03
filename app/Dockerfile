FROM python:3.6-alpine

WORKDIR /app

COPY /app .

# Add necessary dependencies to run psycopg2
RUN pip install -r requirements.txt 

EXPOSE 8080

CMD ["python", "app.py"]

