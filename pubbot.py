\#Importiamo le librerie
import os
from InstagramAPI import InstagramAPI
import time
import schedule

\#Importiamo l'elenco di tutti i file presenti nella cartella coda_file in una lista
fileNames = os.listdir("./coda_file/")

\#definiamo la funzione che pubblicherà i nostri file
def pubblica():
    print("..Pubblicazione")

    IGUSER = "...Il tuo username di In"  
    PASSWD = "...la tua password" 

    IGCaption = "Questa è la descrizione della nostra immagine posso aggiungere anche dei tag #motivazione #dailymotivational"

    igapi = InstagramAPI(IGUSER, PASSWD)
    \#Colleghiamoci all'API di instgram
    igapi.login() 

    \#eliminiamo la foto pubblicata
    photo = './elaborati/'+ fileNames[0]
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    print("Elimino : " + "./elaborati/" + fileNames[0])
    os.remove("./elaborati/" + fileNames[0])
