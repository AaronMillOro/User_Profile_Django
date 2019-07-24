# User Profile with Django

This project describes a form that was built to record personal details of a registered user and displays that information on a profile page. 
## Project details
* The **profile page** is visible once the user has logged in.

* The profile includes **first name, last name, email, date of birth, short bio and the option to upload an avatar**.

* There is a validation set up for email, date of birth and the biography:
	* The **Date of Birth** form accepts three date formats: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY. 
	* The **Email** validation checks if the email addresses match and are in a valid format. 
	* The **Bio** validation checks that this fields contains more than 10 characters and that properly escapes HTML formatting (filter explicity added).
	
* There is a **"change password"** page that updates the user’s password. This page will ask for **current password, new password and confirm password** fields. 

* A **password validation** was implemented and verifies that:
	* current password is valid 
	* the new password and confirm password fields match
	* the new password follows these rules:
	
		1. Must not be the same as the current password
		2. Minimum password length of 14 characters
 		3. Must use of both uppercase and lowercase letters
		4. Must include of one or more numerical digits
		5. Must include of special characters, such as @, #, $
		6. Cannot contain the username or parts of the user’s full name, such as his first name

## Test the app in terminal
1. Set the repertory **User_Profile_Django/**, install and run pipenv.

		> pipenv install
		
		> pipenv shell

2. Download the corresponding dependencies in the virtual environment. 

		> pip install -r requirements.txt
		
		> pipenv graph

3. In the root directory (User_Profile_Django/user_profile_django/) run the application.
		
		> python3 manage.py runserver 0.0.0.0:5000

4. Open your favorite web browser and type:

		http://localhost:5000/

5. You can Sign in with a pre-loade profile :

		User : ArminVanBuuren
		Password: A$tateOFtrance2019


Enjoy! :shipit: