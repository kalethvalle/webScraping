# Project Tecnical test Web scraping
This project is developed to share the technical test in the company [tusdatos](https://www.tusdatos.co/).
### Requirements:
#### Extract data from page using method scraping
- Extraer listado de procesos que genera la búsqueda.
- Distinguir entre los procesos de demandado y demandante. 
- Extraer el detalle para cada proceso.
- Extraer todas las actuaciones judiciales de cada proceso.
- Guardar toda la información de los procesos en base de datos o un archivo (csv, json, etc).
#### Create API REST using library Flask
- Endpoints que puedan exponer la data
- Usar un sistema de autorización y autenticación (el de preferencia)
- Contener una documentación del uso del API.

## Install Dependencies
To correctly run the scraping method you must download the chromium driver [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#stable).
- `python3 -m venv ENV_DIR`
- `source ./ENV_DIR/bin/activate`
- `cd from folder webScraping`
- `pip install -r requirements.txt`

## Execute scraping page
- `python ./scraping_page/main.py`

## Execute API REST
- `python ./app.py`

### Observations
The api has 3 requests
1. `/login`: Authentication
2. `/api/process`: get all saved processes
3. `/api/docs/`: shows swagger documentation
