## Main.py:

This script can add new users to the credential databases and, provided the right credentials, can check whether a credit card number exists.

It requires a main argument: “add” or “validate”, which determines whether the code will work in “add new user” mode or “validate CC number code”, and some mandatory arguments.

In “add” mode:

  -a: username of the new user to be added
    
  -p: password of the new user to be added

In “validate” mode:
 
  -u: username for login
    
  -p: password for login
    
  -cn: card number to validate
   
  -v (optional): whether to work in verbosity or non verbosity mode
    
Moreover, a "test" mode is present in order to allow the code in the test_main.py to run, since it does not require credentials to validate the credit card number. 


## Dbmanager.py:

This script can check the user existence in the database or create the databases themselves.

It works with three arguments (two of which required):

  -a: username of the new user to add
    
  -u: username of the already existing user
    
  -p: password of the already-existing user or of the newly created one

Depending on whether -a or -u is provided, the script will add or check the existence of a user.

## Test_main.py

This script contains the routine to follow in order to automate the code test. 

It is composed of four functions which are called in the following order:

  - “setUp”, which checks for the existence of the temporary folder in which to save temporary files for testing. If it exists, it            deletes it along with all the content. If not, it just creates it.
    
  - “check_invalid_entries”, which gives card numbers at the validation program and saves the outputs to a temporary file in the              temporary folder, then it opens that file and reads if the content is "unknown". If it's not, it raises an error.
    
  - “check_valid_entries”, which basically does the same thing as the previous function but with valid card numbers. If a value that          is not expected is saved in the file, then the code raises an error.
    
  - “tearDown”, which removes the temporary folder with all its files.

Note that the code does not test all the card numbers, since in order to test all numbers from 000000 to 999999 it would have taken a long time to run, thus a step of 1000 is considered.

