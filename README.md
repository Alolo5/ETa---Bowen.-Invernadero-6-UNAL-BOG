# Estimación de Evapotranspiración Real (ETa) mediante Razón de Bowen (BREB) en Invernadero

Este repositorio contiene el pipeline de procesamiento agrometeorológico para la estimación y análisis de la Evapotranspiración Real (ETa) mediante el método del Balance de Energía y Razón de Bowen (BREB). El proyecto está desarrollado como parte del trabajo de tesis de maestría, realizado en un entorno de invernadero ubicado en Bogotá, Colombia (Universidad Nacional de Colombia - Sede Bogotá).

---

## 📌 Contexto y Ubicación

* **Ubicación:** Invernadero de Docencia e Investigación (Invernadero 6), UNAL Sede Bogotá.
* **Elevación:** $2600$ msnm.
* **Presión Atmosférica Promedio ($P$):** $\approx 75,4$ kPa.
* **Instrumentación:** Datalogger Meter ZL6 (radiación solar, humedad de suelo) y psicrómetros con dataloggers EL-USB-2-LCD.

---

## ⚙️ Flujo de Procesamiento Computacional (Pipeline)

El análisis automatizado en Python ejecuta las siguientes etapas sobre las series temporales:

```text
[1. Datos Crudos (.txt/.xlsx)] ──► Carga de series temporales ZL6 y EL-USB-2-LCD
            │
            ▼
[2. Control y Sincronización] ─► Normalización (pd.to_numeric) y alineación temporal (pd.merge_asof)
            │
            ▼
[3. Resampling Temporal] ───────► Agregación regular a 30 min ('.resample('30min').mean()')
            │
            ▼
[4. Cálculos Psicrométricos] ───► Presión de vapor e_s(T), e_a(T, HR), VPD y gradientes (ΔT, Δe)
            │
            ▼
[5. Radiación Neta y Flujo G] ──► Estimación de R_n (FAO-56) y G en función de R_n (c_día = 0.15, c_noche = 0.50)
            │
            ▼
[6. QA/QC Razón de Bowen (β)] ──► Exclusión de la singularidad (-1.25 < β < -0.75) y umbrales físicos
            │
            ▼
[7. Partición de Flujos] ───────► Despeje de Calor Latente (LE) y Calor Sensible (H)
            │
            ▼
[8. Conversión a ETa] ──────────► Transformación de W/m² a mm/intervalo vía λ y Δt (30 min)
            │
            ▼
[9. Agregación Diaria] ─────────► Integración de la lámina acumulada (.resample('1D').sum())
