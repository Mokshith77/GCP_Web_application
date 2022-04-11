from flask import Flask,request, render_template,make_response,jsonify
import yfinance as yf
import flask
from api_constants import mongoDB_password
from flask_pymongo import PyMongo
import json


app = Flask(__name__)

database_name="API_1"

mongodb_client = PyMongo(app,uri="mongodb+srv://jj:{}@cluster0.gqhg7.mongodb.net/{}?retryWrites=true&w=majority".format(mongoDB_password,database_name))
db = mongodb_client.db

@app.route('/',methods=["POST","GET"])
def home():

    if request.method == 'POST':
        stock = request.form["stock"]
        period = request.form["period"]
        interval = request.form["interval"]
        var = yf.download(stock,period=period ,interval=interval)
        var1 = var.to_html()
        return var1

    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add():
    if request.method == 'POST':
        stock_id = request.form["stock_id"]
        symbol = request.form["symbol"]
        earnings = request.form["earnings"]
    db.stock.insert_one({'stock_id': stock_id, 'symbol': symbol,'earnings':earnings})
    return flask.jsonify(message="success")



@app.route("/read")
def read():
    stock = db.stock.distinct("symbol")
    return json.dumps([st for st in stock], default=str)


@app.route('/update',methods=["POST"])
def update():
    if request.method == 'POST':
        symbol = request.form["symbol"]
        updated_stock = {"$set": {'earnings' : 30}}
        filt = {'symbol' : symbol}
        db.stock.update_one(filt, updated_stock)
        result = {'result' : 'Updated successfully'}
        return result
    return ("Hello")




@app.route('/delete', methods=["POST", "GET"])
def delete():
    if request.method == 'POST':
        stock = request.form["stock"]
        filt = {'symbol': stock}
        db.stock.delete_one(filt)
        result = {'result': 'Deleted successfully'}
        return result

        stock = request.form["stock"]

##########

@app.route("/route_input")
def route_input():
    return render_template("input.html")

@app.route("/route_update")
def route_update():
    return render_template("update.html")

@app.route("/route_delete")
def route_delete():
    return render_template("delete.html")

@app.route("/route_home")
def route_home():
    return render_template("index.html")
##########


if __name__ == "__main__":
    app.run(debug = True)