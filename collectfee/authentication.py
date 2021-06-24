import pyrebase
import pyrebase
config = {
  "apiKey": "AIzaSyDXrmsZ84_F5epIVe-DlfnddQLMlDpxH1o",
  "authDomain": "rajarshi-8c7cc.firebaseapp.com",
  "databaseURL": "https://rajarshi-8c7cc-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "rajarshi-8c7cc.appspot.com",
  "serviceAccount": "collectfee/serviceAccountKey.json"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

persons = db.child("persons").get()
print(persons.val())


