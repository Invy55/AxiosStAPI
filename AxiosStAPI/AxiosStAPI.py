import requests
import json
from .utils import HEADERS, VENDOR_ALU, RC4_KEY, WSALU
from .utils.rc4 import rc4
from .utils.services import services
from datetime import datetime

#TODO: Raise exceptions per ogni possibile errore di axios invece dei return False

class AxiosStAPI():
    """
    Classe che rappresenta l'interfaccia API con Axios per il registro cloud.
    ### Attributi
    ----------
    `session`: str = None
        Stringa della sessione ottenute da axios [es: ddf1944c-6452-490e-b326-74fd6ca6dc6a]
    `s`: requests.Session
        Sessione di requests con le headers settate nell'__init__.py
    ### Metodi
    -------
    login(user: str, password: str)
        Logga l'utente, imposta la sessione nella classe e restituisce la risposta del server
    """
    def __init__(self, session: str = None, headers: dict = None) -> None:
        """
        ### Parametri
        ----------
        `session`: str = None
            Stringa della sessione ottenute da axios [es: ddf1944c-6452-490e-b326-74fd6ca6dc6a]
        `headers`: dict = None
            Headers da utilizzare per le richieste, default in utils/__init__.py
        """
        self._session = session
        self.s = requests.Session()
        if headers:
            self.s.headers
        else:
            self.s.headers = HEADERS
        self._rc4 = rc4(RC4_KEY)
        self._services = services
        self._idAlunno = False # da ottenere con retrieveDataInformation

    def login(self, scuola: str, user: str, password: str) -> dict|list:
        """
        Metodo per loggarsi, imposta la sessione e la scuola nella classe e restituisce la risposta del server
        ### Parametri
        ----------
        `scuola`: str
            Codice fiscale della scuola
        `user`: str
            Username dell'utente, solitamente numerico, ma ogni tanto funziona anche la mail (?)
        `password`: str
            Password dell'utente
        ### Returns
        -------
        dict|list
            Risposta del server
        """
        data = {
            "sCodiceFiscale": scuola,
            "sUserName": user,
            "sPassword": password,
            "sAppName":"ALU_APP",
            "sVendorToken": VENDOR_ALU
        }
        params = {"json": 
                  self._rc4.encrypt(json.dumps(data), 2)
            }
        r = self.s.get(f"{WSALU}/Login2?json={params['json']}")
        if r.status_code == 200:
            resp = self._rc4.decrypt(r.text)
            try:
                resp = json.loads(resp)
            except json.JSONDecodeError:
                return False
            self._session = resp.get("response", {}).get("usersession", False)
            self._scuola = scuola
            if not self._session: # Se non c'è la sessione, ritorna False
                return False
            return resp.get("response", {})
        else:
            return False

    def _retrieveInformation(self, data: dict, endpoint: str) -> dict:
        """
        Metodo di base per le richieste a `RetrieveDataInformation`, `RetrieveAPPCustomerInformationByString`, ecc, usare i wrapper `self.retrieveDataInformation`, `self.retrieveAPPCustomerInformationByString`, ecc
        ### Parametri
        ----------
        `data`: dict
            Dati da inviare al server
        `endpoint`: str
            Endpoint a cui inviare i dati
        ### Returns
        -------
        dict
            Risposta del server
        """
        params = {"json": 
                  self._rc4.encrypt(json.dumps(data))
            }
        r = self.s.get(f"{WSALU}/{endpoint}?json={params['json']}")
        if r.status_code == 200:
            resp = self._rc4.decrypt(r.text)
            try:
                resp = json.loads(resp)
            except json.JSONDecodeError:
                return False
            return resp.get("response", {})
        else:
            return False
    
    def retrieveDataInformation(self, service, **kwargs) -> dict|list:
        """ #TODO fix markdown dei ### Parametri
        Metodo per ottenere informazioni dalle api. Servizi disponibili:
        - `STRUCTURAL`: Ottiene la struttura delle risposte delle api
        - `TIMELINE` (args: giorno): Ottiene gli eventi del giorno specificato, default oggi
        - `STUDENTI`: Ottiene le informazioni sullo studente
        - `COMUNICAZIONI` (args: idAlunno): Ottiene le comunicazioni
        - `COMPITI` (args: idAlunno): Ottiene i compiti
        - `ORARIO` (args: idAlunno): Ottiene l'orario
        - `MATERIALE` (args: idAlunno): Ottiene il materiale
        - `ARGOMENTI` (args: idAlunno): Ottiene gli argomenti
        - `VOTI` (args: idAlunno): Ottiene i voti
        - `ASSENZE` (args: idAlunno): Ottiene le assenze
        - `NOTE` (args: idAlunno): Ottiene le note
        - `AUTORIZZAZIONI` (args: idAlunno): Ottiene le autorizzazioni
        - `PAGELLA` (args: idAlunno): Ottiene la pagella
        - `CURRICULUM` (args: idAlunno): Ottiene il curriculum
        - `PAGOSCUOLA` (args: idAlunno): Ottiene i pagamenti scolastici
        - `DOCUMENTI` (args: idAlunno): Ottiene i documenti
        ### Parametri
        ----------
        `service`: str
            Servizio da richiedere
        `**kwargs`
            Parametri aggiuntivi da passare al servizio (vedi sopra)
            `giorno`: str
                Data nel formato "%d/%m/%Y", es. 18/03/2024
            `idalunno`: str
                Id dell'alunno, di default la libreria lo ottiene in automatico
        ### Returns
        -------
        dict|list
            Risposta del server
        """
        services = self._services.RetrieveDataInformation
        if service not in services.__dict__.values():
            return False
        base = {"sCodiceFiscale": self._scuola,
                "sSessionGuid": self._session,
                "sCommandJSON": {
                    "sApplication": "FAM",
                    "sService": service
                },
                "sVendorToken": VENDOR_ALU
            }
        if service == services.STRUCTURAL:
            pass # Non è necessaria nessuna aggiunta
        elif service == services.TIMELINE:
            giorno = kwargs.get("giorno", datetime.now().strftime("%d/%m/%Y")) # giorno di default oggi
            base["sCommandJSON"]["data"] = {"dataGiorno": giorno}
        elif service == services.STUDENTI:
            base["sCommandJSON"]["data"] = {"appName": "ALU_APP"}
        else:
            idAlunno = kwargs.get("idalunno", self.getIdAlunno())
            base["sCommandJSON"]["data"] = {"alunnoId": idAlunno}
        
        return self._retrieveInformation(base, "RetrieveDataInformation")

    def retrieveAPPCustomerInformationByString(self, service, **kwargs) -> dict|list:
        """ #TODO fix markdown dei ### Parametri
        Metodo per ottenere informazioni dalle api. Servizi disponibili:
        - `SSEARCH`: Ottiene la lista delle scuole da CAP, nome, ecc
        ### Parametri
        ----------
        `**kwargs`
            Parametri da passare al servizio (vedi sopra)
            `query`: str
                Query di ricerca
        ### Returns
        -------
        dict|list
            Risposta del server
        """
        services = self._services.RetrieveAPPCustomerInformationByString
        if service not in services.__dict__.values():
            return False
        base = {
                "sVendorToken": VENDOR_ALU
            }
        if service == services.SSEARCH:
            base["sSearch"] = kwargs.get("query", "")
        
        return self._retrieveInformation(base, "RetrieveAPPCustomerInformationByString")

    def getIdAlunno(self) -> str:
        """
        Metodo per ottenere l'id dell'alunno
        ### Returns
        -------
        str
            Id dell'alunno
        """
        if not self._idAlunno:
            resp = self.retrieveDataInformation(self._services.RetrieveDataInformation.STUDENTI)
            self._idAlunno = resp[0].get("idAlunno", False)

        return self._idAlunno