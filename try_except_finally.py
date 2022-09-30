# https://www.geeksforgeeks.org/built-exceptions-python/
'''
Exception       Description
IndexError      When the wrong index of a list is retrieved.
AssertionError  It occurs when the assert statement fails
AttributeError  It occurs when an attribute assignment is failed.
ImportError     It occurs when an imported module is not found.
KeyError        It occurs when the key of the dictionary is not found.
NameError       It occurs when the variable is not defined.
MemoryError     It occurs when a program runs out of memory.
TypeError       It occurs when a function and operation are applied in an incorrect type.
'''

dicto={'key':'ok found key'}

try:
    print("Performing an action which may throw an exception.")
    print(dicto['key'])  # ok
    #print(dicto['key2'])
    raise KeyError('key not found')
except KeyError as error:
    print ("An exception was thrown!")
    print ('Key error:',str(error))
else:
    print ("Everything looks great!")
finally:
    print ("Finally is called directly after executing the try statement whether an exception is thrown or not.")