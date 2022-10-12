from flask import Flask
from flask_cors import CORS, cross_origin
import pymongo
from bson.json_util import dumps

conn_str = "mongodb+srv://[user]:[password]@cluster0.wvmvj.mongodb.net/newsdb"
client = pymongo.MongoClient(conn_str, serverSelectiontimeoutMS=10000)
db = client['newsdb']

app = Flask(__name__)
cors = CORS(app)


@app.get('/')
def index():
    return "hello world"


@app.get('/getData')
def getData():
    data = db.newsV2.find({}).limit(20)
    data_to_json = list(data)
    json_data = json.dumps(data_to_json)
    return json_data, mimetype="application/json" 

@app.get('/test')
def test():
    list = [{'id': {'oid':'1'}, 'title': 'lololol', 'date':'212121'
    }, {'id': {'oid':'1'}, 'title': 'lololol', 'date':'212121'
    }, {'id': {'oid':'1'}, 'title': 'lololol', 'date':'212121'
    }]
    return list


if __name__=="__main__":
    app.run(debug=True)