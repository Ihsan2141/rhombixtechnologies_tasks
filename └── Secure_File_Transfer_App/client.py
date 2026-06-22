```python
import socket
from crypto_utils import *
from datetime import datetime

HOST = '127.0.0.1'
PORT = 9999

key = generate_key()

with open("SampleFiles/testfile.txt", "rb") as f:
    data = f.read()

original_hash = calculate_hash(data)

encrypted = encrypt_data(data, key)

client = socket.socket()
client.connect((HOST, PORT))

client.send(encrypted)

client.close()

with open("Logs/transfer_log.txt", "a") as log:
    log.write(
        f"{datetime.now()} - File Sent - SHA256: {original_hash}\n"
    )

print("Encrypted file transfer completed.")
print("Original SHA256:", original_hash)
```
