__author__ = 'williewonka'

import PyDatabase

db = PyDatabase.PyDatabase()
print(db.Update(table='test', values={'testtext': 'test'}, condition_and={'ID': 1}))
print(db.query)
print(db.Select(table="test", columns=["testtext", "testinteger"], condition_and={'ID': 1}))
print(db.query)