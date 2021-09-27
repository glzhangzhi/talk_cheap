```python
import socket

hostname = socket.gethostname()
localip = socket.gethostbyname(hostname)
print(localip)
```

