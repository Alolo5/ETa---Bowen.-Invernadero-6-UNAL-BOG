import pandas as pd

# 1. Cargar el archivo Excel especificando la hoja donde están los registros
archivo_entrada = "z6-13472 07sept.26-1105.xlsx"
df = pd.read_excel(archivo_entrada, sheet_name='Processed Data Config 1')

# 2. Extraer las dos primeras filas (nombres de sensores y unidades) para no perderlas
df_encabezados = df.iloc[:2].copy()
df_datos = df.iloc[2:].copy()

# 3. Convertir la primera columna (que actúa como índice de tiempo) a formato datetime
columna_tiempo = df.columns[0] 
df_datos[columna_tiempo] = pd.to_datetime(df_datos[columna_tiempo])

# 4. Establecer las condiciones de filtrado
fecha_inicio = '2026-04-01'
fecha_fin = '2026-07-14 23:59:59'

# 5. Filtrar estrictamente la sección de datos
mascara = (df_datos[columna_tiempo] >= fecha_inicio) & (df_datos[columna_tiempo] <= fecha_fin)
df_datos_acotados = df_datos.loc[mascara].copy()

# 6. Devolver el tiempo a su formato de texto original (AAAA-MM-DD HH:MM:SS)
df_datos_acotados[columna_tiempo] = df_datos_acotados[columna_tiempo].dt.strftime('%Y-%m-%d %H:%M:%S')

# 7. Unir nuevamente los encabezados con los datos ya filtrados
df_final = pd.concat([df_encabezados, df_datos_acotados], ignore_index=True)

# 8. (Opcional) Actualizar la celda que cuenta la cantidad de registros ("Records: XXXX")
df_final.iat[0, 0] = f"Records: {len(df_datos_acotados)}"

# 9. Guardar los datos en un nuevo archivo Excel
nombre_salida = "z6-13472_acotado_01Abr_14Jul.xlsx"
df_final.to_excel(nombre_salida, index=False)

print(f"¡Listo! Se guardaron {len(df_datos_acotados)} registros en '{nombre_salida}'.")