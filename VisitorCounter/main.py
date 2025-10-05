from flask import Flask,render_template
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis-instance")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to my App!"

@app.route('/count')
def count():
  try:  
    count = redis_client.incr('visitor_count')
    return render_template('index.html' ,count=count)
    #return f'You are Visitor number: {count}'
  except Exception as ex:
    return(str(ex))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)