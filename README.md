<div style="width: 100%; clear: both;">
<div style="float: left; width: 50%;">
<img src="https://www.uoc.edu/portal/system/modules/edu.uoc.presentations/resources/img/branding/logo-uoc-default.png_1618809817.png", align="left">
</div>
<div style="float: right; width: 50%;">
<p style="margin: 0; padding-top: 22px; text-align:right;">M2.879 · Trabajo Fin de Máster · TFM</p>
<p style="margin: 0; text-align:right;">2023-2 · Máster universitario en Ciencia de datos (Data science)</p>
<p style="margin: 0; text-align:right; padding-button: 100px;">Estudios de Informática, Multimedia y Telecomunicación</p>
</div>
</div>
<div style="width:100%;">&nbsp;</div>


# TFM UOC (Actualmente en ejecución)

<div class="alert alert-block alert-info">
<strong>Nombre y apellidos: Pablo Martínez Pavón</strong>
</div>

## Introducción

Este proyecto busca llevar la detección de anomalías y mitigación de “concept drift” al entorno industrial, ya que con el auge de la Industria 4.0, cada vez hay un mayor volumen de datos que se generan en tiempo real procedentes de máquinas y procesos. 
Así, se diseñará, desarrollará e implementará un sistema que sea capaz de adquirir Data Streams (lectura incremental de datos continuos en tiempo real), aprender automáticamente a detectar anomalías y poder mitigar el impacto del “concept drift” si se produjese.
Con ello, se busca dotar de herramientas al personal de empresas industriales de herramientas que permitan prevenir fallos y optimizar el funcionamiento de sus equipos e instalaciones.

## Descripción del contenido: 
Actualmente, este repositorio contiene:
  - main.py: desde donde se pueden ejecutar todas las funciones desarrolladas.
  - setupInicial.py: creación del sistema de carpetas.
  - reloxo.py: contiene una clase para controlar el tiempo de ejecución de las funciones.
  - githubInteraccion.py: empleando la API de GitHub, se encarga de listar los archivos de un repositorio y descargarlos.
  - transformarEDA.py: se encarga de todas las operaciones relacionadas con el tratamiento de los datos y el Análisis Exploratorio.
  - pcaLDA.py: técnicas de reducción de dimensionalidad PCA y LDA.
  - afinadoHiperparametros: se hace un primer afinado de los modelos a emplear (regresión logística (RL), Naive-Bayes (NB) y árbol de decisión (DT).
  - streamRiver.py: simula el stream de datos e implementa los diferentes modelos y métodos de data streaming.
  - plotPerformance.py: permite hacer un gráfico dinámico para controlar el rendimiento de los modelos en streaming en base a una de las métricas.

## Dataset Empleado: 
Para el presente TFM, se ha empleado el dataset Time-series Industrial Anomaly dataset (TiNA), un conjunto de datos de series temporales para detección de anomalías dentro de un contexto industrial. El conjunto de datos contiene información de sensórica de una máquina de minería perteneciente a la compañía ArcelorMittal.

@misc{tina_dasci_arcelor
  title={Time-series Industrial Anomaly dataset},
  authors={Ignacio Aguilera-Martos and David López and Marta García-Barzana and Julián Luengo and Francisco Herrera},
  year={2022},
  URL={https://github.com/ari-dasci/OD-TINA}
}

## Recursos Empleados: 
El lenguaje empleado es Python junto con la librería River para realizar ML online.

## Enlaces:
1. [UOC](https://www.uoc.edu/portal/es/index.html)
2. [TINA dataset](https://dasci.es/transferencia/open-data/tina-dataset/)
3. [River library](https://riverml.xyz/latest/)

