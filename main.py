from flask import*
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'



app.run(host='0.0.0.0',port=8080)
