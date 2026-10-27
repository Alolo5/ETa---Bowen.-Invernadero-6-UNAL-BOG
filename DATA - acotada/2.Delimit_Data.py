import pandas as pd

# 1. Cargar el archivo combinado generado en el paso anterior
# Utilizamos utf-8-sig porque así lo guardamos en el código pasado
df1 = pd.read_csv("datos_psicrometrico1_completos.txt", encoding='utf-8-sig')
df2 = pd.read_csv("datos_psicrometrico2_completos.txt", encoding='utf-8-sig')

# 2. Convertir la columna 'Time' a formato datetime de pandas
# dayfirst=True le indica a pandas que el formato original asume primero el día (DD/MM/YYYY)
df1['Time'] = pd.to_datetime(df1['Time'], dayfirst=True)
df2['Time'] = pd.to_datetime(df2['Time'], dayfirst=True)

# 3. Definir las fechas de inicio y fin (usamos formato AAAA-MM-DD para mayor seguridad)
# Esta fecha corresponde a una situación en la que no estaba sembrado aún el pepino
# La fecha real de siembra de las plántulas es el 2026-04-08 pero ya estaba preparado el terreno para siembra
fecha_inicio = '2026-04-01'
# Agregamos la hora 23:59:59 para asegurarnos de incluir todos los datos que ocurrieron durante el último día (14 de julio)
# La fecha real de la segunda cosecha es el 2026-07-10
fecha_fin = '2026-07-14 23:59:59' 

# 4. Crear una condición (máscara) para filtrar los datos
mascara = (df1['Time'] >= fecha_inicio) & (df1['Time'] <= fecha_fin)

# 5. Aplicar el filtro para obtener los datos acotados
df_acotado1 = df1.loc[mascara].copy()
df_acotado2 = df1.loc[mascara].copy()

# 6. (Opcional) Re-numerar la columna 'EL 1' para que el nuevo archivo comience desde el número 1
df_acotado1['EL 1'] = range(1, len(df_acotado1) + 1)
df_acotado2['EL 6'] = range(1, len(df_acotado2) + 1)

# 7. Convertir la columna 'Time' nuevamente a un formato de texto limpio antes de guardar (opcional pero recomendado)
df_acotado1['Time'] = df_acotado1['Time'].dt.strftime('%d/%m/%Y %H:%M:%S')
df_acotado2['Time'] = df_acotado2['Time'].dt.strftime('%d/%m/%Y %H:%M:%S')

# 8. Guardar los datos filtrados en un nuevo archivo
nombre_archivo_salida1 = "datos_acotados_01Abr_14Jul_EL1.txt"
nombre_archivo_salida2 = "datos_acotados_01Abr_14Jul_EL6.txt"
df_acotado1.to_csv(nombre_archivo_salida1, index=False, encoding='utf-8-sig')
df_acotado2.to_csv(nombre_archivo_salida2, index=False, encoding='utf-8-sig')

print(f"¡Proceso completado! Se guardaron {len(df_acotado1)} registros en el archivo '{nombre_archivo_salida1}' y {len(df_acotado2)} en '{nombre_archivo_salida2}'.")