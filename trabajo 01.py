import yfinance as yf

# Crear objeto ticker para Tesla
tesla = yf.Ticker("TSLA")

# Descargar datos históricos completos
tesla_hist = tesla.history(period="max")
# Mostrar las primeras filas para verificari
print(tesla_hist.head())
