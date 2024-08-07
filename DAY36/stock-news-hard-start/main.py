import requests
import os
from twilio.rest import Client

# Need to give stock, twilio, news_credentials as environment variables and need to provide "to" value while sending msg using twilio
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_ENDPOINT_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_ENDPOINT_API_KEY = os.environ["NEWS_API_KEY"]

stock_endpnt_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_ENDPOINT_API_KEY
}

news_endpnt_params = {
    "q": COMPANY_NAME,
    "language": "en",
    "apiKey": NEWS_ENDPOINT_API_KEY
}


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

response = requests.get(url=STOCK_ENDPOINT, params=stock_endpnt_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Getting all days data
day_wise_data = [info for (day, info) in data.items()]

# Getting the yesterday's and day before yesterday's data
yesterdays_closing_price = float(day_wise_data[0]["4. close"])
day_before_yesterdays_closing_price = float(day_wise_data[1]["4. close"])

# Getting the difference and percentage change in it
diff = abs(yesterdays_closing_price - day_before_yesterdays_closing_price)

percentage_diff = (diff / yesterdays_closing_price) * 100

# fetch the first 3 articles for the COMPANY_NAME using https://newsapi.org/docs/endpoints/everything
if percentage_diff > 4:
    response = requests.get(url=NEWS_ENDPOINT, params=news_endpnt_params)
    response.raise_for_status()
    news_data = response.json()["articles"][:3]
    # print(news_data)
    if yesterdays_closing_price - day_before_yesterdays_closing_price > 0:
        percentage_symbol = f"🔺{abs(yesterdays_closing_price - day_before_yesterdays_closing_price)}%"
    else:
        percentage_symbol = f"🔻{abs(yesterdays_closing_price - day_before_yesterdays_closing_price)}%"
    # Send a separate message with each article's title and description to your phone number using twilio.com/docs/sms/quickstart/python
    for news in news_data:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"{STOCK}: {percentage_symbol}\n Headline: {news['title']}\nBrief: {news['description']}",
            from_="+17207261620",
            # Number need to be added while running
            to="",
        )
        print(message.status)
        print(message.body)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

