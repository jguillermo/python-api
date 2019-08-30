from db import sql_db
from model import ModelA
from module_one import string_sql

sql_db.set_paramas('access')

print(string_sql())

print(ModelA.printer())
