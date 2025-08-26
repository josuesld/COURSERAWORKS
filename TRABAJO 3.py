# Pregunta 3 - Extracción de datos de acciones de GameStop utilizando yfinance

import yfinance as yf

# Descargar datos históricos de GameStop
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")

# Resetear el índice para que la fecha sea una columna normal
gme_data_reset = gme_data.reset_index()

# Guardar el DataFrame en un archivo CSV
gme_data_reset.to_csv("gme_data.csv", index=False)

# Mostrar las primeras 5 filas
print(gme_data_reset.head())

