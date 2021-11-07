import hashlib
import multiprocessing
import uuid

#generated_ids - lista identyfikatorów
#ids_num - liczba identyfikatorów
generated_ids = []
ids_num = 200

#wyliczenie sumy i zwrócenie zapisanej w systemie szesnastkowym
def enumerateControlSum(uuid):
    return hashlib.md5(uuid.encode()).hexdigest()

for i in range(ids_num):
    generated_ids.append(uuid.uuid4().hex)

ids_sums = multiprocessing.Pool().map(enumerateControlSum, generated_ids)

for i in range (ids_num):
    print(f"{generated_ids[i]} - {ids_sums[i]}")



