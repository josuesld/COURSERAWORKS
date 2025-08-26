
import yfinance as yf
import pandas as pd

tesla = yf.Ticker("TSLA")

# Obtener el estado de ingresos (income statement)
income_stmt = tesla.financials

# Mostrar los primeros datos
print(income_stmt.head())
