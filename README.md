# PASSWORD_LOCKER

## AUTHOR
 [SHARON KEMBOI]

## DESCRIPTION
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## USER STORIES
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* To create an account with my details - log in and password
* Store my existing login credentials

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./passwordlocker.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## setup

* In your terminal:
        
        $ git clone https://github.com/sharon002/password_locker.git
       
## RUN THE APPLICATION
* To run the Application, in your terminal
  $ chmod +x run.py
  $ ./run.py

## TESTING APLICATION
* To run the application for the class file:
   
    $ python3.8 test_passwordlocker.py 

## Technologies Used
python3.8

## Licence
MIT &copy;2021 [SHARON KEMBOI]
