import requests

# STOCK_DETAILS
stock_name = "TSLA"
company_name = "Tesla Inc"

# API_DETAILS
stock_api_key = "8KH6PX887FA5HKLW"
news_api_key = "9daffed90e1349c7843bd7b675a1dc58"
STOCK_URL = 'https://www.alphavantage.co/query'
NEWS_URL = 'https://newsapi.org/v2/everything'

# Params setup for stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": stock_api_key
}

# Request stock data
stock_request = requests.get(STOCK_URL, params=stock_params)
stock_data = stock_request.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# Yesterday's data
yesterdays_data = stock_data_list[0]
yesterdays_data_closing = float(yesterdays_data['4. close'])

# Day before yesterday's data
before_yesterdays_data = stock_data_list[1]
before_yesterdays_data_closing = float(before_yesterdays_data['4. close'])

# Step 1: Calculate the positive difference
positive_difference = abs(yesterdays_data_closing - before_yesterdays_data_closing)

# Step 2: Calculate 5% of yesterday's closing price
five_percent_value = yesterdays_data_closing * 0.05

# Check if the positive difference is greater than 5% of yesterday's closing price
if positive_difference > five_percent_value:
    # Params setup for news data
    news_params = {
        "q": company_name,
        "apiKey": news_api_key
    }

    # Request news data
    news_request = requests.get(NEWS_URL, params=news_params)
    news_data = news_request.json()

    # Step 3: Using python slice operator to create a list that contains the first 3 articles
    first_three_articles = news_data["articles"][:3]

    # Print the first three articles
    for i, article in enumerate(first_three_articles, start=1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")
else:
    print("The positive difference is not greater than 5% of yesterday's closing price. No news fetched.")
