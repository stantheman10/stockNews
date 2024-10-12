import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ.get("STOCK_API")
NEWS_API_KEY = os.environ.get("NEWS_API")


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

news_params = {
    "q": "tesla",
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
    "language": "en",
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()
yest_date = list(data["Time Series (Daily)"].keys())[0]
close_value_yest = data["Time Series (Daily)"][yest_date]["4. close"]
print(close_value_yest, "Day Before Yest")

day_bfr_date = list(data["Time Series (Daily)"].keys())[1]
close_value_day_bfr = data["Time Series (Daily)"][day_bfr_date]["4. close"]
print(close_value_day_bfr, "Yesterday")

diff = float(close_value_yest) - float(close_value_day_bfr)
print(abs(diff))

per = (abs(diff) / float(close_value_yest)) * 100

print("5% of yestersdays stock is ", per)

if per > 5:
    print("Get News")

    res = requests.get(NEWS_ENDPOINT, params=news_params)
    data = res.json()["articles"]
    three_articles = data[:3]
    for article in three_articles:
        formatted_articles = [
            f"Headline: {article['title']}\n Brief: {article['description']}"
            for article in three_articles
        ]

    print(formatted_articles)


