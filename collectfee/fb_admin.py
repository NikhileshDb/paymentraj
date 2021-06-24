from django.shortcuts import render
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("collectfee/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
import json
db = firestore.client()

# # Add documents
# data = {
#     'name': 'John Doe',
#     'age': 34, 
#     'employed': 'False'
# }
# #db.collection('poeple').add(data)

# #Set documents with known IDs
# data = {
#     'name': 'John Doe',
#     'age': 34, 
#     'employed': 'False'
# }

# db.collection('persons').document('jandoe').set({'address':'London'}, merge=True) #Document reference

#set documents with auto IDs
#db.collection('persons').document().set(data)

# Get collection by known Id
# result = db.collection('persons').document("jandoe").get()
# if result.exists:
#     print(result.to_dict())


#Get all documents in collection
# docs = db.collection('persons').get()
# for doc in docs:
#     print(doc.to_dict())


# Querying
# Equal

# docs = db.collection('persons').where('age', '<', 40).get()
# for doc in docs:
#     print(doc.to_dict())

# def fireTest(request):
#     data = db.collection('persons').get()
#     id = []
#     keys= []
#     values = []
#     for data in data:
#         ids = data.id
#         id.append(ids)
#         ls_doc = data.to_dict()
#         for doc in ls_doc:
#             for k,v in ls_doc.items():
#                 keys.append(k)
#                 values.append(v)
#     print(id)
#     print(keys)
#     print(values)
#     comb_lis = zip(id , keys, values)
#     context = {
#        'comb_lis':comb_lis
#     }
    
#     return render(request, 'firetest.html', context)

# data = db.collection('persons').get()
# datas = []
# for doc in data:
#     dat = doc.to_dict()
#     datas.append(dat)
# print(datas)
    
from firebase_admin import auth



#    # Start listing users from the beginning, 1000 at a time.
# page = auth.list_users()
# while page:
#     for user in page.users:
#         print('User: ' + user.uid)
#     # Get next batch of users.
#     page = page.get_next_page()

# # Iterate through all users. This will still retrieve users in batches,
# # buffering no more than 1000 users in memory at a time.
# for user in auth.list_users().iterate_all():
#     print('User: ' + user.uid)
   




# dad = db.collection("persons").document('o2y4aj9z1SCSSk3qgURb').get()
# dam = dad.to_dict()
# key = []
# val = []
# for k,v in dam.items():
#     key.append(k)
#     val.append(v)

# print(key, val)








# from django.db import models
# class persons(models.Model):
#     def __init__(self, name, age, address, employed ):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.employed = employed
    
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(max_length=200)
#     address = models.CharField(max_length=200)
#     employed = models.CharField(max_length=200)




# def fireTest(request):
#     data = db.collection('persons').get()
#     ls_doc = []
#     for doc in data:
#         ls_doc.append(doc.to_dict())
#     lj = json.dumps(ls_doc)
#     lj_list = json.loads(lj)
#     print(type(lj_list))
#     return render(request, 'firetest.html')

# data = db.collection('persons').get()
# ls_dat = []

# for doc in data:
#     dat  = doc.to_dict()
#     ls_dat.append(dat)

# print(type(ls_dat))

# lj = json.loads(ls_dat)
# print(type(lj))
