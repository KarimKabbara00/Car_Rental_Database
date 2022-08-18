# Car_Rental_Database
Car Rental Database that allows for adding customers/cars, and scheduling/returning rentals into a SQL database that uses python for interaction.

The source code assumes the following:

	-pymysql is installed on the system:
		import pymysql is required to 
		establish a connection from 
		source code to database. 


	-When establishing a connection: 

		1. host="localhost"
		2. user="root"
		3. passwd=""
		4. database="car_rental_database"


	-The system date is accurate:
		
		The source code utilizes the current
		system's date to make calculations 
		such as whether or not a rental is active
		or scheduled in the future.  
