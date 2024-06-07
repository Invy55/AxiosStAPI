from AxiosStAPI.utils.rc4 import rc4
from AxiosStAPI.utils.services import services
from AxiosStAPI.AxiosStAPI import AxiosStAPI
from os import getenv
from dotenv import load_dotenv
load_dotenv()

api = AxiosStAPI()
print(api.retrieveAPPCustomerInformationByString(services.RetrieveAPPCustomerInformationByString.SSEARCH, query="20090"))

api.login(getenv("SCUOLA"), getenv("USER"), getenv("PASSWORD"))
print(api.retrieveDataInformation(services.RetrieveDataInformation.TIMELINE, giorno="28/02/2024"))
print(api.retrieveDataInformation(services.RetrieveDataInformation.ORARIO))