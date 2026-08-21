import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Load keys
load_dotenv()
api_key = os.getenv('ALPACA_API_KEY')
secret_key = os.getenv('ALPACA_API_SECRET')

# Initialize client
trading_client = TradingClient(api_key, secret_key, paper=True)

try:
    print("⏳ Attempting to place $1 order for SPY...")
    
    # Set up the order instructions
    market_order_data = MarketOrderRequest(
        symbol="SPY",
        notional=1.00,          # This tells Alpaca to buy exactly $1 worth
        side=OrderSide.BUY,     # We are buying
        time_in_force=TimeInForce.DAY
    )

    # Execute the order
    market_order = trading_client.submit_order(order_data=market_order_data)

    print("✅ Order Successfully Submitted!")
    print(f"Asset: {market_order.symbol}")
    print(f"Amount: ${market_order.notional}")
    print(f"Order ID: {market_order.id}")

except Exception as e:
    print(f"❌ Order Failed: {e}")