import mysql.connector
from mysql.connector import Error
import os

from scipy import rand

os.chdir(os.path.dirname(__file__))

import random

connection = mysql.connector.connect(host='127.0.0.1',
                                     port='8002',
                                     database='db',
                                     user='root',
                                     password='root')


cursor = connection.cursor()




counter = 0
for i in range(0, 10000):
    for i in range(0, 1000):
        first_names = open('FirstNames.txt').readlines()
        first_name = random.choice(first_names).strip()
        last_names = open('LastNames.txt').readlines()
        last_name = random.choice(last_names).strip()
        
        balance = round(random.uniform(10.5, 5194.5),2)
        cursor.execute(f"INSERT INTO db.test (first_name, last_name, balance) VALUES ('{first_name}', '{last_name}', {balance});")
    
    connection.commit()
    counter += 1000
    
    print(f'+ {counter} rows')

# result = cursor.fetchall()
# print(result)