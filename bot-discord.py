import time
import nicefunc
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
import discord_webhook

# PASTE YOUR URL DISCORD WEBHOOK
url = 'https://discord.com/api/webhooks/___YOUR_URL_WEBHOOK'

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

        print('Pesquisando Moedas...')

        sumario = output.get_analysis().summary
        sum = sumario['RECOMMENDATION']
        s_sell = (sum == 'STRONG_SELL')
        s_buy = (sum == 'STRONG_BUY')

        medias = output.get_analysis().moving_averages
        rec = medias['RECOMMENDATION']
        m_sell = (rec == 'STRONG_SELL')
        m_buy = (rec == 'STRONG_BUY')

        if s_sell == True and m_sell == True:
            webhook = discord_webhook.DiscordWebhook(
                url=url, content=f'Cripto atualmente escaneada: {symbol}')
            response = webhook.execute()
            webhook = discord_webhook.DiscordWebhook(
                url=url, content=f'Forte Tendencia para Short :arrow_down:')
            response = webhook.execute()
            webhook = discord_webhook.DiscordWebhook(
                url=url, content='\n**********************************************')
            response = webhook.execute()
            print(s_sell, symbol, 'Short encontrado')
            print(m_sell, symbol, 'Short encontrado')

        if s_buy == True and m_buy == True:
            webhook = discord_webhook.DiscordWebhook(
                url=url, content=f'Cripto atualmente escaneada: {symbol}')
            response = webhook.execute()
            webhook = discord_webhook.DiscordWebhook(
                url=url, content=f'Forte Tendencia para Long :arrow_up:')
            response = webhook.execute()
            webhook = discord_webhook.DiscordWebhook(
                url=url, content='\n**********************************************')
            response = webhook.execute()
            print(s_sell, symbol, 'Long encontrado')
            print(m_sell, symbol, 'Long encontrado')

        time.sleep(3)
