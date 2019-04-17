# TDD workshop in Python using Pytest

The code is based on this: https://osherove.com/tdd-kata-1/

We are using pytest. Best practice is to list requirements in a requirements file. So you can install it like this:

## installation

```
pip install -r requirements.txt
```

This code works with Python2.7 and Python3.7.

## suggested procedure

Read the kata web page from the top and see if you can figure out what piece of the kata specification was implemented by each test.

Then keep going :)

## useful stuff

`re` stands for "regular expression". These make life nice and easy. Eg:

```
re.split("[,\n]","1,2\n3")
['1', '2', '3']
```

To learn about what a function does:

```
help(re.split)
```

to run the tests. `cd` into the project directory and run:

```
py.test
```

And virtualenvironments are your friends. We'll learn about them properly another day but if you have already been exposed to them then it would be best if you used one. (best == industry-standard best practice)



