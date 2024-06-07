from AxiosStAPI.utils.services import services
from AxiosStAPI.AxiosStAPI import AxiosStAPI
from os import getenv
from dotenv import load_dotenv
load_dotenv()

api = AxiosStAPI()
# Ricerca delle scuole con una stringa che può essere nome, cap, via, ecc
print(api.retrieveAPPCustomerInformationByString(services.RetrieveAPPCustomerInformationByString.SSEARCH, query="20090"))

api.login(getenv("SCUOLA"), getenv("USER"), getenv("PASSWORD"))
print(api.retrieveDataInformation(services.RetrieveDataInformation.TIMELINE, giorno="28/02/2024"))
print(api.retrieveDataInformation(services.RetrieveDataInformation.ORARIO))