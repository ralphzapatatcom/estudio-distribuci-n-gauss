import numpy as np
import matplotlib.pyplot as plt

def estudiar_gauss(media, desviacion, puntos=1000):
    # 1. Crear un rango de valores en el eje X
    # Generamos valores desde (media - 4*sigma) hasta (media + 4*sigma)
    x = np.linspace(media - 4*desviacion, media + 4*desviacion, puntos)

    # 2. Calcular la Campana de Gauss usando la fórmula matemática
    # NumPy nos permite hacer esto de forma vectorizada (muy rápido)
    y = (1 / (desviacion * np.sqrt(2 * np.pi))) * \
        np.exp(-0.5 * ((x - media) / desviacion)**2)

    # 3. Configurar la visualización
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'Media={media}, σ={desviacion}', color='#2c3e50', linewidth=2)
    
    # Rellenar el área bajo la curva para que se vea mejor
    plt.fill_between(x, y, color='skyblue', alpha=0.4)

    # Añadir detalles estéticos
    plt.title('Estudio de la Distribución Normal (Campana de Gauss)', fontsize=14)
    plt.xlabel('Valores', fontsize=12)
    plt.ylabel('Densidad de Probabilidad', fontsize=12)
    plt.axvline(media, color='red', linestyle='--', label='Media (Centro)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Ejecutar el estudio con una media de 0 y desviación de 1 (Normal Estándar)
estudiar_gauss(media=0, desviacion=1)