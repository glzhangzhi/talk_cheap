# 创建

```python
import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()
# conn.execute('DROP TABLE USER; ')
cursor.execute('''
CREATE TABLE USERS
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SEX VARCHAR(10),
CITY VARCHAR(10),
SALARY REAL
);
''')
cursor.execute("INSERT INTO USER (ID, NAME, AGE, SEX, CITY, SALARY)"
            "VALURES(1, 'LEO', 32, 'MALE', 'SHANGHAI', 12000)")
cursor.execute("INSERT INTO USER (ID, NAME, AGE, SEX, CITY, SALARY)"
            "VALURES(2, 'JACK', 30, 'MALE', 'BEIJING', 15000)")
cursor.execute("INSERT INTO USER (ID, NAME, AGE, SEX, CITY, SALARY)"
            "VALURES(3, 'LULU', 27, 'FEMALE', 'CHENGDU', 8000)")
cursor.execute("INSERT INTO USER (ID, NAME, AGE, SEX, CITY, SALARY)"
            "VALURES(4, 'MARTIN', 28, 'MALE', 'NANJING', 9500)")
cursor.close()
conn.commit()
conn.close()
```

# 读取

```python
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("select * from user where id=?", ('1'))
rows = cursor.fetchall()
# row = cursor.fetchone()
for row in rows:
    print(row)
cursor.close()
conn.close()
```

# 插入

```python
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
# 第一种插入方式
cursor.execute("insert into user values(5,'A',55)")
# 第二种插入方式
many = ((5, 'A', 55),
        (6, 'B', 44),
        (7, 'C', 33)
)
cursor.executemany("insert into user values(?, ?, ?)", many)
# 第三种插入方式
cursor.executescript("""insert into cars values(5, 'A', 55);
					  insert into cars values(6, 'B', 44);
					  insert into cars values(7, 'C', 33);
""")
cursor.close()
conn.commit()
conn.close()
```

# 更新

```python
conn = sqlite3.connect('users.db')
conn.execute("UPDATE USERS set SALARY =30000.00 WHERE ID=10");
conn.commit()
conn.close()
```

# 查询

```python
conn = sqlite3.connect('users.db')
conn.execute("SELECT AGE, SALARY from USERS"
			 "WHERE AGE > 30 and SALARY >= 10000");
for row in cursor:
	print(row)
conn.close()
```

# 排序

```python
conn = sqlite3.connect('users.db')
cursor = conn.execute("SELECT id, name, CITY, salary "
                      " from USERS ORDER BY salary DESC ")
for row in cursor:
    print(row)
conn.close()
```

# 删除

```python
conn = sqlite3.connect('users.db')
conn.execute("DELETE from USERS where ID=2")
conn.commit()
```

