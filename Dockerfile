FROM python:3.8

WORKDIR /Netquest_Assignment

COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]