from urllib import parse
from Crypto.Cipher import ARC4
from pybase64 import b64encode, b64decode

class rc4:
    """
    Classe di metodi per la codifica e la decodifica
    ### Metodi
    -------
    get_key()
        Restituisce la chiave di codifica impostata
    """
    def __init__(self, key: str) -> None:
        self._key = key.encode()

    def _crypt(self):
        return ARC4.new(self._key)

    def get_key(self) -> str:
        """
        Restituisce la chiave di codifica impostata
        ### Returns
        -------
        str
            La chiave di codifica impostata
        """
        return self._key.decode()

    def encrypt(self, data: str, urlenc: int = 1) -> str:
        """
        ### Parametri
        ----------
        `data`: str
            Stringa di dati da criptare
        `urlenc`: int = 1
            Numero di volte da urlencodare la stringa criptata
        ### Returns
        -------
        str
            La stringa criptata e urlencodata `urlenc` volte
        """
        crypted = self._crypt().encrypt(data.encode()) # utf-8 encode => cripta con rc4
        crypted = b64encode(crypted).decode() # base64 encode => utf-8 decode

        for _ in range(urlenc):
            crypted = parse.quote(crypted, safe="") # url encode `urlenc` volte

        return crypted

    def decrypt(self, data: str) -> str:
        """
        ### Parametri
        ----------
        `data`: str
            Stringa di dati da decriptare
        ### Returns
        -------
        str
            La stringa decriptata
        """
        data = data.replace("\"", "")
        data = data.replace("\\/", "/") #TODO: trovare un modo migliore per gestire gli escape visto che data.encode().decode("unicode-escape") non funziona
        old = False
        # Loop per decodificare la stringa urlencoded n volte determinate in automatico
        while(data != old):
            old = data
            data = parse.unquote(data) # url decode
        decrypted = b64decode(data.encode()) # utf-8 encode => base64 decode
        decipher = self._crypt().encrypt(decrypted)
        
        return decipher.decode("latin1") # (~utf-8 decode~) sembra sia in latin1