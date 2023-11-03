import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('secret.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'autumn-webapp',
})

def set_data_db(data):

  collection = data['collection']
  document = data['document']
  contents = data['contents']

  db = firestore.client()

  # doc_ref = db.collection(u'users').document(u'user01')
  # doc_ref.set({
  #     u'level': 20,
  #     u'money': 700,
  #     u'job': "knight"
  # })

  doc_ref = db.collection(collection).document(document)
  doc_ref.set(contents)
  
  return


def delete_collection(coll_name):
	batch_size = 10
	deleted = 0

	db = firestore.client()
	coll_ref = db.collection(coll_name)
	docs = coll_ref.list_documents(page_size=batch_size)

	for doc in docs:
		print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
		doc.delete()

# da = {
#   "collection": "user",
#   "document": "autumn",
#   "contents": {

#     "job" : "dataengineer",
#     "money" : 500,
#     "age" : 30,

#   }
#   }

# set_data_db(da)
