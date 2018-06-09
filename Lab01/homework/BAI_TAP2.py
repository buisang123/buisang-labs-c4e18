from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
posts = db["posts"]
new_posts = {
    "title" : "BUI SANG",
    "author":"fa",
    "content":"một câu chuyện buồn: ......tôi mù lập trình ......!"

}
posts.insert_one(new_posts)