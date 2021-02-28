# F-Strings & String Formatting In Python

"""
1 String Formatting (% Operator)
Python has a built-in operation that we can access with the % operator. 
This will help us to do simple positional formatting. If anyone knows a 
little bit about C programming, then they have worked with printf statement, 
which is used to print the output. This statement uses the % operator. Similarly, 
in Python, we can perform string formatting using the % operator. For Example:
"""
    
name="Jack"

print("My name is %s" %name)

"""
2 Using Tuple ()
The string formatting syntax, which uses % operator changes slightly if we want to
make multiple substitutions in a single string. The % operator takes only one argument,
to mention more than one argument, use tuples. Tuples are better than using the old 
formatting string method. However, it is not an ideal way to deal with large strings.
For Example:
"""

name="Jack"
c=5
print("%s is in class %d" %(name,c))

"""
3  String Formatting (str.format)
Python 3 introduced a new way to do string formatting. format() string formatting method 
eliminates the %-operator special syntax and makes the syntax for string formatting more regular. 
str.format() allows multiple substitutions and value formatting. We can use format() to do simple
positional formatting, just like you could with old-style formatting:

In str.format(), we put one or more replacement fields and placeholders defined by a pair 
of curly braces { } into a string.

Syntax: {}.format(values)

"""

str = "This article is written in {} "

print (str.format("Python"))

"""
4 Using f-Strings ( f ):
Python added a new string formatting approach called formatted string literals or "f-strings." 
This is a new way of formatting strings. A much more simple and intuitive solution is the use of 
Formatted string literals.f-string has an easy syntax as compared to previous string formatting
techniques of Python. They are indicated by an "f" before the first quotation mark of a string.
Put the expression inside { } to evaluate the result. Here is a simple example

"""

## declaring variables

str1="Python"

str2="Programming"

print(f"Welcome to our {str1} {str2} tutorial")


# F strings
import math

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)
  
