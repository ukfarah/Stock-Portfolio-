import requests

# Define the portfolio dictionary
portfolio = {}
# Replace with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

# Function to add stock to the portfolio
def add_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity
    print(f"Added {quantity} shares of {symbol}.")

# Function to remove stock from the portfolio
def remove_stock(symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol] > quantity:
            portfolio[symbol] -= quantity
            print(f"Removed {quantity} shares of {symbol}.")
        elif portfolio[symbol] == quantity:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol}.")
        else:
            print(f"Cannot remove {quantity} shares. Only {portfolio[symbol]} shares available.")
    else:
        print(f"{symbol} not found in portfolio.")

# Function to get real-time stock price
def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        return float(data['Time Series (1min)'][latest_time]['1. open'])
    else:
        print(f"Error fetching data for {symbol}.")
        return None

# Function to track the portfolio performance
def track_portfolio():
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            value = price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

# Main function to handle user input
def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(symbol, quantity)
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
