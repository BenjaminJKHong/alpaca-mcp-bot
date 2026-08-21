import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

api_key = os.getenv('ALPACA_API_KEY')
secret_key = os.getenv('ALPACA_API_SECRET')

if not api_key or not secret_key:
    print("❌ Error: Missing API keys in .env file.")
    exit()

trading_client = TradingClient(api_key, secret_key, paper=True)

try:
    account = trading_client.get_account()
    print("✅ Connection Successful!")
    print(f"Status: {account.status}")
    print(f"Equity (Balance): ${account.equity}")
    print(f"Buying Power: ${account.buying_power}")
except Exception as e:
    print(f"❌ Connection Failed: {e}")