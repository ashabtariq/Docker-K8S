FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV MONGO_URI=mongodb://mongo:27017/
EXPOSE 5000
CMD ["python", "app.py"]
