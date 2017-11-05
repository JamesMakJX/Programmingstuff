import datetime as dt
from datetime import timedelta
import pandas as pd
import pandas_datareader.data as web
import csv

years = 1
days_per_year = 365.24

start = dt.date.today() - dt.timedelta(days=(years*days_per_year))
end = dt.date.today()

writer = pd.ExcelWriter('StockData.xlsx')

        
##def add_stock():
##    source = input("Source of data (Eg. Yahoo = Yahoo finance):")
##    stock_code = input("Stock Code from Source (Eg. TSLA = Tesla):")
##    global sc
##    global s
##    sc = stock_code
##    s = source
##    df = web.DataReader(stock_code, source, start, end)
##    df.to_excel(writer, sheet_name="{}".format(stock_code))
##    writer.save()
##    with open('Stock_list.csv', 'r') as Stock_list:
##        reader = csv.reader(Stock_list)
##        if ([sc, s] in reader) is False:
##            with open('Stock_list.csv', 'a', newline="") as Stock_add:
##                csv_writer = csv.writer(Stock_add)
##                csv_writer.writerow([sc, s])
##
##def update():
##    with open('Stock_list.csv', 'r') as Stock_list:
##        reader = csv.reader(Stock_list)
##        for [sc, s] in reader:
##            print("Updating: {}".format(sc))
##            add_stock(sc, s)
##            print("Updated: {}".format(sc))



def add_stock():
    source=input("Source of data (Eg. Yahoo = Yahoo finance):")
    stock_code=input("Stock Code from Source (Eg. TSLA = Tesla):")
    with open('Stock_list.csv', 'r') as Stock_list:
        reader = csv.reader(Stock_list)
        if ([stock_code, source] in reader) is False:
            with open('Stock_list.csv', 'a', newline="") as Stock_add:
                csv_writer = csv.writer(Stock_add)
                csv_writer.writerow([stock_code, source])


def update():
    with open('Stock_list.csv', 'r') as Stock_list:
        reader = csv.reader(Stock_list)
        for [stock_code, source] in reader:
            print("Updating: {}".format(stock_code))
            df = web.DataReader(stock_code, source, start, end)
            df.to_excel(writer, sheet_name="{}".format(stock_code))
            writer.save()
            print("Updated: {}".format(stock_code))
