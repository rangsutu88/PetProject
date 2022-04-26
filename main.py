import time
import telebot
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from tradingview_ta import TA_Handler, Interval, Exchange

api_key = "wlt9AdgeaS3RWaFwWr2pfQN9O0hlSWdnBLQhayZHoT9XpEnuD5p2IvmM5DoZI0Xf"
api_secret = "D3e8p6UqnHuZaQdVDoaDU5svB60xTWSjjv0JLCmBOFM6fk5qoL4tjJTJHE1DfuMG"
client = Client(api_key, api_secret)

TOKEN = "5331277773:AAFLMHVaR_8ZSLrrVaTX6As7M9tfuBCLOZE"
bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['a'])  # welcome message handler
def send_welcome(message):
    tesla = TA_Handler(
        symbol="TSLA",
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY,
    )

    bot.reply_to(message, tesla.get_analysis().summary)



while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(1)
