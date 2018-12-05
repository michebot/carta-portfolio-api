# Carta Investor Services Fellowship: Portfolio API

##### By Michelle Espinosa

## Portfolio API Description

The investor services team at Carta manages investments for hundreds of venture capital firms.

Create an API for one piece of our product, the portfolio. Use the framework of your choice (Ruby on Rails, Flask, Django, Express, Sinatra, Slim, etc). The portfolio is a list of investments in companies, that can be viewed historically. Over time, investors buy and sell shares of companies, and need to view the state of their investments as of specific dates in the past for audit and accounting purposes.

Each investment should have the following data points:
  - Company: the company we invested in (set only on creation)
  - Quantity: number of shares held (this can change over time as we buy more stock from a company)
  - Cost: total amount paid (this can change over time as we buy more stock from a company)

Create an API endpoint that returns the state of all investments on a given date in the investment timeline. If no date is passed, assume we want investments data as of today.

The response should look something like the following:
```
/investments?date=2018-01-01

[
  {
    "company": "Meetly",
    "quantity": 1000,
    "cost": 1000
  },
  {
    "company": "IMIM",
    "quantity": 1000,
    "cost": 1000
  }
]
```

We will also need endpoints to create new investments, and to update existing investments as we buy/sell shares (updating the quantity and cost values for that point onward).

## Tech Stack
- Python
- Flask
- SQLAlchemy
- PostgreSQL
- JSON

## Requirements
- Python3
- pip

1. Set up an environment and run `pip install -r requirements.txt` to install requirements.

2. In the project root folder run `createdb portfolio_db` to create the database. Source secrets and then run `python model.py` and all tables will be created and populated.

3. Run `python api_server.py` and navigate [here](http://127.0.0.1:5000/).

## Usage

#### GET: get_all_investments
If a date isn't passed, it will return all investments as of today:
```
http://127.0.0.1:5000/investments
```

If a date is passed, it will return all investments up until that date:
```
http://127.0.0.1:5000/investments?date=2018-01-01
```

#### POST: create_investment
Creates a new investment transaction by specifying company id, asset, date (if no date is passed, the current date will be set) cost, and quantity.
```
curl -i -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/investments -d '{"company_id": 9, "asset": "Series A Preferred", "cost_per_share": 300, "num_shares": 300000}'
```

#### PATCH: PATCH_investment
Using the transaction id, update the quantity and cost of the investment.
```
curl -i -X PATCH -H "Content-Type:application/json" http://127.0.0.1:5000/investments/4 -d '{"num_shares": 15000, "cost_per_share": 30}'
```
