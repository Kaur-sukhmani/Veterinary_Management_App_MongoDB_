from sess18A import Customer
from sess18B import MongoDBHelper
from bson.objectid import ObjectId


def main():
    db = MongoDBHelper()

    # customer = Customer()
    #
    # customer.read_customer_data()
    #
    # document = vars(customer)
    #
    # db.insert(document)

    # query = {'phone': '+91 98779165055'}
    query = {'_id': ObjectId('64c35e6f3be3d75b04aef264')}
    # query = {'email': 'john@example.com'}
    # db.delete(query)

    db.fetch(query=query)

    document_data_to_update = {'name': 'George W', 'phone': '+91 9316807340', 'age': '33'}
    db.update(document_data_to_update, query)



if __name__ == "__main__":
    main()
