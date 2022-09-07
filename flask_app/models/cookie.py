from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

NUMBOXES_REGEX = re.compile(r'^[1-9]\d*$')

class Cookie:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # STATIC METHODS

    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie['customer_name']) < 1:
            flash(u'First name must be at least 1 character long', 'customer_name')
            is_valid = False

        customers = []

        query = '''
        SELECT cookie_orders.customer_name FROM cookie_orders;
        '''
        results = connectToMySQL('cookie_orders').query_db(query)

        for row in results:
            print(f'{row} PRINTING ROW ---------------------------------------------------------------')
            customers.append(row['customer_name'])

        
        print(f'{customers} CUSTOMERS LIST AFTER FOR LOOP --------------------------------------------------')

        print(f"{cookie['customer_name']} CUSTOMER NAME PASSED IN FROM FROM --------------------------------------)")

        if cookie['customer_name'] in customers:
            flash(u'Customer name already exists', 'customer_name')
            is_valid = False
        
        if len(cookie['cookie_type']) < 5:
            flash(u'Cookie type must be at least 5 characters.', 'cookie_type')
            is_valid = False
        
        if not NUMBOXES_REGEX.match(cookie['num_boxes']):
            flash(u'Must order at least one box of cookies. Positive integers only.', 'num_boxes')
            is_valid = False
        
        return is_valid


    # CLASS METHODS

    @classmethod
    def get_all(cls):
        query = '''
        SELECT * FROM cookie_orders;
        '''
        results = connectToMySQL('cookie_orders').query_db(query)

        all_orders = []

        for row in results:
            all_orders.append(cls(row))
        
        return all_orders
