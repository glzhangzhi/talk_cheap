首先是基本操作了
```
from lxml import etree
html = etree.HTML(r.text)
result = html.xpath('......')
```
nodename  选取此节点的所有子节点
/ 从根节点选取
// 从匹配选择的当前节点选择文档中的节点，不考虑他们的位置
. 选择当前节点
.. 选取当前节点的父节点
@ 选取属性

z.B.
bookstore 选取bookstore的节点
/bookstore 选取根节点下个bookstore节点
bookstore/book 选择bookstore节点下的book子节点
//book 选择所有book节点
bookstore//book 选择bookstore节点下所有的book节点，不一定要是子节点
//@lang 选取所有lang属性

/book[1] 选取第一个book节点，特别注意XPath里第一个元素是[1]，不是Python里的[0]
/book[last()] 选取最后一个book节点
/book[last()-1] 选取倒数第二个book节点
/book[position()<3] 选取前两个book节点
//title[@lang] 选取所有包含有lang属性的title节点
//title[@lang='eng'] 选取所有lang属性为eng的title节点
/book[price>35.00] 选取所有price值大于35的book的节点
//title[@lang='eng'][price>35.00] 选取所有语言为英语且价格大于35的节点

\* 匹配任何元素节点
@* 匹配任何属性节点

/book/* book节点下的所有子节点
//* 所有节点
//title[@*] 所有有属性的title
//title[child/@attri=‘a'] 所有的title节点，其下有child子节点且child中的attri属性值为a

可以使用|运算
//book/title | //book/price 选取book节点的所有title和price节点
//title | //price 选取所有title和price节点

Xpath中，Element类的一些属性和方法
node.tag 返回节点名
node.text 返回节点内容
node.attrib 返回属性的字典对列表
node.getparent() 返回父节点
node.getchildren() 返回子节点
node.get('属性名') 得到属性的值
node.items() 列出此节点的所有属性键值对