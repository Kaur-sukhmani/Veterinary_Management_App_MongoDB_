# # Flask Web App :)
# # HTML Tutorial -> https://www.w3schools.com/html/
# # Bootstrap tutorial -> https://www.w3schools.com/bootstrap5/index.php/index.php
#
# """
#     wedfive
#     /templates
#     /sess19.py
# """
# from flask import *
# import datetime
# import hashlib
# from sess18B import MongoDBHelper
# from bson.objectid import ObjectId
#
# # bootsrap tutorial
#
#
# web_app = Flask("Vets App")
#
#
# @web_app.route("/")
# def index():
#     # return "This is amazing. Its : {}".format(datetime.datetime.today())
#     return render_template('index.html')
#
#
# @web_app.route("/register")
# def register():
#     return render_template('register.html')
#
#
#
# @web_app.route("/home")
# def home():
#     return render_template('home.html', email=session['vet_email'])
#
#
# # @web_app.route("/save-vet", methods=['POST'])
# @web_app.route("/register-vet", methods=['POST'])
# # def save_vet():
# def register_vet():
#     vet_data = {
#         'name': request.form['name'],
#         'email': request.form['email'],
#         'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
#         'createdOn': datetime.datetime.today()
#     }
#     print(vet_data)
#     db = MongoDBHelper(collection="vets")
#     db.insert(vet_data)
#
#     return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
#
#
# @web_app.route("/add-customer", methods=['POST', 'GET'])
# def add_customer():
#     # if len(session['vet_id']) == 0:
#     #     return render_template("/")
#
#     customer_data = {
#         'name': request.form['name'],
#         'phone': request.form['phone'],
#         'email': request.form['email'],
#         'age': int(request.form['age']),
#         'gender': request.form['gender'],
#         'address': request.form['address'],
#         'vet_id': session['vet_id'],
#         'vet_email': session['vet_email'],
#         'createdon': datetime.datetime.today()
#     }
#
#     if len(customer_data['name']) == 0 or len(customer_data['phone']) == 0 or len(customer_data['email']) == 0:
#         return render_template('error.html', message="Name, Phone, Email cannot be empty")
#
#     print(customer_data)
#     db = MongoDBHelper(collection="customer")
#     db.insert(customer_data)
#
#     return render_template('success.html', message="{} added successfully".format(customer_data['name']))
#
# @web_app.route("/update-customer-db", methods=['POST'])
# def update_customer_in_db():
#
#     # if len(session['vet_id']) == 0:
#     #     return redirect("/")
#
#     customer_data_to_update = {
#         'name': request.form['name'],
#         'phone': request.form['phone'],
#         'email': request.form['email'],
#         'age': int(request.form['age']),
#         'gender': request.form['gender'],
#         'address': request.form['address'],
#     }
#
#     if len(customer_data_to_update['name']) == 0 or len(customer_data_to_update['phone']) == 0 or len(customer_data_to_update['email']) == 0:
#         return render_template('error.html', message="Name, Phone and Email cannot be Empty")
#
#     print(customer_data_to_update)
#     db = MongoDBHelper(collection="customer")
#     query = {'_id': ObjectId(request.form['cid'])}
#     db.update(customer_data_to_update, query)
#
#     return render_template('success.html', message="{} updated successfully".format(customer_data_to_update['name']))
#
#
# @web_app.route("/login-vet", methods=['POST'])
# def login_vet():
#     vet_data = {
#         'email': request.form['email'],
#         'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest()
#
#     }
#
#     print(vet_data)
#     db = MongoDBHelper(collection="vets")
#     documents = db.fetch(vet_data)
#     print(documents, type(documents))
#     if len(documents) == 1:
#         session['vet_id'] = str(documents[0]['_id'])
#         session['vet_email'] = documents[0]['email']
#         session['vet_name'] = documents[0]['name']
#         print(vars(session))
#         return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
#     else:
#         return render_template('error.html')
#
#
# @web_app.route("/fetch-customers")
# def fetch_customer_of_vet():
#     db = MongoDBHelper(collection="customer")
#     # query = {'vet_email': session['vet_email']}
#     query = {'vet_id': session['vet_id']}
#     documents = db.fetch(query)
#     print(documents, type(documents))
#     # return "customers fetched for the Vet {}".format(session['vet_name'])
#     return render_template('customers.html', email=session['vet_email'], name=session['vet_name'], documents=documents)
#
# @web_app.route("/fetch-all-pets")
# def fetch_all_pets():
#     db = MongoDBHelper(collection="pet")
#     query = {'vet_id': session['vet_id']}
#     documents = db.fetch(query)
#     print(documents, type(documents))
#     # return "Customers Fetched for the Vet {}".format(session['vet_name'])
#     return render_template('all-pets.html',
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            documents=documents)
#
# @web_app.route("/fetch-pets/<id>")
# def fetch_pets_of_customer(id):
#
#     db = MongoDBHelper(collection="customer")
#     query = {'_id': ObjectId(id)}
#     customer = db.fetch(query)[0]
#
#     db = MongoDBHelper(collection="pet")
#     query = {'vet_id': session['vet_id'], 'customer_id': id}
#     documents = db.fetch(query)
#     print(documents, type(documents))
#     # return "Customers Fetched for the Vet {}".format(session['vet_name'])
#     return render_template('pets.html',
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            customer=customer,
#                            documents=documents)
#
# @web_app.route("/fetch-all-consultations")
# def fetch_all_consultations():
#
#     db = MongoDBHelper(collection="consultation")
#     query = {'vet_id': session['vet_id']}
#     documents = db.fetch(query)
#     print(documents, type(documents))
#     # return "Customers Fetched for the Vet {}".format(session['vet_name'])
#     return render_template('all-consultations-pets.html',
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            documents=documents)
#
# @web_app.route("/fetch-consultation-customer-pets/<id>")
# def fetch_consultations_of_customer_pets(id):
#     print("Inside fetch-consultation-customer-pets ")
#
#     db = MongoDBHelper(collection="pet")
#     query = {'_id': ObjectId(id)}
#     pet = db.fetch(query)[0]
#
#     db = MongoDBHelper(collection="consultation")
#     query = {'vet_id': session['vet_id'], 'customer_id': pet['customer_id'], 'pet_id': str(pet['_id'])}
#     print("[DEBUG] QUERY:", query)
#     documents = db.fetch(query)
#     print(documents, type(documents))
#     # return "Customers Fetched for the Vet {}".format(session['vet_name'])
#     return render_template('consultations-pets.html',
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            pet=pet,
#                            documents=documents)
#
#
# @web_app.route("/delete-customer/<id>")
# def delete_customer(id):
#     db = MongoDBHelper(collection='customer')
#     query = {'_id': ObjectId(id)}
#     customer = db.fetch(query)[0]
#     db.delete(query)
#     return render_template('success.html', message="Customer {} deleted".format(customer['name']))
#
#
#
# @web_app.route("/update-customer/<id>")
# def update_customer(id):
#     # return "Updating customer with Email{}".format(id)
#     db = MongoDBHelper(collection='customer')
#     query = {'_id': ObjectId(id)}
#     customer = db.fetch(query)[0]
#     return render_template('update-customer.html', email=session['vet_email'],
#                            name=session['vet_name'], customer=customer)
#
# @web_app.route("/search")
# def search():
#     return render_template('search.html', email=session['vet_email'], name=session['vet_name'])
#
#
#
# @web_app.route("/add-pet/<id>")
# def add_pet(id):
#     db = MongoDBHelper(collection='customer')
#     query = {'_id': ObjectId(id)}
#     customers = db.fetch(query)
#     customer = customers[0]
#     return render_template('add-pet.html',
#                            vet_id=session['vet_id'],
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            customer=customer
#                            )
#
#
# @web_app.route("/search-customer", methods = ['POST'])
# def search_customer():
#     db = MongoDBHelper(collection='customer')
#     query = {'email': request.form['email'], 'vet_id': session['vet_id']}
#     customers = db.fetch(query)
#     if len(customers) == 1:
#         customer = customers[0]
#         return render_template("customer-profile.html",
#                                customer=customer,
#                                email=session['vet_email'],
#                                name=session['vet_name'],
#                                )
#     else:
#         return render_template("error.html", message="Customer not found..")
#
#
# @web_app.route("/add-pet/<id>")
# def add_pet(id):
#     db = MongoDBHelper(collection='customer')
#     query = {'_id': ObjectId(id)}
#     customers = db.fetch(query)
#     customer = customers[0]
#     return render_template('add-pet.html',
#                            vet_id=session['vet_id'],
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            customer=customer
#                            )
#
#
# @web_app.route("/save-pet", methods = ['POST'])
# def save_pet():
#     print("Received POST request for /save-pet")
#     pet_data = {
#         'name': request.form['name'],
#         'breed': request.form['breed'],
#         'age': int(request.form['age']),
#         'gender': request.form['gender'],
#         'customer_id': request.form['customer_id'],
#         'customer_email': request.form['customer_email'],
#         'vet_id': session['vet_id'],
#         'createdon': datetime.datetime.today()
#     }
#     print("Form data:", request.form) #just for debuging
#
#     if len(pet_data['name']) == 0 or len(pet_data['breed']) == 0:
#         return render_template('error.html', message="Name and Breed cannot be Empty")
#
#     print(pet_data)
#     db = MongoDBHelper(collection="pet")
#     db.insert(pet_data)
#
#     return render_template('success.html', message="{} added for customer {} successfully.."
#                            .format(pet_data['name'], pet_data['customer_email']))
#
#
# web_app.route("/add-consultation/<id>")
# def add_consultation(id):
#     db = MongoDBHelper(collection='pet')
#     query = {'_id': ObjectId(id)}
#     pets = db.fetch(query)
#     pet = pets[0]
#
#
# @web_app.route("/add-consultation/<id>")
# def add_consultation(id):
#     db = MongoDBHelper(collection='pet')
#     print("in_add_consultaton")
#     query = {'_id': ObjectId(id)}
#     pets = db.fetch(query)
#     pet = pets[0]
#     print("running add_consultaton html file")
#     return render_template('add-consultation.html',
#                            vet_id=session['vet_id'],
#                            email=session['vet_email'],
#                            name=session['vet_name'],
#                            pet=pet
#                            )
#
# @web_app.route("/save-consultation", methods = ['POST'])
# def save_consultation():
#
# @web_app.route("/save-consultation", methods=['POST'])
# def save_consultation():
#     print("in_save_consultaton")
#     consultation_data = {
#         'problem': request.form['problem'],
#         'heartrate': int(request.form['heartrate']),
#         'temperature': float(request.form['temperature']),
#
#         'gender': request.form['gender'],
#         'pet_name': request.form['pet_name'],
#         'pet_id': request.form['pet_id'],
#         'customer_id': request.form['customer_id'],
#         'customer_email': request.form['customer_email'],
#         'vet_id': session['vet_id'],
#         'createdOn': datetime.datetime.today()
#     }
#
#     if len(consultation_data['problem']) == 0 or len(consultation_data['medicines']) == 0:
#         return render_template('error.html', message="Name and Breed cannot be Empty")
#         'medicines': request.form['medicines'],
#         'pet_name': request.form['pet_name'],
#         'pet_id': request.form['pet_id'],
#         'customer_id': request.form['customer_id'],
#         'vet_id': session['vet_id'],
#         'createdOn': datetime.datetime.today()
#     }
#     print("running save_consultaton html file")
#
#     if len(consultation_data['problem']) == 0 or len(consultation_data['medicines']) == 0:
#         return render_template('error.html', message="Problem and Medicine cannot be Empty")
#
#
#     print(consultation_data)
#     db = MongoDBHelper(collection="consultation")
#     db.insert(consultation_data)
#
#
#     return render_template('success.html', message="{} added for customer {} successfully.."
#                            .format(consultation_data['name'], consultation_data['customer_email']))
#
#
# # @web_app.route("/delete-pet/<id>")
# # def delete_pet(id):
# #     db = MongoDBHelper(collection='pet')
# #     query = {'_id': ObjectId(id), 'customer_id'}
# #     customer = db.fetch(query)[0]
# #     db.delete(query)
# #     return render_template('success.html', message="Customer {} deleted".format(customer['name']))
#
#
#     return render_template('success.html', message="Consultation for Pet {} added successfully..".format(consultation_data['pet_name']))
#
#
# @web_app.route("/delete-consultation/<id>")
# def delete_consultation(id):
#     print("Inside delete consultation pets ")
#
#     db = MongoDBHelper(collection="consultation")
#     query = {'_id': ObjectId(id)}
#     consultations = db.fetch(query)
#     print(consultations)
#     consultation = consultations[0]
#     db.delete(consultation)
#     return render_template('success.html', message="Consultation {} deleted with {} problem".format(id, consultation['problem']))
#
# @web_app.route("/update-consultation/<id>")
# def update_consultation(id):
#     db = MongoDBHelper(collection="consultation")
#     query = {'_id': ObjectId(id)}
#     consultation = db.fetch(query)[0]
#     return render_template("update-consultation.html",email=session['vet_email'],
#                            name=session['vet_name'], consultation=consultation)
#
#
# # Add this route to handle the form submission from update-consultation.html
# @web_app.route("/update-consultation-db", methods=['POST'])
# def update_consultation_db():
#     updated_consultation_data = {
#         'problem': request.form['problem'],
#         'heartrate': int(request.form['heartrate']),
#         'temperature': float(request.form['temperature']),
#         'medicines': request.form['medicines'],
#     }
#
#     consultation_id = request.form['consultation_id']  # Assuming you have an input field named consultation_id
#
#     if len(updated_consultation_data['problem']) == 0 or len(updated_consultation_data['medicines']) == 0:
#         return render_template('error.html', message="Problem and Medicine cannot be Empty")
#
#     print(updated_consultation_data)
#
#     db = MongoDBHelper(collection="consultation")
#     query = {'_id': ObjectId(consultation_id)}
#     db.update(updated_consultation_data, query)
#
#     return render_template('success.html', message="Consultation updated successfully")
#
#
# @web_app.route("/delete-pet/<id>")
# def delete_pet(id):
#     db = MongoDBHelper(collection='pet')
#     query = {'_id': ObjectId(id)}
#     pet = db.fetch(query)[0]
#     query = {'_id': ObjectId(id), 'customer_id': pet['customer_id']}
#     db.delete(query)
#     return render_template('success.html', message="Customer {} deleted".format(pet['name']))
#
# @web_app.route("/update-pet/<id>")
# def update_pet(id):
#     db = MongoDBHelper(collection='pet')
#     query = {'_id': ObjectId(id)}
#     pet = db.fetch(query)[0]
#     return render_template('update-pet.html', message="Pet with Id {} and Name {} Updated Successfully".format(id, pet['name']), email=session['vet_email'],
#                            name=session['vet_name'], pet=pet)
#
# @web_app.route("/update-pet-db", methods=['POST'])
# def update_pet_in_db():
#     pet_data_to_update = {
#         'name': request.form['name'],
#         'breed': request.form['breed'],
#         'age': int(request.form['age']),
#         'gender': request.form['gender']
#     }
#     if len(pet_data_to_update['name']) == 0 :
#         return render_template('error.html', message="Name and age cannot be Empty")
#
#     print(pet_data_to_update)
#     db = MongoDBHelper(collection='pet')
#     query = {'name': request.form['name']}
#     db.update(pet_data_to_update, query)
#
#     return render_template('success.html', message="{} updated successfully".format(pet_data_to_update['name']))
#
# @web_app.route("/logout")
# def logout():
#     session['vet_id'] = ""
#     session['vet_email'] = ""
#     return redirect("/")
#
#
# # session -> client is connected to server (store data and can use anywhere )
# def main():
#     # in order to use session in flask , we need some key as secret_key in app
#     web_app.secret_key = 'vetsapp-key-1'
#     web_app.run(port=5001)
#
#
# if __name__ == "__main__":
#     main()
# Flask Web App :)
# HTML Tutorial -> https://www.w3schools.com/html/
# Bootstrap tutorial -> https://www.w3schools.com/bootstrap5/index.php/index.php

"""
    wedfive
    /templates
    /sess19.py
"""
from flask import *
import datetime
import hashlib
from sess18B import MongoDBHelper
from bson.objectid import ObjectId

# bootsrap tutorial


web_app = Flask("Vets App")


@web_app.route("/")
def index():
    # return "This is amazing. Its : {}".format(datetime.datetime.today())
    return render_template('index.html')


@web_app.route("/register")
def register():
    return render_template('register.html')



@web_app.route("/home")
def home():
    return render_template('home.html', email=session['vet_email'])


# @web_app.route("/save-vet", methods=['POST'])
@web_app.route("/register-vet", methods=['POST'])
# def save_vet():
def register_vet():
    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'createdOn': datetime.datetime.today()
    }
    print(vet_data)
    db = MongoDBHelper(collection="vets")
    db.insert(vet_data)

    return render_template('home.html', email=session['vet_email'], name=session['vet_name'])


@web_app.route("/add-customer", methods=['POST', 'GET'])
def add_customer():
    # if len(session['vet_id']) == 0:
    #     return render_template("/")

    customer_data = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'address': request.form['address'],
        'vet_id': session['vet_id'],
        'vet_email': session['vet_email'],
        'createdon': datetime.datetime.today()
    }

    if len(customer_data['name']) == 0 or len(customer_data['phone']) == 0 or len(customer_data['email']) == 0:
        return render_template('error.html', message="Name, Phone, Email cannot be empty")

    print(customer_data)
    db = MongoDBHelper(collection="customer")
    db.insert(customer_data)

    return render_template('success.html', message="{} added successfully".format(customer_data['name']))

@web_app.route("/update-customer-db", methods=['POST'])
def update_customer_in_db():

    # if len(session['vet_id']) == 0:
    #     return redirect("/")

    customer_data_to_update = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'address': request.form['address'],
    }

    if len(customer_data_to_update['name']) == 0 or len(customer_data_to_update['phone']) == 0 or len(customer_data_to_update['email']) == 0:
        return render_template('error.html', message="Name, Phone and Email cannot be Empty")

    print(customer_data_to_update)
    db = MongoDBHelper(collection="customer")
    query = {'_id': ObjectId(request.form['cid'])}
    db.update(customer_data_to_update, query)

    return render_template('success.html', message="{} updated successfully".format(customer_data_to_update['name']))


@web_app.route("/login-vet", methods=['POST'])
def login_vet():
    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest()

    }

    print(vet_data)
    db = MongoDBHelper(collection="vets")
    documents = db.fetch(vet_data)
    print(documents, type(documents))
    if len(documents) == 1:
        session['vet_id'] = str(documents[0]['_id'])
        session['vet_email'] = documents[0]['email']
        session['vet_name'] = documents[0]['name']
        print(vars(session))
        return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template('error.html')


@web_app.route("/fetch-customers")
def fetch_customer_of_vet():
    db = MongoDBHelper(collection="customer")
    # query = {'vet_email': session['vet_email']}
    query = {'vet_id': session['vet_id']}
    documents = db.fetch(query)
    print(documents, type(documents))
    # return "customers fetched for the Vet {}".format(session['vet_name'])
    return render_template('customers.html', email=session['vet_email'], name=session['vet_name'], documents=documents)

@web_app.route("/fetch-all-pets")
def fetch_all_pets():
    db = MongoDBHelper(collection="pet")
    query = {'vet_id': session['vet_id']}
    documents = db.fetch(query)
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('all-pets.html',
                           email=session['vet_email'],
                           name=session['vet_name'],
                           documents=documents)

@web_app.route("/fetch-pets/<id>")
def fetch_pets_of_customer(id):

    db = MongoDBHelper(collection="customer")
    query = {'_id': ObjectId(id)}
    customer = db.fetch(query)[0]

    db = MongoDBHelper(collection="pet")
    query = {'vet_id': session['vet_id'], 'customer_id': id}
    documents = db.fetch(query)
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('pets.html',
                           email=session['vet_email'],
                           name=session['vet_name'],
                           customer=customer,
                           documents=documents)

@web_app.route("/fetch-all-consultations")
def fetch_all_consultations():

    db = MongoDBHelper(collection="consultation")
    query = {'vet_id': session['vet_id']}
    documents = db.fetch(query)
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('all-consultations-pets.html',
                           email=session['vet_email'],
                           name=session['vet_name'],
                           documents=documents)

@web_app.route("/fetch-consultation-customer-pets/<id>")
def fetch_consultations_of_customer_pets(id):
    print("Inside fetch-consultation-customer-pets ")
    db = MongoDBHelper(collection="pet")
    query = {'_id': ObjectId(id)}
    pet = db.fetch(query)[0]

    db = MongoDBHelper(collection="consultation")
    query = {'vet_id': session['vet_id'], 'customer_id': pet['customer_id'], 'pet_id': str(pet['_id'])}
    print("[DEBUG] QUERY:", query)
    documents = db.fetch(query)
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('consultations-pets.html',
                           email=session['vet_email'],
                           name=session['vet_name'],
                           pet=pet,
                           documents=documents)


@web_app.route("/delete-customer/<id>")
def delete_customer(id):
    db = MongoDBHelper(collection='customer')
    query = {'_id': ObjectId(id)}
    customer = db.fetch(query)[0]
    db.delete(query)
    return render_template('success.html', message="Customer {} deleted".format(customer['name']))



@web_app.route("/update-customer/<id>")
def update_customer(id):
    # return "Updating customer with Email{}".format(id)
    db = MongoDBHelper(collection='customer')
    query = {'_id': ObjectId(id)}
    customer = db.fetch(query)[0]
    return render_template('update-customer.html', email=session['vet_email'],
                           name=session['vet_name'], customer=customer)

@web_app.route("/search")
def search():
    return render_template('search.html', email=session['vet_email'], name=session['vet_name'])


@web_app.route("/search-customer", methods = ['POST'])
def search_customer():
    db = MongoDBHelper(collection='customer')
    query = {'email': request.form['email'], 'vet_id': session['vet_id']}
    customers = db.fetch(query)
    if len(customers) == 1:
        customer = customers[0]
        return render_template("customer-profile.html",
                               customer=customer,
                               email=session['vet_email'],
                               name=session['vet_name'],
                               )
    else:
        return render_template("error.html", message="Customer not found..")

@web_app.route("/add-pet/<id>")
def add_pet(id):
    db = MongoDBHelper(collection='customer')
    query = {'_id': ObjectId(id)}
    customers = db.fetch(query)
    customer = customers[0]
    return render_template('add-pet.html',
                           vet_id=session['vet_id'],
                           email=session['vet_email'],
                           name=session['vet_name'],
                           customer=customer
                           )

@web_app.route("/save-pet", methods = ['POST'])
def save_pet():
    print("Received POST request for /save-pet")
    pet_data = {
        'name': request.form['name'],
        'breed': request.form['breed'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'customer_id': request.form['customer_id'],
        'customer_email': request.form['customer_email'],
        'vet_id': session['vet_id'],
        'createdon': datetime.datetime.today()
    }
    print("Form data:", request.form) #just for debuging

    if len(pet_data['name']) == 0 or len(pet_data['breed']) == 0:
        return render_template('error.html', message="Name and Breed cannot be Empty")

    print(pet_data)
    db = MongoDBHelper(collection="pet")
    db.insert(pet_data)

    return render_template('success.html', message="{} added for customer {} successfully.."
                           .format(pet_data['name'], pet_data['customer_email']))


@web_app.route("/add-consultation/<id>")
def add_consultation(id):
    db = MongoDBHelper(collection='pet')
    print("in_add_consultaton")
    query = {'_id': ObjectId(id)}
    pets = db.fetch(query)
    pet = pets[0]
    print("running add_consultaton html file")
    return render_template('add-consultation.html',
                           vet_id=session['vet_id'],
                           email=session['vet_email'],
                           name=session['vet_name'],
                           pet=pet
                           )


@web_app.route("/save-consultation", methods=['POST'])
def save_consultation():
    print("in_save_consultaton")
    consultation_data = {
        'problem': request.form['problem'],
        'heartrate': int(request.form['heartrate']),
        'temperature': float(request.form['temperature']),
        'medicines': request.form['medicines'],
        'pet_name': request.form['pet_name'],
        'pet_id': request.form['pet_id'],
        'customer_id': request.form['customer_id'],
        'vet_id': session['vet_id'],
        'createdOn': datetime.datetime.today()
    }
    print("running save_consultaton html file")

    if len(consultation_data['problem']) == 0 or len(consultation_data['medicines']) == 0:
        return render_template('error.html', message="Problem and Medicine cannot be Empty")

    print(consultation_data)
    db = MongoDBHelper(collection="consultation")
    db.insert(consultation_data)

    return render_template('success.html', message="Consultation for Pet {} added successfully..".format(consultation_data['pet_name']))


@web_app.route("/delete-consultation/<id>")
def delete_consultation(id):
    print("Inside delete consultation pets ")

    db = MongoDBHelper(collection="consultation")
    query = {'_id': ObjectId(id)}
    consultations = db.fetch(query)
    print(consultations)
    consultation = consultations[0]
    db.delete(consultation)
    return render_template('success.html', message="Consultation {} deleted with {} problem".format(id, consultation['problem']))

@web_app.route("/update-consultation/<id>")
def update_consultation(id):
    db = MongoDBHelper(collection="consultation")
    query = {'_id': ObjectId(id)}
    consultation = db.fetch(query)[0]
    return render_template("update-consultation.html",email=session['vet_email'],
                           name=session['vet_name'], consultation=consultation)


# Add this route to handle the form submission from update-consultation.html
@web_app.route("/update-consultation-db", methods=['POST'])
def update_consultation_db():
    updated_consultation_data = {
        'problem': request.form['problem'],
        'heartrate': int(request.form['heartrate']),
        'temperature': float(request.form['temperature']),
        'medicines': request.form['medicines'],
    }

    consultation_id = request.form['consultation_id']  # Assuming you have an input field named consultation_id

    if len(updated_consultation_data['problem']) == 0 or len(updated_consultation_data['medicines']) == 0:
        return render_template('error.html', message="Problem and Medicine cannot be Empty")

    print(updated_consultation_data)

    db = MongoDBHelper(collection="consultation")
    query = {'_id': ObjectId(consultation_id)}
    db.update(updated_consultation_data, query)

    return render_template('success.html', message="Consultation updated successfully")


@web_app.route("/delete-pet/<id>")
def delete_pet(id):
    db = MongoDBHelper(collection='pet')
    query = {'_id': ObjectId(id)}
    pet = db.fetch(query)[0]
    query = {'_id': ObjectId(id), 'customer_id': pet['customer_id']}
    db.delete(query)
    return render_template('success.html', message="Customer {} deleted".format(pet['name']))

@web_app.route("/update-pet/<id>")
def update_pet(id):
    db = MongoDBHelper(collection='pet')
    query = {'_id': ObjectId(id)}
    pet = db.fetch(query)[0]
    return render_template('update-pet.html', message="Pet with Id {} and Name {} Updated Successfully".format(id, pet['name']), email=session['vet_email'],
                           name=session['vet_name'], pet=pet)

@web_app.route("/update-pet-db", methods=['POST'])
def update_pet_in_db():
    pet_data_to_update = {
        'name': request.form['name'],
        'breed': request.form['breed'],
        'age': int(request.form['age']),
        'gender': request.form['gender']
    }
    if len(pet_data_to_update['name']) == 0 :
        return render_template('error.html', message="Name and age cannot be Empty")

    print(pet_data_to_update)
    db = MongoDBHelper(collection='pet')
    query = {'name': request.form['name']}
    db.update(pet_data_to_update, query)

    return render_template('success.html', message="{} updated successfully".format(pet_data_to_update['name']))

@web_app.route("/logout")
def logout():
    session['vet_id'] = ""
    session['vet_email'] = ""
    return redirect("/")


# session -> client is connected to server (store data and can use anywhere )
def main():
    # in order to use session in flask , we need some key as secret_key in app
    web_app.secret_key = 'vetsapp-key-1'
    web_app.run(port=5000)


if __name__ == "__main__":
    main()