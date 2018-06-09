from pymongo import MongoClient
mongo_uri = "mongodb://ducsang:SANG1998@ds013182.mlab.com:13182/sangbui-c4e18"

#1. connect to database
client = MongoClient(mongo_uri)

#2. get database 
db = client.get_default_database()

#3. create collection 
games = db["gmaes"]
film = db["films"]

#4. create document

# new_game = {
#     "title": "pes",
#     "description":"game pro "

# new_film ={
#     "anime":"inuyasha",
#     "film hd":"cuoc chien vo cuc",
#     "film hai":"chien thang"
# }



#5. insert document into collection
# games.insert_one(new_game)
# film.insert_one(new_film)

all_games = games.find()
for game in all_games:
    print(game)