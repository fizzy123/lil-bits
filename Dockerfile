FROM python:3.6
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
CMD ["gunicorn", "-w", "1", "--threads", "3", "-b", ":5001", "server:app"]
