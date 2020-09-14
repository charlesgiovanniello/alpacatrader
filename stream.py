import config
import websocket, json

def on_open(ws):
    #Takes a reference to the websocket application, then provide the action (authenticate) along with authentication credentials
    #Next, send the authentication data to the websocket app
    print("Opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
    }

    ws.send(json.dumps(auth_data))
    
    listen_message = {"action": "listen", "data": {"streams": ["T.MSFT", "T.AAPL"]}}
    
    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("Received a message")
    print(message)

def on_close(ws):
    print("\nClosed connection")

socket = "wss://data.alpaca.markets/stream" #data.alpaca will gather all market data (when specifying the requests)

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()