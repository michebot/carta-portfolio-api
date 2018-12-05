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

