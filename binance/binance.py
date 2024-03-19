import requests
import pandas as pd
from datetime import datetime, timedelta

def get_products():
    url = 'https://api.binance.com/api/v3/exchangeInfo'
    response = requests.get(url)
    data = response.json()
    products = [product['symbol'] for product in data['symbols']]
    products_df = pd.DataFrame(products, columns=['Product'])
    return products_df

def get_historical_data(symbol, interval, start_time, end_time):
    base_url = 'https://api.binance.com/api/v1/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
        'endTime': end_time
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
               'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
               'Taker buy quote asset volume', 'Ignore']
    df = pd.DataFrame(data, columns=columns)
    return df

# Отримати список доступних продуктів
print("Список доступних продуктів:")
products_df = get_products()
print(products_df)

# Вибрати 3 продукти
selected_products = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']

# Параметри для отримання історичних даних
interval = '1d'  # щоденно
end_time = datetime.now()
start_time_day = end_time - timedelta(days=1)
start_time_month = end_time - timedelta(days=30)
start_time_year = end_time - timedelta(days=365)

# Отримати і вивести історичні дані за останній день, місяць та рік для кожного вибраного продукту
for product in selected_products:
    print(f"\nІсторичні дані для продукту {product}:")
    
    print("\nЗа останній день:")
    historical_data_day = get_historical_data(product, interval, int(start_time_day.timestamp())*1000, int(end_time.timestamp())*1000)
    print(historical_data_day)
    
    print("\nЗа останній місяць:")
    historical_data_month = get_historical_data(product, interval, int(start_time_month.timestamp())*1000, int(end_time.timestamp())*1000)
    print(historical_data_month)
    
    print("\nЗа останній рік:")
    historical_data_year = get_historical_data(product, interval, int(start_time_year.timestamp())*1000, int(end_time.timestamp())*1000)
    print(historical_data_year)
