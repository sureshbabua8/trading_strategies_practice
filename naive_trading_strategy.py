import alpaca_trade_api as tradeapi
import random

API_KEY = "****"
API_SECRET = "****"
BASE_URL = "https://paper-api.alpaca.markets"

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

# Get account information
account = api.get_account()

# Cancel any open orders so they don't interfere with this script
api.cancel_all_orders()

# Get a list of tradable assets
assets = api.list_assets(status="active")

# Filter tradable assets to only include stocks
tradable_assets = [asset for asset in assets if asset.tradable]

# Define the number of random assets to select for trading
num_assets_to_trade = 10

while True:
    # Randomly select assets to trade
    assets_to_trade = random.sample(tradable_assets, num_assets_to_trade)

    # Place random buy or sell orders for each selected asset
    for asset in assets_to_trade:
        side = random.choice(["buy", "sell"])
        quantity = random.randint(1, 10)  # Randomly select quantity to trade
        if side == "buy":
            try:
                api.submit_order(
                    symbol=asset.symbol,
                    qty=quantity,
                    side="buy",
                    type="market",
                    time_in_force="gtc"
                )
                print(f"Bought {quantity} shares of {asset.symbol} at market price.")
            except Exception as e:
                print(f"Failed to buy {quantity} shares of {asset.symbol}: {e}")
        elif side == "sell":
            try:
                api.submit_order(
                    symbol=asset.symbol,
                    qty=quantity,
                    side="sell",
                    type="market",
                    time_in_force="gtc"
                )
                print(f"Sold {quantity} shares of {asset.symbol} at market price.")
            except Exception as e:
                print(f"Failed to sell {quantity} shares of {asset.symbol}: {e}")
