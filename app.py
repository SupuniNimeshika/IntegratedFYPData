from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    print ('Sadeepa')
    return 'Hello World!'


@app.route('/accessToken/<token>' , methods=['POST'])
def fb_data(token):
    print ('access')
    print(str(token))
    re = 'https://graph.facebook.com/v3.2/me/posts?fields=comments%2Cmessage%2Cfull_picture&access_token='+token
    me1 = requests.get(re)
    # f1 =requests.get(friends)

    print(me1.text);
    return me1.text

if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port=9091, debug=False)
