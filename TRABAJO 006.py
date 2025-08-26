# Pregunta 6 - Cuadro de mando de acciones de GameStop: Graficar datos de acciones

import yfinance as yf
import matplotlib.pyplot as plt

# Descargar datos históricos de GameStop
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")

def make_graph(data, title):
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data['Close'], label='Precio de cierre')
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.show()

# Usar la función para graficar GameStop
make_graph(gme_data, 'Precio de cierre histórico de acciones de GameStop')
