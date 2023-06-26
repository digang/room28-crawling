import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Firebase 서비스 계정 키(JSON 파일)의 경로
cred = credentials.Certificate('private_key.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 가져오기
db = firestore.client()

# JSON 파일 업로드
def upload_json_to_firestore(json_path, collection_name):
    with open(json_path, 'r') as file:
        data = json.load(file)
        collection_ref = db.collection(collection_name)
        if collection_name == 'Brands':
            # 컬렉션 경로
            collection_path = "Brands/7d5wwd5AJHaJFSTq95Fy/Products"
            # 컬렉션 레퍼런스
            collection_ref = db.collection(collection_path)
            # 컬렉션의 모든 문서 가져오기
            docs = collection_ref.get()
            # 문서 삭제
            for doc in docs:
                doc.reference.delete()
        
        if isinstance(data, list):
            for item in data:
                brand_name = item['brandName']
                query = collection_ref.where(field_path="branName", op_string="==", value=brand_name)
                
                results = query.get()
                
                if len(results) > 0:
                    for doc in results:
                        doc.reference.update(item)
                        print(brand_name + " is updated!")
                else:
                    if brand_name == 'donut_revenge':
                        document_ref = collection_ref.document()  # 새로운 문서 생성
                    else:
                        document_ref = collection_ref.document(brand_name)  # 새로운 문서 생성
                    document_ref.set(item)
                    print(brand_name + " is created!")
        elif isinstance(data, dict):
            for document_id, document_data in data.items():
                document_ref = collection_ref.document(document_id)
                document_ref.set(document_data)
        else:
            print("Invalid JSON format: Expecting a list or dictionary.")

# JSON 파일 업로드 호출 예시
upload_json_to_firestore('./list.json', 'News')
upload_json_to_firestore('./donut_revenge.json', 'Brands')

