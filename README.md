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
