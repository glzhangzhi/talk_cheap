```python
import socket

hostname = socket.gethostname()
localip = socket.gethostbyname(hostname)
print(localip)
```

```python
import os

IP = os.popen('hostname -I').read().split('\n')[0][:-1]
print(IP)
```

