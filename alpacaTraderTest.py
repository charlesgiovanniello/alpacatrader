import alpaca_trade_api as tradeapi
from config import *

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, base_url=APCA_API_BASE_URL) # or use ENV Vars shown below
account = api.get_account()
api.list_positions()
api.submit_order(
    symbol='SPY',
    side='buy',
    type='market',
    qty='100',
    time_in_force='day',
)
print(account.list_orders)