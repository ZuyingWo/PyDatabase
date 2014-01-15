__author__ = 'williewonka'

import PyDatabase

db = PyDatabase.PyDatabase(host="localhost",user="root",passwd="",db="test")
print(db.Update(table='test', values={'testtext': 'test2'}, condition_and={'ID': 1}))
print(db.query)
print(db.Select(table="test", columns=["testtext", "testinteger"], condition_and={'ID': 1}))
print(db.query)
print(db.Insert(table='test', values={'testtext': "new 'foo' insert", 'testinteger' : '76'}))
print(db.query)
db.Close()