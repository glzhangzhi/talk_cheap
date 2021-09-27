# 保存

```python
import pickle

a = 1

with open('example.pickle', 'wb') as file:
	pickle.dump(a, file)
```

# 提取

```python
import pickle

with open('example.pickle', 'rb') as file:
    a = pickle.load(file)
```

