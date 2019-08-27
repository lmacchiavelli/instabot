#Importiamo le librerie
import os
from InstagramAPI import InstagramAPI
import time
import schedule

#Importiamo l'elenco di tutti i file presenti nella cartella coda_file in una lista
foldername = './coda_file/'
fileNames = os.listdir(foldername)

#definiamo la funzione che pubblicherà i nostri file
def pubblica():
    print("..Pubblicazione")

    IGUSER = '...Il tuo username di In'  
    PASSWD = '...la tua password'

    IGCaption = 'Questa è la descrizione della nostra immagine posso aggiungere anche dei tag #motivazione #dailymotivational...'

    igapi = InstagramAPI(IGUSER, PASSWD)
    #Ci colleghiamo all'API di instgram
    igapi.login() 
    
    #Pubblico l'immagine
    photo = foldername'+ fileNames[0]
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    
    #eliminiamo la foto pubblicata
    print("Elimino : " + foldername + fileNames[0])
    os.remove(foldername + fileNames[0])

    
#temporizziamo il tutto con il modulo schedule
schedule.every().day.at("09:12").do(pubblica)

while True:
    schedule.run_pending()
    time.sleep(1)
