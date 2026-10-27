import pandas as pd

# 1. Agregamos encoding='latin1' para que pueda leer correctamente el símbolo de grados (°)
df1 = pd.read_csv("EL 1.1.txt", encoding='latin1')
df2 = pd.read_csv("EL 1.2.txt", encoding='latin1')
df3 = pd.read_csv("EL 6.1.txt", encoding='latin1')
df4 = pd.read_csv("EL 6.2.txt", encoding='latin1') # Asegúrate de poner el nombre exacto de tu segundo archivo

# 2. Unir ambos archivos verticalmente
df_combinado1 = pd.concat([df1, df2], ignore_index=True)
df_combinado2 = pd.concat([df3, df4], ignore_index=True)

# 3. Actualizar la columna numerativa "EL 1" para que mantenga una secuencia continua
df_combinado1['EL 1'] = range(1, len(df_combinado1) + 1)
df_combinado2['EL 6'] = range(1, len(df_combinado2) + 1)

# 4. Guardar el archivo final
# Usamos utf-8-sig al exportar para que, si lo abres en Excel u otro programa, reconozca el símbolo de grados sin problemas
df_combinado1.to_csv("datos_psicrometrico1_completos.txt", index=False, encoding='utf-8-sig')
df_combinado2.to_csv("datos_psicrometrico2_completos.txt", index=False, encoding='utf-8-sig')

print("¡Archivos unidos y guardados con éxito!")