import requests
import csv

url = 'https://api.binance.com/api/v3/ticker/24hr'
headers = {
    "Accept": 'application/json',
    "Content-Type": 'application/json'
}
response = requests.get(url, headers=headers)
myjson = response.json()
outdata = []

# Define the CSV header
csvheader = ['symbol', 'firstId', 'volume', 'priceChange', 'priceChangePercent',
             'weightedAvgPrice', 'prevClosePrice', 'lastPrice', 'lastQty', 'bidPrice',
             'bidQty', 'askPrice', 'askQty', 'openPrice', 'highPrice', 'lowPrice',
             'quoteVolume', 'openTime', 'closeTime', 'lastId', 'count']

for x in myjson:
    listing = [x['symbol'], x['firstId'], x['volume'], x['priceChange'], x['priceChangePercent'],
               x['weightedAvgPrice'], x['prevClosePrice'], x['lastPrice'], x['lastQty'], x['bidPrice'],
               x['bidQty'], x['askPrice'], x['askQty'], x['openPrice'], x['highPrice'], x['lowPrice'],
               x['quoteVolume'], x['openTime'], x['closeTime'], x['lastId'], x['count']]
    outdata.append(listing)

# Write data to a CSV file
with open('binance.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(outdata)

print("Done")
