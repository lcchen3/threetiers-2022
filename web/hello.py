# import package flask
from flask import Flask #python server

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

#create flask app
app = Flask(__name__)

#create root route to create API
@app.route('/')
def hello_world():
    return 'Hello mars!'

#start server, debug so that we can stop in middle
if __name__ == '__main__':
    app.run(debug=True, port=3000)





