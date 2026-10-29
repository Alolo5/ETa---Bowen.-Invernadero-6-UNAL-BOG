# Estimación de Evapotranspiración Real (ETa) mediante Razón de Bowen (BREB) en Invernadero

Este repositorio contiene el pipeline de *procesamiento agrometeorológico* para la estimación y análisis de la Evapotranspiración Real (ETa) mediante el método del Balance de Energía y Razón de Bowen (BREB). El proyecto está desarrollado como parte del trabajo de tesis de maestría en ciencias - meteorología, realizado en un entorno de invernadero ubicado en Bogotá, Colombia (Universidad Nacional de Colombia - Sede Bogotá).


<p align="center">
            <img width="400" height="299" alt="Gemini_Generated_Image_ad3h2ad3h2ad3h2a" src="https://github.com/user-attachments/assets/e2eab0fd-3910-4a6b-9872-3719f143e5eb" />
</p>

---

## Contexto y Ubicación

- **Ubicación:** Invernadero No6 de la Facultad de Ciencias Agrarias, UNAL Sede Bogotá.
- **Elevación:** $\approx 2600$ msnm.
- **Presión Atmosférica Promedio ($P$):** $\approx 75,4$ kPa.
- **Instrumentación:** Datalogger Meter ZL6 (temperatura, humedad relativa, radiación solar, presión atmosférica) y psicrómetros EL-USB-2-LCD (temperatura, humedad relativa) a diferentes alturas.

---

## Flujo de Procesamiento Computacional (Pipeline)

El análisis automatizado en Python ejecuta las siguientes etapas sobre las series temporales:

<p align="center">
            <img width="264" height="1186" alt="Blank diagram - Page 1" src="https://github.com/user-attachments/assets/3e3ebf60-64ff-4266-8068-7cc500b72b15" />
</p>
