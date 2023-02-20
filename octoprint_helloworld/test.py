import os

stream = os.popen('echo Returned output')
output = stream.read()
print(output)
