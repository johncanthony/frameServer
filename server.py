from flask import Flask , request
from DataHandler import DataHandler

app = Flask(__name__)

ABOUT_INFO="info.json"



'''
FamFrame Info Page
'''
@app.route('/frame',methods=['GET'])
def get_dish():
        a = DataHandler("1234")
        print(a)
        return "FamFrame v0.1"


@app.route('/frame/healthcheck', methods=['GET'])
def healthcheck():
        return "GOOD"



if __name__=="__main__":
        app.run(host='0.0.0.0', port=1225 ,debug=True)
