from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

#db.orders.insert_one({'orderName':'abonne_bag','orderCount':1,'orderAddress': '서울시 강남구', 'orderNumber': '010-1111-1111'})

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('shopmain.html')


## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    orderName_receive = request.form['orderName_give']
    orderCount_receive = request.form['orderCount_give']
    orderAddress_receive = request.form['orderAddress_give']
    orderNumber_receive = request.form['orderNumber_give']

    # DB에 삽입할 order form 만들기
    order = {
        'orderName': orderName_receive,
        'orderCount': orderCount_receive,
        'orderAddress': orderAddress_receive,
        'orderNumber': orderNumber_receive

    }
    # orders에 order 저장하기
    db.orders.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    # 1. DB에서 리뷰 정보 모두 가져오기
    orders = list(db.orders.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'orders': orders})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
