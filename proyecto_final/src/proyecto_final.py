import requests
import json
import pandas as pd

# el archivo api_key no está porque fue añadido al .gitignore
from .api_key import API_KEY

proyectos = {"Baraya Principal": 603,
             "Baraya Respaldo": 604,
             "Valle de Gandalf Principal": 609,
             "Valle de Gandalf Respaldo": 610,
             "Cañahuate Principal": 606,
             "Cañahuate Respaldo": 607,
             "Baraya Principal": 603,
             "Baraya Respaldo": 604,
             "Perijá Principal": 848,
             "Perijá Respaldo": 849,
             "La Paz Vallenata Principal": 845,
             "La Paz Vallenata Respaldo": 846}

'''r = requests.get(url=f"https://gaia.quoia.energy/api/node/{
                 ID}/measurements?init_date=2024-10-31T00:00:00Z-0500&end_date=2024-10-31T12:00:00Z-0500&vars=v,ap", headers={"Authorization": f"Token {API_KEY}"})'''

api_response = b'[{"time":"2024-10-30T14:00:02-05:00","node_id":845,"vp1":7640.496499999999,"vp2":7421.387,"vp3":7409.9445000000005,"app1":-323762.26,"app2":-315569.2,"app3":-314031.65},{"time":"2024-10-30T14:15:02-05:00","node_id":845,"vp1":7740.580999999999,"vp2":7517.412000000001,"vp3":7507.844,"app1":-320941.425,"app2":-312839.79,"app3":-312643.715}]'

data = json.loads(api_response)

df = pd.DataFrame(data)

df['time'] = pd.to_datetime(df['time'])

print(df.head())
