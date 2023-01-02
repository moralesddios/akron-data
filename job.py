from data.extract import extract
from data.load import load


#### ----- Extracción ----- ####
df = extract("puntos-de-acceso-wifi.csv")

#### ----- Carga ----- ####
load(df, "access_points")
