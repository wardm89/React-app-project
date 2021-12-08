

#Market Data Finacial Modeling Prep
#https://financialmodelingprep.com/developer/docs
MARKET_DATA_KEY = "2d4ad5ce693c78727709ececae93b167"

#Alpaca Keys
API_KEY="PKTOOC2EQ8G086W1PMKD"
SECRET_KEY="BkXpxsIRNMdyUC0Yq0BqGrIqSQcQzb3ms8vmYhT0"

# ALPACA_SOCKET = "wss://data.alpaca.markets/stream"
ALPACA_SOCKET = "wss://stream.data.alpaca.markets/v2/{source}"


COINBASE_PRO_SOCKET      = "wss://ws-feed.pro.coinbase.com"                 #Live trading
COINBASE_PRO_URL         = "https://api.pro.coinbase.com"                   #Live trading
SAND_COINBASE_PRO_URL    = "https://api-public.sandbox.pro.coinbase.com"    #sandbox
SAND_COINBASE_PRO_SOCKET = "wss://ws-feed-public.sandbox.pro.coinbase.com"  #sandbox
#Coinbase Pro
COINBASE_PRO_KEY = "6f14c7c18e7161b690866cec701369ba" #Dev Key
COINBASE_PRO_PASSPHRASE = "hklfxlh7q9k" #Dev Key
COINBASE_PRO_SECRET_KEY = "3SvH7kWWyGzCy6FNC6Yd14imm5lQZ2W5mCvbYSCAWesadwzA5iLsAOTlafVK+0jr9R5pejvPEbkwk1BTdD47SQ==" #Dev Key
SAND_COINBASE_PRO_KEY = "ea768b1af08f0c51e9f1f5638aadd47a"
SAND_COINBASE_PRO_PASSPHRASE = "gi4naxn2soi"
SAND_COINBASE_PRO_SECRET_KEY = "m9LfardNi4bTXc0uiSq8bUZ5DtkeMtbmzm/RU7Wj5e14EF2IMVr63dr/19LyTEruwvzeclrJq54R1UnUwaCPAw=="

#Coinbase Pro
COINBASE_KEY        = "UY8YSkAcAB4aJ30k" #Dev Key
COINBASE_SECRET_KEY = "mX6nGgzAgpZqlxqOmt7dAHt9oP9FpaL8" #Dev Key
COINBASE_URL        = "'https://api.coinbase.com/v2/'"

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_CRYPTO_URL = "https://data.alpaca.markets/v1beta1/crypto"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
ASSETS_URL = "{}/v2/assets".format(BASE_URL)
BARS_URL = "{}/v2/stocks".format(BASE_URL)
CRYPTO_BARS_URL = "{}".format(ALPACA_CRYPTO_URL)
POSITIONS_URL = "{}/v2/positions".format(BASE_URL)

#Email Credentials
EMAIL_PORT = 465
EMAIL_ADDRESS = 'tradingedgeupdates@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PASSWORD = 'IS6U3VHrSo3v'

#PostgresDb Credentials
DATABASE_URL = "postgres://nohrhjezxqouad:e8458698dd2407b14b1cf79178c83225ad137578305bd719f424ba7157039289@ec2-54-81-126-150.compute-1.amazonaws.com:5432/das7mvst92faa0"




#Coinbase pro account IDs for currencies
USD_ACCOUNT_ID = '5211a2fb-1bb0-4c3d-bfc4-d0c5f221a470'


