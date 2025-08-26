# Pregunta 4 - Extracción de datos de ingresos de GameStop usando yfinance

import yfinance as yf

gme = yf.Ticker("GME")

# Obtener el estado de ingresos (income statement)
income_stmt = gme.financials

# Mostrar los primeros datos
print(income_stmt.head())