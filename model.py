# model.py

"""Models and database functions for the Portfolio db"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from marshmallow import fields, Schema

# import datetime


# class Investor(db.Model)
#     """Investors model"""

#     # table name and columns
#     __tablename__ = "investors"

#     investor_id = db.Column(db.Integer, primary_key=True)
#     investor_name = db.Column(db.String(130), nullable=False)


class Investment(db.Model):
    """Investments in companies model"""

    # table name and columns
    __tablename__ = "investments"

    company_id = db.Column(db.Integer, primary_key=True, 
        autoincrement=True)
    company = db.Column(db.String(130), nullable=False)


    # class constructor
    # def __init__(self, data):
    #     """Class constructor"""

    #     self.investment = data.get("investment")
    #     self.asset = data.get("asset")

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self, data):
    #     for key, item in data.items():
    #         setattr(self, key, item)
    #     db.dession.commit()

    # # def delete(self):
    # #     db.session.delete(self)
    # #     db.session.commit()

    # @staticmethod
    # def get_all_investments():
    #     return Investment.query.all()

    # @staticmethod
    # def get_one_investment(id):
    #     return Investment.query.get(id)

    def __repr__(self):
        """Show info about Investments"""

        return """<Company id={}, Company={}>"""\
               .format(self.company_id, self.company)


class Transaction(db.Model):
    """Transaction model"""

    # table name and columns
    __tablename__ = "transactions"

    trx_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, 
        db.ForeignKey("investments.company_id"), nullable=False)
    asset = db.Column(db.String(130), nullable=False)
    # date
    date = db.Column(db.DateTime, nullable=False)
    cost_per_share = db.Column(db.Integer, nullable=False)
    # num_shares
    num_shares = db. Column(db.Integer, nullable=False)

    # define relationships
    company = db.relationship("Investment", backref="investment_trx")


    # class constructor
    # def __init__(self, data):
    #     """Class constructor"""

    #     self.investment_date = datetime.datetime.utcnow()
    #     self.cost_per_share = data.get("cost_per_share")
    #     self.amt_of_shares = data.get("amt_of_shares")

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self, data):
    #     for key, item in data.items():
    #         setattr(self, key, item)
    #     self.investment_date = datetime.datetime.utcnow()
    #     db.dession.commit()

    # # def delete(self):
    # #     db.session.delete(self)
    # #     db.session.commit()

    # @staticmethod
    # def get_all_transactions():
    #     return Transaction.query.all()

    # @staticmethod
    # def get_one_transaction(id):
    #     return Transaction.query.get(id)

    def __repr__(self):
        """Show info about transactions"""

        return """<Transaction id={}, Asset={}, Date={}, 
               Cost per share={}, Num shares={}>"""\
               .format(self.trx_id, self.asset, self.date, 
                       self.cost_per_share, self.num_shares)




##############################################################################
# Helper functions


def connect_to_db(app, db_uri='postgresql:///portfolio_db'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


if __name__ == "__main__":

    from api_server import app
    # connect_to_db(create_app)
    connect_to_db(app)
    print("Connected to DB.")

