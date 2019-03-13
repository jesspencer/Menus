from flask import Flask
app = Flask(__name__)
#decorator in python
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    #tells the webserver on vagrant to listen on all public ports
    app.run(host = '0.0.0.0', port = 5000)
