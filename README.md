## Implementation of the Luhn algorithm

A Credit Card (CC) number is made of 16 digits, the first 6 numbers identify the issuer of the CC, the next 9 numbers identify the account number, the last number is to check the validity of the number (a checksum). Not every 16-digit number is a valid credit card number, and the Luhn algorithm checks that the number is valid. You can find the algorithm defined in this [Wikipedia page](https://en.wikipedia.org/wiki/Luhn_algorithm). 


In this repository you can find a file named ```luhn.py``` that implements the ```isLuhnValid()``` function. This function is used in the ```main.py``` file to test two numbers. If you run the program, executing the main file with: ```python main.py``` it will  give you the results of the test on two CC numbers. One is correct, the other is not. 

The program also contains a small list of issuers, each one with its own range of allowed prefixes. It will try to verify if the given CC falls in the range allocated to a known issuer.


```
$ python main.py
The number that was given as input:4556194895263730 is a valid CC number
The issuer is: Visa
The number that was given as input:8556194895263730 is not a valid CC number
The issuer is: unknown
```



## Credits:

Code is taken from the nice [practice Python](https://www.practicepython.org/) website from Michele Pratusevich and is released with a [CC-BY](https://www.practicepython.org/about/) license.




## Main.py:

This script can add new users to the credential databases and, provided the right credentials, can check whether a credit card number exist.

It requires a main argument: “add” or “validate”, which determines whether the code will work in “add new user” mode or “validate CC number code”, and some mandato arguments.

In “add” mode:
    -a: username of the new user to be added
    -p: password of the new user to be added

In “validate” mode:
    -u: username for login
    -p: password for login
    -cn: card number to validate
    -v (optional): whether to work in verbosity or non verbosity mode


## Dbmanager.py:

This script can check the user existence to db or create the databases themselves.

It works with three arguments (two of which required):
    -a: username of the new user to add
    -u: username of the already existing user
    -p: password of the already-existing user or of the negli-create one

Depending on whether -a or -u is provided, the script will add or check the existence of a user.


