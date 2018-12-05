# model.py

"""Models and database functions for portfolio_db."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

    def __repr__(self):
        """Show info about Investments"""

        return """<Company id={}, Company={}>"""\
               .format(self.company_id, self.company)


class Transaction(db.Model):
    """Transaction model"""

    # table name and columns
    __tablename__ = "transactions"

    trx_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey("investments.company_id"), 
                           nullable=False)
    asset = db.Column(db.String(130), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    # maybe cost and amt better as floats?
    cost_per_share = db.Column(db.Integer, nullable=False)
    num_shares = db. Column(db.Integer, nullable=False)

    # define relationships
    company = db.relationship("Investment", backref="investment_trx")

    def __repr__(self):
        """Show info about transactions"""

        return """<Transaction id={}, Asset={}, Date={}, 
               Cost per share={}, Num shares={}>"""\
               .format(self.trx_id, self.asset, self.date, 
                       self.cost_per_share, self.num_shares)


### Helper functions ###
def connect_to_db(app, db_uri='postgresql:///portfolio_db'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


def load_investments():
    """Load investments into database."""

    # Delete all rows in table, so duplicate companies won't be made
    Investment.query.delete()

    investments = ["Arcanerover", "Berry Cloud Inc.", "BetaHex", 
                   "EverChat", "Krakatoa", "Mystic Brews", 
                   "Questindustries", "Test Letter", "ZeusBeat",]

    investments_to_add = []

    for investment in investments:
        investment = Investment(company=investment)
        investments_to_add.append(investment)

    db.session.add_all(investments_to_add)
    db.session.commit()

def load_transactions():
    """Load transactions into database."""

    # Delete all rows in table, so duplicate transactions won't be made.
    Transaction.query.delete()

    arcanerover_a = Transaction(company_id=1, 
                                asset="Series A Preferred", 
                                date="2014 Aug 01",
                                cost_per_share=25, 
                                num_shares=10000)
    arcanerover_b = Transaction(company_id=1, 
                                asset="Series B Preferred", 
                                date="2018 Sep 18",
                                cost_per_share=30, 
                                num_shares=15000)
    berry_cloud_inc_seed = Transaction(company_id=2, 
                                       asset="Series Seed Preferred", 
                                       date="2016 Jul 01",
                                       cost_per_share=11, 
                                       num_shares=5000)
    betahex_seed = Transaction(company_id=3, 
                               asset="Series Seed Preferred", 
                               date="2015 Sep 30",
                               cost_per_share=30, 
                               num_shares=8000)
    krakatoa_common = Transaction(company_id=5, 
                                  asset="Series Seed Preferred", 
                                  date="2018 Jan 05",
                                  cost_per_share=10, 
                                  num_shares=10000)

    db.session.add_all([arcanerover_a, arcanerover_b, berry_cloud_inc_seed, 
                        betahex_seed, krakatoa_common])
    db.session.commit()



if __name__ == "__main__":

    from api_server import app
    # connect_to_db(create_app)
    connect_to_db(app)
    print("Connected to DB.")

