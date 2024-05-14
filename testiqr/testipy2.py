import json

x =  '{ "elem":{ "i":"02630", "u":"02630.111678", "t":1715077560, "v":"2024-08-31" }, "type":"Tuudo", "sign":"jKpWXbUM1Blb8r12iJ1U+RRj7afTgMo6OaFYVifDh2bWLyNVo/GttJXiSXr046lRBw0W0aGl6LVswlQCcc4TOekPK3czYoGOcX7cNyLU0uCWWA30GZ1sHVs7IP2pbfnz6m9Ag4V/sqDW9WQJjIAtjSe/7kn/GGpl6bwCjFODOjI=" } '
y = json.loads(x)

u_value = y['elem']['u']
after_dot = u_value.split('.')[1]
u_integer = int(after_dot)

print(u_integer)
