import pymongo 
import pandas

client = pymongo.MongoClient("mongodb+srv://Group78:CS361@cluster0.coljqkn.mongodb.net/?retryWrites=true&w=majority")
 
# Database Name
db = client["Plunder_high_scores"]
 
# Collection Name
col = db["High_Scores"]
 
x = col.find({},{'_id': 0})


df = pandas.DataFrame(x)
print(df)