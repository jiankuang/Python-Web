# Python
## Python Interpreter
On Windows machines, the Python installation is usually placed in `C:\Python27`

## Decorator

## Interview Questions
### Theoretical Questions
#### How do you understand "In Python, functions are first-class objects."?
This means that they can be assigned to variables, returned from other functions and passed into functions. 

#### What are the supported data types in Python? (Five standard data types)
Numbers, String, List, Tuple, Dictionary

#### What are tuples in Python?
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

#### What is the difference between tuples and lists in Python?
The main differences between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

#### What is the difference between Django and Flask?
Flask is a “microframework” primarily build for a small application with simpler requirements.  In flask, you have to use external libraries.  Flask is ready to use.
Django can also used for larger applications.  It includes an ORM.

### Coding Questions
#### What will be the output of the code below? Explain your answer.
```python
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```
The output of the above code will be:
```python
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```
##### How would you modify the definition of `extendList` to produce the presumably desired behavior?
The definition of the extendList function could be modified as follows
```python
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
```
With this revised implementation, the output would be:
```python
list1 = [10]
list2 = [123]
list3 = ['a']
```

#### What will be the output of the code below? Explain your answer.
```python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
```
The output of the above code will be:
```
1 1 1
1 2 1
3 2 3
```
