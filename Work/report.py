#!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    '''
    Opens a portfolio file and reads it into a list of dictionaries
    '''
    with open(filename) as lines:
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return portfolio

def read_prices(filename):
    '''
    Reads a set of prices into a dictionary where the keys of the dictionary are the stock names
    and the values in the dictionary are the stock prices
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types =[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list and prices dictionary
    '''

    report = []

    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        listing = (s.name, s.shares, current_price, change)
        report.append(listing)

    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''

    #Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    #Create the report data
    report = make_report_data(portfolio, prices)

    #Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

def main(argv):
     portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
