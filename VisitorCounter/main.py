from flask import Flask,render_template
import redis
import os
import logging
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from the .env file (if present)
load_dotenv()


# Connect to Redis
redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT"))
try:
  redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
except Exception as ex:
  logging.critical(ex)
  
# @app.route('/')
# def welcome():
#     return "Welcome to my App!"

@app.route('/')
def count():
  try:  
    count = redis_client.incr('visitor_count')
    return render_template('index.html' ,count=count)
    #return f'You are Visitor number: {count}'
  except Exception as ex:
    logging.critical(ex)
    return(str(ex))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)