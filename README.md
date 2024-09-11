# LIE
> List item extractor

A program that print the largest int in a list
In a dict it only look at the keys.
It ignores non integers value and convert floats to integers.

### Example of list type that requires quotes when passed as arguments:

~~~
python lie.py "{1:2,2:a,3:b}"
~~~
OR
~~~
python lie.py "(1,a,3)"
~~~

> Output: 3

---

### Example of list type that don't requires quotes when passed as arguments:

~~~
python lie.py [1,2,5,6,3,5,a,5]
~~~
OR
~~~
python lie.py 1,2,5,6,3,5,a,5
~~~
OR
~~~
python lie.py 1 2 5 6 3 5 a 5
~~~

> Output: 6
