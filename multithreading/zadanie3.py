import uuid
import hashlib

res = {}
for i in range(200):
    id = str(uuid.uuid4().hex)
    sum = hashlib.md5(id.encode()).hexdigest()
    res[id] = sum

for (key, value) in res.items():
    print('{key}: {value}'.format(key=key, value=value))