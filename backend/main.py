from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import  numpy, pandas, requests, psycopg2
import psycopg2.extras

# Sets the display parameters for an easier view on the terminal when printing
pandas.set_option('display.max_rows', 10)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

app = FastAPI()
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Connect to db
connection = psycopg2.connect(host="ec2-54-81-126-150.compute-1.amazonaws.com", port=5432, dbname="das7mvst92faa0", user="nohrhjezxqouad", password="e8458698dd2407b14b1cf79178c83225ad137578305bd719f424ba7157039289")
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record, "\n")


@app.get("/")
async def index():
    cursor.execute("""
            SELECT * FROM tStocks ORDER BY fSymbol
        """)

    rows = cursor.fetchall()
    totalStocks = len(rows)

    return {"totalStocks": totalStocks}\

@app.get("/getTotalStocks")
async def getTotalStocks():
    cursor.execute("""
            SELECT * FROM tStocks ORDER BY fSymbol
        """)

    rows = cursor.fetchall()
    total_stocks = len(rows)

    return {"totalStocks": total_stocks}