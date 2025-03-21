FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src

WORKDIR /app/src

CMD ["chainlit", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]
