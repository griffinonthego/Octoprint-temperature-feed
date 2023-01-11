import os
import dht_simpletest.py

stream = os.popen('echo Returned output')
dht_simpletest.py
output = stream.read()
print(output)
