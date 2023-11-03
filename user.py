from google.cloud import firestore
 
# 새로운 사용자를 데이터베이스에 추가
db = firestore.Client()
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
 'first': 'autumn',
 'last': 'seo',
 'born': 1994
})
 
# 그런 다음 사용자 목록을 쿼리
users_ref = db.collection('users')
for doc in users_ref.stream():
 print('{} => {}'.format(doc.id, doc.to_dict()))