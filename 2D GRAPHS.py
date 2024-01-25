import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener la ruta al escritorio
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Construir la ruta completa a la carpeta 
proyecto_python_path = os.path.join(desktop_path, "TESIS PROYECTO DE GRADO")

# Construir las rutas completas a los archivos Excel
excel_file1 = os.path.join(proyecto_python_path, "Datos Performance FI", "Datos horarios 2023.xlsx")
excel_file2 = os.path.join(proyecto_python_path, "Datos Performance FI", "Datos 3.xlsx")


# Leer los datos de los tres archivos Excel, saltando la primera fila
df1 = pd.read_excel(excel_file1, usecols=[1], header=None, names=['Columna_2'], skiprows=2).fillna(0)
df2 = pd.read_excel(excel_file2, usecols=[1], header=None, names=['Columna_2'], skiprows=2).fillna(0)


# Asegurar que todos los DataFrames tengan la misma longitud
max_len = max(len(df1), len(df2))
df1 = df1.reindex(range(max_len)).fillna(0)
df2 = df2.reindex(range(max_len)).fillna(0)

# Convertir el índice y las columnas a matrices de NumPy
index1 = df1.index.values
values1 = df1['Columna_2'].astype(float).values

index2 = df2.index.values
values2 = df2['Columna_2'].astype(float).values


# Crear un DataFrame con las fechas y valores
df_dates_values = pd.DataFrame({'Fecha': pd.to_datetime(index1 * 5, unit='m', origin='2023-01-01'),
                                'Valor1': values1,
                                'Valor2': values2})

# Agrupar por mes y calcular el promedio
df_monthly_mean = df_dates_values.resample('M', on='Fecha').mean()

# Crear una figura para la gráfica 2D
plt.figure()

# Convertir el índice de df_monthly_mean a un array de NumPy
index_array = df_monthly_mean.index.to_numpy()

# Graficar los datos promedio de cada archivo con colores diferentes y líneas interconectadas
plt.plot(index_array, df_monthly_mean['Valor1'].values, label='Archivo 1', color='blue', marker='o', linestyle='-')
plt.plot(index_array, df_monthly_mean['Valor2'].values, label='Archivo 2', color='green', marker='o', linestyle='-')


# Configurar etiquetas y leyenda
plt.xlabel('Fecha (Mes)')
plt.ylabel('Valor Columna 2 (Promedio Mensual)')
plt.legend()

# Mostrar la gráfica
plt.show()
