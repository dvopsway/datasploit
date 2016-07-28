from pymongo import MongoClient

def save_record(domain, tid, key, data):
	client = MongoClient()
	db = client.database1
        d = {"targetname": domain, "taskId": tid, "record": {"type": key, "data": data}}
        result = db.domaindata.insert(d, check_keys=False)
        return result
