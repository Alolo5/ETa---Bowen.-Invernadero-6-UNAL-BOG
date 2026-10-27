import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de gráficas
sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
plt.rcParams['figure.dpi'] = 300 
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'DejaVu Sans'

os.makedirs("Resultados_Estadisticos", exist_ok=True)
os.makedirs("Graficas_Tesis", exist_ok=True)

archivos_entrada = {
    "Z6": {"ruta": "z6-13472_acotado_01Abr_14Jul.xlsx", "tipo": "excel"},
    "EL_1": {"ruta": "datos_psicrometrico1_completos.txt", "tipo": "txt"}, 
    "EL_6": {"ruta": "datos_psicrometrico2_completos.txt", "tipo": "txt"} 
}

def generar_analisis(df, nombre_sensor):
    estadisticas = df.describe().T
    estadisticas['Asimetria (Skewness)'] = df.skew()
    estadisticas['Curtosis (Kurtosis)'] = df.kurtosis()
    estadisticas.to_excel(f"Resultados_Estadisticos/Resumen_{nombre_sensor}.xlsx")

    variables = [col for col in df.columns if df[col].dtype in ['float64', 'int64'] 
                 and col not in ['EL 1', 'EL 6', 'Serial Number']]

    for var in variables:
        nombre_limpio = str(var)[:20].replace('/', '_').replace('°', 'deg')

        # A. Serie de Tiempo
        plt.figure(figsize=(12, 4))
        sns.lineplot(data=df, x=df.index, y=var, linewidth=0.8, color="#2c3e50")
        plt.title(f"Serie de Tiempo ({nombre_sensor}): {var}")
        plt.xlabel("Fecha")
        plt.ylabel(var)
        plt.tight_layout()
        plt.savefig(f"Graficas_Tesis/Serie_{nombre_sensor}_{nombre_limpio}.png")
        plt.close()

        # B. Ciclo Diurno
        ciclo_diurno = df.groupby(df.index.hour)[var].agg(['mean', 'std'])
        plt.figure(figsize=(8, 5))
        plt.plot(ciclo_diurno.index, ciclo_diurno['mean'], label='Promedio', color="#e74c3c", linewidth=2)
        plt.fill_between(ciclo_diurno.index, 
                         ciclo_diurno['mean'] - ciclo_diurno['std'], 
                         ciclo_diurno['mean'] + ciclo_diurno['std'], 
                         color="#e74c3c", alpha=0.2, label='±1 Desv. Estándar')
        plt.title(f"Ciclo Diurno ({nombre_sensor}): {var}")
        plt.xlabel("Hora")
        plt.xticks(range(0, 24, 2))
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"Graficas_Tesis/Diurno_{nombre_sensor}_{nombre_limpio}.png")
        plt.close()

        # C. Boxplots Mensuales
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=df.index.month, y=df[var], palette="Blues", legend=False)
        plt.title(f"Distribución Mensual ({nombre_sensor}): {var}")
        plt.xlabel("Mes")
        plt.tight_layout()
        plt.savefig(f"Graficas_Tesis/Boxplot_{nombre_sensor}_{nombre_limpio}.png")
        plt.close()

for sensor, info in archivos_entrada.items():
    try:
        if info["tipo"] == "excel":
            df_raw = pd.read_excel(info["ruta"])
            nombres = df_raw.iloc[0].astype(str) + " (" + df_raw.iloc[1].astype(str) + ")"
            df = df_raw.iloc[2:].copy()
            df.columns = nombres
            df.rename(columns={df.columns[0]: 'Time'}, inplace=True)
        else:
            df = pd.read_csv(info["ruta"], encoding='utf-8-sig') 
        
        # Parseo de fechas específico por sensor
        if sensor == "Z6":
            df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%Y %H:%M', errors='coerce')
        else:
            df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
            
        # Eliminar posibles filas donde la fecha no se pudo convertir (NaT)
        df.dropna(subset=['Time'], inplace=True)
        
        df.set_index('Time', inplace=True)
        df = df.apply(pd.to_numeric, errors='coerce')
        
        generar_analisis(df, sensor)
        print(f"✅ Análisis de {sensor} completado.")
        
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo para {sensor} en la ruta: {info['ruta']}")