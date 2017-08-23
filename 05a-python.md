# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and Tuples are both structures for storing data.  The main difference is that tuples are immutable and lists are mutable.  Tuples are a better choice for dictionaries because of their immutability - the structure of the data is very unlikely to change and if you need to change it for a particular purpose you can just create a new tuple or list for those purposes.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists are an ordered collection of non-unique elements whereas sets are an unordered collection of unique elements.  You can iterate over a list but not a set.  Finding an element is faster in a set because it is hashable and immutable.  

Examples:
my_set = set(n\*3 for n in range(5))
my_list = ["apples", "bananas", "oranges", "peaches"]

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

a lambda function is an anonymous function that is used at runtime to perform actions inline.

Example:
nums = [n\*\*2 for n in range(20)]
sorted(nums, key=lambda num: num%2 == 0)

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.   

List comprehension is creating a list based on a number set defined in the input.     
Example:   
``` 
L = {x**2 for x in range(15)}
```
map equivalent: 
```
L = list(map(lambda x:x**2, range(15)))
```
filter equivalent:
```
squares = list(filter(lambda x: x in L, range(200)))
```

List is very open ended and can create a huge variety of types of lists.  Map is limited in that it requires applying a function to a list.  Filter is limited more in that it must pull out elements from a list for which a condition evaluates as true.     

Set comprehension ex:   
```
import string
s = {x for x in string.ascii_lowercase}
```
Dict comprehension ex:   
```
{x: x**3 for x in range(40) if x**3 % 3 == 0}
```



---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





