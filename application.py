import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pycountry_convert as pc

basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    dateOfBirth = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    countryCode = db.Column(db.String(5))
    email = db.Column(db.String(100))
    orders = db.relationship('Order', backref='customer')

    def __repr__(self):
        return f'<Customer "{self.firstName}">'

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'dateOfBirth': self.dateOfBirth,
            'city': self.city,
            'country': self.country,
            'country_code': self.countryCode,
            'email': self.email
        }
    
    def to_json_birthday(self):
        
        date = pd.Timestamp(self.dateOfBirth)

        return {
            'dateOfBirth': self.dateOfBirth,
            'day': date.day_name()
        }
    
    def to_json_continent(self):
        
        country_code = pc.country_name_to_country_alpha2(self.country, cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)

        return {
            'country': self.country,
            'continent': continent_name
        }


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    item = db.Column(db.String(100))
    email = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'item': self.item,
            'customer_id': self.customer_id
        }

    def __repr__(self):
        return f'<Order "{self.item}">'

@application.route('/customers/', methods=['POST'])
def create_customer():
    if not request.json:
        abort(400)
    customer = Customer(
        firstName = request.json.get('firstName'),
        lastName = request.json.get('lastName'),
        email = request.json.get('email').lower(),
        dateOfBirth = request.json.get('dateOfBirth'),
        city = request.json.get('city'),
        country = request.json.get('country')

    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json()), 201

# @application.route('/createorder/', methods=['POST', 'GET'])
# def create_order():
#     if request.method == 'POST':
#         firstName = request.form['firstName']
#         lastName = request.form['lastName']
#         email = request.form['email'].lower()
#         item = request.form['item']
#         customer_id = Customer.query.filter_by(email = email).first().id
#         order = Order(
#             firstName = firstName,
#             lastName = lastName,
#             email = email,
#             item = item,
#             customer_id = customer_id
#         )
#         db.session.add(order)
#         db.session.commit()
#     return jsonify(order.to_json()), 201

@application.route('/customers/<int:id>/', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    return jsonify(customer.to_json())

@application.route('/customers/<int:id>/birthday', methods=['GET'])
def get_customer_birthday(id):
    customer = Customer.query.get(id)
    return jsonify(customer.to_json_birthday())

@application.route('/customers/<int:id>/continent', methods=['GET'])
def get_customer_continent(id):
    customer = Customer.query.get(id)
    return jsonify(customer.to_json_continent())

@application.route('/orders/', methods=['POST'])
def create_order():
    if not request.json:
        abort(400)
    order = Order(
        firstName = request.json.get('firstName'),
        lastName = request.json.get('lastName'),
        email = request.json.get('email').lower(),
        item = request.json.get('item'),
        customer_id = Customer.query.filter_by(email = request.json.get('email').lower()).first().id
    )
    db.session.add(order)
    db.session.commit()
    print("Hi")
    return jsonify(order.to_json()), 201

@application.route('/orders/<int:id>/', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    return jsonify(order.to_json())

@application.route('/orders/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_json() for order in orders])

@application.route('/customers/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_json() for customer in customers])

@application.route('/')
def index():
    customers = Customer.query.all()
    orders = Order.query.all()
    return render_template('index.html', customers = customers, orders = orders)

    
