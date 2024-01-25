import os
import pandas as pd
import matplotlib.pyplot as plt

# Ruta completa del archivo Excel
#En esta parte debe cambiar la ruta a donde tenga el archivo, la ruta está puesta: Desktop/TESIS PROYECTO DE GRADO/ Datos Performance FI/ Datos 3.xlsx
#Para cambiarla solo cambie el nombre de las carpetas para que coincida con el que tenga.
ruta_excel = os.path.join(os.path.expanduser("~"), "Desktop", "TESIS PROYECTO DE GRADO", "Datos Performance FI", "Datos 3.xlsx") 

# Cargar datos desde el archivo Excel
df = pd.read_excel(ruta_excel, header=None, skiprows=2, usecols=[3], names=['Datos'])

# Rellenar valores "n/a" con 0
df['Datos'].replace("n/a", 0, inplace=True)

# Convertir a tipo numérico
df['Datos'] = pd.to_numeric(df['Datos'], errors='coerce')

# Agrupar datos por mes (cada mes tiene 30 días para simplificar)
df['Fecha'] = pd.date_range(start='1/1/2022', periods=len(df), freq='5T')
df['Mes'] = df['Fecha'].dt.month
# Obtener abreviaturas de los meses
abreviaturas_meses = df['Fecha'].dt.strftime('%b').unique()

# Crear un gráfico de cajas y bigotes por mes
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['Mes'] == mes]['Datos'].dropna().tolist() for mes in range(1, 13)], labels=abreviaturas_meses)
plt.title('Gráfico de Producción Fotovoltaica (Wh)')
plt.xlabel('Mes')
plt.ylabel('Producción Fotovoltaica')

# Mostrar el gráfico
plt.show()