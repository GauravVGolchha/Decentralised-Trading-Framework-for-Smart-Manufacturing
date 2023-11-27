from flask import Flask, request, jsonify
from flask_restful import Api
app = Flask(__name__)
api = Api(app)

database = {
    "123":{
        "RCMC":"123",
        "IEC":"123",
        "GST":"123",
        "Account":"123",
        "IFSC":"123",
        "QCI":"123",
    },
    "124":{
        "RCMC":"124",
        "IEC":"124",
        "GST":"124",
        "Account":"124",
        "IFSC":"124",
        "QCI":"124",
    },
    "125":{
        "RCMC":"125",
        "IEC":"125",
        "GST":"125",
        "Account":"125",
        "IFSC":"125",
        "QCI":"125",
    }
}


@app.route("/")
def home():
    return "Welcome home page of App setu"


@app.route("/tradeLicense/<string:tradeLicense>", methods=['GET'])
def checkTrade(tradeLicense):
    print(tradeLicense)
    if tradeLicense in database:
        return "True"
    else:
        return "False"

@app.route("/tradeLicense/<string:tradeLicense>/iec/<string:IEC>", methods=['GET'])
def checkIEC(tradeLicense,IEC):
    if database[tradeLicense]["IEC"] == IEC:
        return "True"
    else:
        return "False"    

@app.route("/tradeLicense/<string:tradeLicense>/rcmc/<string:RCMC>", methods=['GET'])
def checkRCMC(tradeLicense,RCMC):
    if database[tradeLicense]["RCMC"] == RCMC:
        return "True"
    else:
        return "False"    

@app.route("/tradeLicense/<string:tradeLicense>/qci/<string:QCI>", methods=['GET'])
def checkQCI(tradeLicense,QCI):
    if database[tradeLicense]["QCI"] == QCI:
        return "True"
    else:
        return "False"    

@app.route("/tradeLicense/<string:tradeLicense>/gst/<string:GST>", methods=['GET'])
def checkGST(tradeLicense,GST):
    if database[tradeLicense]["GST"] == GST:
        return "True"
    else:
        return "False"    


@app.route("/tradeLicense/<string:tradeLicense>/account/<string:Account>/ifsc/<string:IFSC>", methods=['GET'])
def checkAccount(tradeLicense,Account,IFSC):
    if database[tradeLicense]["Account"] == Account:
        return "True"
    else:
        return "False"    

if __name__ == '__main__':
    app.run(debug=True,port=49154)
    


