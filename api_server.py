# /app.py


### IMPORTS ###
import os
import datetime
from pytz import timezone
import pytz
from flask import Flask, jsonify, request, json, Response
from config import app_config
from model import Transaction, Investment, db, connect_to_db


# app initialization
app = Flask(__name__)


### COMPANY API ROUTES ###
@app.route("/company", methods=["POST"])
def create_company():
    """API endpoint to create an investment company."""

    data = request.get_json()

    new_company = Investment(company=data["company"])
    db.session.add(new_company)
    db.session.commit()

    return jsonify({"message": "New investment company."})


@app.route("/companies", methods=["GET"])
def get_all_companies():
    """API endpoint to obtain all companies in our portfolio."""

    companies = Investment.query.all()

    output = []

    for company in companies:
        company_data = {}
        company_data["company_id"] = company.company_id
        company_data["company"] = company.company
        output.append(company_data)

    return jsonify({"companies": output})



### INVESTMENT TRANSACTION API ROUTES ###
@app.route("/investments", methods=["GET"])
def get_all_investments():
    """API endpoint that returns the state of all investments on a 
       given date. Default is investments as of today."""

    date = request.args.get("date")

    if date:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        investments = Transaction.query.filter(Transaction.date == date_obj).all()
    else:
        investments = Transaction.query.all()

    output = []

    for investment in investments:

        investment_data = {}
        # querying for the company's name
        company = Investment.query.get(investment.company_id)

        investment_data["company"] = company.company
        investment_data["cost"] = investment.cost_per_share
        investment_data["quantity"] = investment.num_shares
        output.append(investment_data)

    return jsonify({"investments": output})


@app.route("/investments", methods=["POST"])
def create_investment():
    """API endpoint to create new investment transactions."""

    data = request.get_json()

    new_investment = Transaction(company_id=data["company_id"], 
                                 asset=data["asset"], 
                                 date=datetime.datetime.utcnow(), 
                                 cost_per_share=data["cost_per_share"], 
                                 num_shares=data["num_shares"])
    db.session.add(new_investment)
    db.session.commit()

    return jsonify({"message": "New investment transaction."})


# PATCH REQUESTS for updating investments as buy/sell (PATCH_investment for fx name)
@app.route("/investments/<investment_id>", methods=["PUT"])
def update_investment():
    """API endpoint to update existing investments as we buy/sell shares"""
    return ""



if __name__ == "__main__":

    # env_name = os.getenv("FLASK_ENV")
    # app = create_app(env_name)
    # run app
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
