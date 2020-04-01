from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = target_movie['star']


#movies = list(db.movies.find({'star':target_star}))

db.movies.update_many({'star':target_star},{'$set': {'star':0}})

