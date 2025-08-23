import os
import ssl
import certifi
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

load_dotenv()

ssl_context = ssl.create_default_context(cafile=certifi.where())

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"], ssl=ssl_context)
app = App(client=client)

@app.event("message")
def handle_message_events(event, say, logger):
    logger.info(f"EVENT: {event}")
    if event.get("subtype") is not None:
        return
    text = (event.get("text") or "").strip()
    if not text:
        return
    say(text=f"- RE: {text}", thread_ts=event.get("thread_ts") or event.get("ts"))

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()