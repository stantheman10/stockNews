import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "4YD0A964JFZ65C8M"
NEWS_API_KEY = "bef1f7fb60eb4bcc8f8483e300c02c81"


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


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

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

    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    # HINT 1: Think about using the Python Slice Operator
    res = requests.get(NEWS_ENDPOINT, params=news_params)
    data = res.json()["articles"]
    three_articles = data[:3]
    for article in three_articles:
        formatted_articles = [
            f"Headline: {article['title']}\n Brief: {article['description']}"
            for article in three_articles
        ]

    print(formatted_articles)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
