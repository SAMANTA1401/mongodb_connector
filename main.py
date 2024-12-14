import pymongo
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient('mongodb://localhost:27017/mlops');
# Database Name
databases = client['mlops']
# Collection  Name
collection = databases['mongopack']

# Sample data
d = {'companyName': 'phyCS',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")