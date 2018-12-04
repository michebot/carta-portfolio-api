# /app.py


### IMPORTS ###
import os
import datetime
from flask import Flask, jsonify, request, json, Response
from config import app_config
from model import Transaction, Investment, db, connect_to_db


# app initialization
app = Flask(__name__)


### COMPANY API ROUTES ###
@app.route("/", methods=["GET"])
def index():
    """First endpoint"""

    return jsonify({"show": "I'm showing"})


@app.route("/companies", methods=["GET"])
def get_all_companies():

    companies = Investment.query.all()

    output = []

    for company in companies:
        company_data = {}
        company_data["company_id"] = company.company_id
        company_data["company"] = company.company
        output.append(company_data)

    return jsonify({"companies": output})


@app.route("/companies/<company_id>", methods=["GET"])
def get_one_company():
    return ""

@app.route("/company", methods=["POST"])
def create_company():

    data = request.get_json()

    new_company = Investment(company=data["company"])
    db.session.add(new_company)
    db.session.commit()

    return jsonify({"message": "New investment company."})

@app.route("/company/<company_id>", methods=["PUT"])
def update_company():
    return ""


### INVESTMENT TRANSACTION API ROUTES ###
@app.route("/investments", methods=["GET"])
def get_all_investments():

    investments = Transaction.query.all()
    

    output = []

    for investment in investments:
        investment_data = {}
        investment_data["company_id"] = investment.company_id
        investment_data["asset"] = investment.asset
        investment_data["trx_date"] = investment.trx_date
        investment_data["cost_per_share"] = investment.cost_per_share
        investment_data["amt_of_shares"] = investment.amt_of_shares
        output.append(investment_data)

    return jsonify({"investments": output})



@app.route("/investments/<investment_id>", methods=["GET"])
def get_one_investment():
    return ""

@app.route("/investments", methods=["POST"])
def create_investment():

    data = request.get_json()

    new_investment = Transaction(company_id=data["company_id"], 
                                 asset=data["asset"], 
                                 trx_date=datetime.datetime.utcnow(), 
                                 cost_per_share=data["cost_per_share"], 
                                 amt_of_shares=data["amt_of_shares"])
    db.session.add(new_investment)
    db.session.commit()

    return jsonify({"message": "New investment transaction."})

@app.route("/investments/<investment_id>", methods=["PUT"])
def update_investment():
    return ""



if __name__ == "__main__":

    # env_name = os.getenv("FLASK_ENV")
    # app = create_app(env_name)
    # run app
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")


# def create_app(env_name):
#     """Create app"""

#     # app initialization
#     app = Flask(__name__)

#     app.config.from_object(app_config[env_name])

#     # db.init_app(app)

#     @app.route("/", methods=["GET"])
#     def index():
#         """First endpoint"""

#         return jsonify({"show": "I'm showing"})

#     return app

# if __name__ == "__main__":

#     env_name = os.getenv("FLASK_ENV")
#     app = create_app(env_name)
#     # run app
#     app.run(debug=True, host="0.0.0.0")
