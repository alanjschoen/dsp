# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> > Tuples are static, while lists are dynamic.  Lists support operations like appending, deleting, changing values, pushing, and popping. This makes them very useful for many things, but also makes their contents unpredictable.  Tuples work as dictionary keys because they are static, and they support content comparisons.  When comparing lists, you are really comparing memory locations.  When comparing tuples, you are comparing contents.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> > Lists are ordered and they don't care about their contents.  Sets are unordered and enforce rules about their contents, like uniqueness and search-optimized storage.  For instance, each element in a set must be unique.  These restrictions allow for faster lookup times, which gives much better performance for many operations.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> > lambda declares an anonymous function.  `f = lambda x: x[::-1]` creates a function handle that reverses the order of a list, and stores the handle in the variable `f`.  I can use this handle with the `sorted` function to sort a list of strings by the last letter instead of the first letter `sorted("Non Impediti Ratione Cogitationis".split(), key=f)`.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> > List comprehensions allow you to build a list by collecting the output of a `for` loop.  For instance, `[pow(x,2) for x in range(5)]` creates a list of the squares of numbers from 0 to 4.  The list comprehension `[f(x) for x in arr]` is equivalent to `map(f, arr)`.  Similaryly, `[x for x in arr if f(x)]` is equivalent to `filter(f, arr)`.

> > List comprehensions let you string together operations in a better way.  `[w1 for w1 in par1.split() for w2 in par2.split() if w1==w2]` lets us find all of the matching words in two paragraphs `par1` and `par2` (this is not an efficient solution).  We could use `map` and `filter` to do this, but it would be unreadable: `filter(lambda y: any(map(lambda x: x==y, par2.split())), par1.split())`.

> > Set comprehensions work in a similar way to list comprehensions, but using curly brackets.  `{x for x in arr if x%3==0}` creates a set out numbers in the iterable `arr` which are divisible by 3.
> > Dictionary comprehensions `{value: list2.index(value) for value in list1 if value in list2}` returns a dictionary mapping the values in `list1` to their indices in `list2`.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





