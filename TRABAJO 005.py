# Pregunta 5 - Cuadro de mando de acciones de Tesla: Graficar datos de acciones

import yfinance as yf
import matplotlib.pyplot as plt

# Descargar datos históricos de Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

def make_graph(data, title):
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data['Close'], label='Precio de cierre')
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.show()

# Usar la función para graficar Tesla
make_graph(tesla_data, 'Precio de cierre histórico de acciones de Tesla')