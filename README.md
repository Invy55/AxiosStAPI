# AxiosStAPI
Wrapper in python per usufruire delle API di RE studenti di Axios Italia

## Getting started

### Logging in

```python
from AxiosStAPI.AxiosStAPI import AxiosStAPI

api = AxiosStAPI()
api.login(SCUOLA, USER, PASSWORD)
```

### Retrieving informations:

#### Senza Login

```python
# Ricerca delle scuole con una stringa che può essere nome, cap, via, ecc
api.retrieveAPPCustomerInformationByString(services.RetrieveAPPCustomerInformationByString.SSEARCH, query="20090")
#[{'fsIntitolazione': 'MICROTECH', 'fsNome': 'SRL', 'fsCF': '06830500960', 'fsCap': '20090', 'fsRegione': 'LOMBARDIA', 'fsCitta': 'BUCCINASCO', 'fsProvincia': 'MI'}, ...]
```

#### Con Login
Per la lista di tutti i servizi disponibili consulta [services.py](https://github.com/Invy55/AxiosStAPI/blob/main/AxiosStAPI/utils/services.py) e controlla l'implementazione in [AxiosStAPI.py](https://github.com/Invy55/AxiosStAPI/blob/main/AxiosStAPI/AxiosStAPI.py#L115-L130)
```python
# Ottieni avvenimenti di una giornata
api.retrieveDataInformation(services.RetrieveDataInformation.TIMELINE, giorno="28/02/2024")
#[{'idAlunno': '####', 'today': [{'id': '####', 'type': 'L', 'data': '28/02/2024', 'subType': '', 'ora': '', 'oralez': '2-3', 'desc': {'title': '', 'subtitle': 'SCIENZE NATURALI', 'notes': 'interrogazioni'}}, ...], 'totali': {'assenze_da_giust': '0', 'assenze_totali': '18', 'ritardi_da_giust': '0', 'ritardi_totali': '6', 'uscite_da_giust': '0', 'uscite_totali': '9'}, 'media_a': '8,51'}]
```

## Docs
Work in progress.