import time
import nicefunc
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed

# PASTE YOUR URL DISCORD WEBHOOK
url = 'https://discord.com/api/webhooks/1024788396008276051/BIyICicJVTMp0gP17iq0kvCrxt5bOPBAsm7qsw9tumAx5oySwV3tqK-XSyu11c54xdKe'

# GET HOUR AND DATE
now = datetime.now()

# GET SYMBOLS IN FILE
symbols = nicefunc.coins

# WELCOME MSG
welcome = '''
            *************************
            *** BEM VINDO AO BOT  ***
            *************************
            ******** DISCORD ********
            *************************
            ******** BY D0MB ********
            *************************
'''
print(welcome)

while True:
    for symbol in symbols:
        output = TA_Handler(symbol=symbol,
                            screener='Crypto',
                            exchange='Binance',
                            interval=Interval.INTERVAL_1_MINUTE)

    # Retrieve recommendation.
        rec = output.get_analysis().summary["RECOMMENDATION"]
        rec1 = output.get_analysis().oscillators["RECOMMENDATION"]
        rec2 = output.get_analysis().moving_averages["RECOMMENDATION"]
        rec3 = output.get_analysis().indicators["Recommend.All"]
        print('Pesquisando...', symbol)
        # print('Sumary ', rec, 'oscillators ', rec1,
        #       'moving_averages ', rec2, 'indicators ', rec3)

        if rec3 >= 0.60:

            webhook = discord_webhook.DiscordWebhook(url=url)
            embed = DiscordEmbed(
                title=f'Coin: {symbol}', description='Forte Tendencia para Long :arrow_up:', color='58FC00')
            webhook.add_embed(embed)
            response = webhook.execute()

            print('Moeda: -->> ', symbol, 'Sumario: ', rec, 'Osciladores: ',
                  rec1, 'Medias: ', rec2, 'Indicators BUY', rec3)

        if rec3 <= -0.60:

            webhook = discord_webhook.DiscordWebhook(url=url)
            embed = DiscordEmbed(
                title=f'Coin: {symbol}', description='Forte Tendencia para Short :arrow_down:', color='FC2200')
            webhook.add_embed(embed)
            response = webhook.execute()

            print('Moeda: -->> ', symbol, 'Sumario: ', rec, 'Osciladores: ',
                  rec1, 'Medias: ', rec2, 'Indicators SELL', rec3)
