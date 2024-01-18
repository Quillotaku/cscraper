# cscraper
Scraper de las peliculas de Cinesa.

# Pasos previos
1. Instalar los requirements `pip3 install -r requirements.txt`
2. Conseguir los headers para realizar la petición. 
   1. Para conseguirlos, ir a la página de Cinesa
   2. Abrir la consola de comandos, en la pestaña de **Network**
   3. Dentro de esta misma seleccionar **XHR**.
   4. Dentro del listado de peticiones que se han realizado, buscar una petición GET que contenga algo similar a `first?siteIds=138` o `2024-01-19?siteIds=138`.
   5. Click derecho y copiar el valor de los request headers.
   6. Sustituir o rellenar con esos valores el fichero de headers.json. (Cambian, puede que tengas que refrescarlos para usar el script de un dia a otro)

# Uso
- `python3 cscraper.py CINE FECHA`
- `CINE`:
  - equinoccio
  - heron-city-las-rozas
  - intu-xanadu
  - la-gavia
  - la-moraleja
  - las-rosas
  - manoteras
  - mendez-alvaro
  - nassica
  - oasiz
  - parquesur
  - plaza-lorcana-2
  - proyecciones
  - principe-pio
- `FECHA`: FORMATO: YYYY-MM-DD

Genera un CSV con el nombre de CINE_FECHA.csv.
El cual tiene el nombre de la película, la duración y la sesión. Para usar con con el otro script `cplanner`.
