class services:
    class RetrieveDataInformation:
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":""},"sVendorToken":"{{vendorAlu}}"}
        STRUCTURAL = "GET_STRUCTURAL"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"dataGiorno":"28/02/2024"}},"sVendorToken":"{{vendorAlu}}"}
        TIMELINE = "GET_TIMELINE"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"appName":"ALU_APP"}},"sVendorToken":"{{vendorAlu}}"}
        STUDENTI = "GET_STUDENTI"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        COMUNICAZIONI = "GET_COMUNICAZIONI"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        COMPITI = "GET_COMPITI_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        ORARIO = "GET_ORARIO_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        MATERIALE = "GET_MATERIALE_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        ARGOMENTI = "GET_ARGOMENTI_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        VOTI = "GET_VOTI_LIST_DETAIL"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        ASSENZE = "GET_ASSENZE_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        NOTE = "GET_NOTE_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        AUTORIZZAZIONI = "GET_AUTORIZZAZIONI_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        PAGELLA = "GET_PAGELLA_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        CURRICULUM = "GET_CURRICULUM_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        PAGOSCUOLA = "GET_PAGOSCUOLA_MASTER"
        # : {"sCodiceFiscale":"{{sCodiceFiscale}}","sSessionGuid":"{{usersession}}","sCommandJSON":{"sApplication":"FAM","sService":"","data":{"alunnoId":"{{idalunno}}"}},"sVendorToken":"{{vendorAlu}}"}
        DOCUMENTI = "GET_DOCUMENTI_MASTER"
        
    class RetrieveAPPCustomerInformationByString:
        SSEARCH = "sSearch"