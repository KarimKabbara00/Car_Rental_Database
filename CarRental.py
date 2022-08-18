import pymysql
from datetime import datetime

def carType(x):

   switcher = {
         1: "COMPACT",
         2: "MEDIUM",
         3: "LARGE",
         4: "SUV",
         5: "TRUCK",
         6: "VAN"
      }

   return switcher.get(x)

def boolInput(x):

   if x == 1:
      x="YES"
   elif x == 2:
      x="NO"

   return x

def rentalType(x):

   if x == 1:
      return "Daily"
   elif x == 2:
      return "Weekly"


def calcAmt(cType, rType):

   if rType == "Daily":
      
      retrieve = "Select Daily_Rate from rentalrates where RR_Car_Type = " + "'" + cType + "';"
      cursor.execute(retrieve)
      data = cursor.fetchall()
      
      for i in data:
         rate = float(i[0])

   elif rType == "Weekly":
      
      retrieve = "Select Weekly_Rate from rentalrates where RR_Car_Type = " + "'" + cType + "';"
      cursor.execute(retrieve)
      data = cursor.fetchall()
      
      for i in data:
         rate = float(i[0])/7

   return rate

def compareDates(enteredDate, todayDate):

   if enteredDate > todayDate:
      return 0

   elif enteredDate <= todayDate:
      return 1

##main##
#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="car_rental_database" )
cursor = connection.cursor()

today = datetime.today().strftime('%Y-%m-%d')
Fees = 1.08


UpdateStatus = "Select Start_Date from rental"
cursor.execute(UpdateStatus)
UpdateStatus = cursor.fetchall()
connection.commit()

for i in UpdateStatus: 
   if today == i[0]:
      date = i[0]
      tid = "Select Trans_ID from rental WHERE Start_Date = '" + date + "';"
      cursor.execute(tid)
      tid = cursor.fetchall()

      for j in tid:
         tid = int(j[0])


      updateStatus = "UPDATE rental SET Rental_Status = 'Active' WHERE Trans_ID = '" + str(tid) + "';"
      cursor.execute(updateStatus)
      connection.commit()
      


print("Welcome to the Car Rental Database!")


while(True):
   
   print("\nChoose one of the following: ")
   print("1. Print Databases")
   print("2. Add Customer")
   print("3. Add Car")
   print("4. New Rental")
   print("5. Return Rental")
   print("6. Update Rates")
   print("7. Exit")


   option = int(input("\nOption: "))

   if option == 1:

      print("\nSelect one of the following tables to print:")
      
      while(True):

         print("1. Customers")
         print("2. Cars")
         print("3. Rentals")
         print("4. Rental Rates")
         print("5. Exit")

         choice = int(input("\nChoice: "))

         if choice == 1:
            
            customers = "Select * from customers;"
            cursor.execute(customers)
            data = cursor.fetchall()
            
            print("\n\n\nID", '{0: >10}'.format("Name"), '{0: >27}'.format("Phone Number"))
            print("-------------------------------------------")
            
            for idNo, Name, Phone in data:
               print('{0: <6}'.format(idNo), '{0: <20}'.format(Name), Phone)
               
            print("\n\n")
               
         elif choice == 2:
         
            cars = "Select * from cars;"
            cursor.execute(cars)
            data = cursor.fetchall()

            print("\n\nVehicle ID", '{0: >10}'.format("Type"), '{0: >14}'.format("Make"), '{0: >16}'.format("Model"), '{0: >14}'.format("Year"), '{0: >16}'.format("Available"))
            print("--------------------------------------------------------------------------------------")
            
            for vID, cType, Make, Model, Year, Available in data:
               print('{0: <15}'.format(vID), '{0: <13}'.format(cType), '{0: <17}'.format(Make), '{0: <15}'.format(Model), '{0: <14}'.format(Year), Available)

            print("\n\n")


         elif choice == 3:
            

            rentals = "Select * from rental;"
            cursor.execute(rentals)
            data = cursor.fetchall()
                  
            print("\n\n\n"'{0: <10}'.format("Trans_ID"), '{0: >10}'.format("Customer_ID"), '{0: >12}'.format("Vehicle_ID")
                  , '{0: >13}'.format("Rental_Type"), '{0: >13}'.format("Start_Date"), '{0: >15}'.format("Return_Date")
                  , '{0: >15}'.format("Rental_Length"), '{0: >12}'.format("Amount_Due"), '{0: >15}'.format("Rental_Status"))
            print("----------------------------------------------------------------------------------------------------------------------------")
            
            for Trans_ID, Customer_ID, Vehicle_ID, Rental_Type, Start_Date, Return_Date, Rental_Length, Amount_Due, Rental_Status in data:
               print(Trans_ID, '{0: >10}'.format(Customer_ID), '{0: >13}'.format(Vehicle_ID), '{0: >18}'.format(Rental_Type), '{0: >17}'.format(Start_Date)
                     , '{0: >14}'.format(Return_Date), '{0: >5}'.format(Rental_Length),'{0: >20}'.format(Amount_Due), '{0: >11}'.format(Rental_Status))

            print("\n\n")
            

         elif choice == 4:
         
            rentalRates = "Select * from rentalrates;"
            cursor.execute(rentalRates)
            rentalRates = cursor.fetchall()

            print("\n\nRR_Car_Type", '{0: >18}'.format("Effective_Date"), '{0: >15}'.format("Daily_Rate"), '{0: >16}'.format("Weekly_Rate"))
            print("----------------------------------------------------------------")

            for RR_Car_Type, Effective_Date, Daily_Rate, Weekly_Rate in rentalRates:
               print('{0: <15}'.format(RR_Car_Type), '{0: <19}'.format(Effective_Date), '{0: <15}'.format(Daily_Rate), '{0: <14}'.format(Weekly_Rate))
            
               
            print("\n\n")
            

         elif choice == 5:
            break;
         

         else:
            print("\nInvalid Option.")

   elif option == 2:

      print("\nNew Customer Info")

      maxID = "SELECT MAX(Id_No) AS maximum FROM customers"
      cursor.execute(maxID)
      maxID = cursor.fetchall()

      for i in maxID:
         maximum = int(i[0])
      custID = maximum + 1
      custID = str(custID)


      custName = input("Full Name: ")
      print("\nFormat: (XXX) XXX-XXXX")
      custPhone = input("Phone: ")

      newCust = "INSERT INTO customers (Id_No, Name, Phone) VALUES (%s, %s, %s)"
      values = (custID, custName, custPhone)
      cursor.execute(newCust, values)
      connection.commit()
      print("\nSuccessfully Added New Customer!")


   elif option == 3:

      print("\nNew Car Info")


      maxID = "SELECT MAX(Vehicle_ID) AS maximum FROM cars"
      cursor.execute(maxID)
      maxID = cursor.fetchall()

      for i in maxID:
         maximum = int(i[0])
      vID = maximum + 1
      vID = str(vID)
      
      print("\nCar Type: \n1. Compact\n2. Medium\n3. Large\n4. SUV\n5. Truck\n6. Van")
      cType = int(input("Type: "))
      if cType < 0 or cType > 6:
         print("Error. ")
         continue
      Type = carType(cType)
      
      Make = input("Make: ")
      Model = input("Model: ")
      Year = input("Year: ")

      print("Will the car be available when added?")
      Avail = int(input("1. Yes, 2. No: "))
      Avail = boolInput(Avail)
   
      newCar = "INSERT INTO cars (Vehicle_ID, Car_Type, Make, Model, Year, Available) VALUES (%s, %s, %s, %s, %s, %s)"
      values = (vID, Type, Make, Model, Year, Avail)
      cursor.execute(newCar, values)
      connection.commit()
      print("\nSuccessfully Added New Car!")

      
      
   elif option == 4:

      print("----------------------")
      print("Creating New Rental")
      print("----------------------")


      isEmpty = "SELECT * from rental limit 1"
      cursor.execute(isEmpty)
      result = cursor.fetchall()

      if not result:
         tid = 1

      else:
         isEmpty = "SELECT MAX(Trans_ID) AS maximum FROM rental"
         cursor.execute(isEmpty)
         result = cursor.fetchall()

         for i in result:
            maximum = int(i[0])
         tid = maximum + 1

      
      print("\nSelect the appropriate Customer ID: ")

      customers = "Select * from customers;"
      cursor.execute(customers)
      data = cursor.fetchall()
            
      print("\n\nID", '{0: >10}'.format("Name"), '{0: >27}'.format("Phone Number"))
      print("-------------------------------------------")
            
      for idNo, Name, Phone in data:
         print('{0: <6}'.format(idNo), '{0: <20}'.format(Name), Phone)

      cid = int(input("\nCustomer ID: "))
               
      print("\n\nSelect the appropriate Vehicle ID")
      

      cars = "Select * from cars;"
      cursor.execute(cars)
      data = cursor.fetchall()

      print("\n\nVehicle ID", '{0: >10}'.format("Type"), '{0: >14}'.format("Make"), '{0: >16}'.format("Model"), '{0: >14}'.format("Year"), '{0: >16}'.format("Available"))
      print("--------------------------------------------------------------------------------------")
            
      for vID, cType, Make, Model, Year, Available in data:
         print('{0: <15}'.format(vID), '{0: <13}'.format(cType), '{0: <17}'.format(Make), '{0: <15}'.format(Model), '{0: <14}'.format(Year), Available)
            
               

      vid = int(input("\nVehicle ID: "))

      isAvail = "Select Available from cars WHERE Vehicle_ID = '" + str(vid)+"';"
      cursor.execute(isAvail)
      isAvail = cursor.fetchall()
      for i in isAvail:
         isAvail = i[0]

      if isAvail == "NO":
         print("Car is already being rented!")
         continue

      else:
         cType = "Select Car_Type from cars where Vehicle_ID = " + "'" + str(vid) + "';"
         cursor.execute(cType)
         cType = cursor.fetchall()
         for i in cType:
            cType = i[0]
      
      
      
      print("\n\n")

      print("Select the type of rental: ")
      print("1. Daily\n2. Weekly")

      rType = int(input("Choice: "))
      rType = rentalType(rType)

      if rType == "Daily":
         rLen = int(input("Enter Rental Length in Days: "))

      elif rType == "Weekly":
         rLen = int(input("Enter Rental Length in Weeks: "))
         rLen *= 7 #convert to days

      print("\n\nFormat: YYYY-MM-DD")
      print("Type 'Today' for today's date")
      sDate = input("Enter a Start Date: ")
      if sDate == "Today" or sDate == "today":
            sDate = today


      amtDue = rLen * Fees * calcAmt(cType, rType)


      newRental = "INSERT INTO rental (Trans_ID, Customer_ID, Vehicle_ID, Rental_Type, Start_Date, Return_Date, Rental_Length, Amount_Due, Rental_Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

      if compareDates(sDate, today) == 0:         
         values = (tid, cid, vid, rType, sDate, "0000-00-00", rLen, amtDue, "Scheduled")
         cursor.execute(newRental, values)

      elif compareDates(sDate, today) == 1:         
         values = (tid, cid, vid, rType, sDate, "0000-00-00", rLen, amtDue, "Active")
         cursor.execute(newRental, values)

      #update to 0
      updateStatus = "UPDATE cars SET Available = 'NO' WHERE Vehicle_ID = '" + str(vid)+"';"
      cursor.execute(updateStatus)
      connection.commit()
      print("\nSuccessfully Added New Rental!")



   elif option == 5:

      print("Return a Rental:")

      rentals = "Select * from rental;"
      cursor.execute(rentals)
      data = cursor.fetchall()
            
      print("\n\n\n"'{0: <10}'.format("Trans_ID"), '{0: >10}'.format("Customer_ID"), '{0: >12}'.format("Vehicle_ID")
            , '{0: >13}'.format("Rental_Type"), '{0: >13}'.format("Start_Date"), '{0: >15}'.format("Return_Date")
            , '{0: >15}'.format("Rental_Length"), '{0: >12}'.format("Amount_Due"), '{0: >15}'.format("Rental_Status"))
      print("----------------------------------------------------------------------------------------------------------------------------")
            
      for Trans_ID, Customer_ID, Vehicle_ID, Rental_Type, Start_Date, Return_Date, Rental_Length, Amount_Due, Rental_Status in data:
         print(Trans_ID, '{0: >10}'.format(Customer_ID), '{0: >13}'.format(Vehicle_ID), '{0: >18}'.format(Rental_Type), '{0: >17}'.format(Start_Date)
               , '{0: >14}'.format(Return_Date), '{0: >5}'.format(Rental_Length),'{0: >20}'.format(Amount_Due), '{0: >11}'.format(Rental_Status))
         
         
      print("\n\n")
      retRental = int(input("Trans ID: "))

      

      cid = "Select Vehicle_ID FROM rental WHERE Trans_ID = '" + str(retRental)+ "';"
      cursor.execute(cid)
      cid = cursor.fetchall()
      connection.commit()
      for i in cid:
         cid = i[0]
      

      updateInfo = "UPDATE cars SET Available = 'YES' WHERE Vehicle_ID = '" + str(cid)+"';"
      cursor.execute(updateInfo)
      connection.commit()


      amtDue = "Select Amount_Due from rental WHERE Trans_ID = '" + str(retRental)+"';"
      cursor.execute(amtDue)
      amtDue = cursor.fetchall()
      for i in amtDue:
         amtDue = i[0]
         
      print("Total Amount Due: ", amtDue)


      deleteRental = "DELETE FROM rental WHERE Trans_ID = '" + str(retRental)+ "';"
      cursor.execute(deleteRental)
      connection.commit()
      print("Rental Returned!")


   elif option == 6:

      print("Update Rental Rates:")

      rentalRates = "Select * from rentalrates;"
      cursor.execute(rentalRates)
      rentalRates = cursor.fetchall()

      
      print("\n\nRR_Car_Type", '{0: >18}'.format("Effective_Date"), '{0: >15}'.format("Daily_Rate"), '{0: >16}'.format("Weekly_Rate"))
      print("----------------------------------------------------------------------------")


      for RR_Car_Type, Effective_Date, Daily_Rate, Weekly_Rate in rentalRates:
         print('{0: <15}'.format(RR_Car_Type), '{0: <19}'.format(Effective_Date), '{0: <15}'.format(Daily_Rate), '{0: <14}'.format(Weekly_Rate))


      carT = input("\nEnter Car Type to change: ")

      carT = carT.upper()

      print("\nFormat: YYYY-MM-DD")
      print("Type 'Today' for today's date")
      effDate = input("Enter effective date: ")
   
      if effDate == "Today" or effDate == "today":
            effDate = today
            
      rateType = int(input("\nEnter rate type: \n1. Daily\n2. Weekly\nType: "))
      rateType = rentalType(rateType)
      newRate = input("\nEnter new Rate: ")


      updateStatus = "UPDATE rentalrates SET " + rateType + "_Rate = '" + str(newRate) + "' WHERE RR_Car_Type = '" + carT +"';"
      cursor.execute(updateStatus)
      connection.commit()

      updateDate = "UPDATE rentalrates SET Effective_date = '" + effDate + "' WHERE RR_Car_Type = '" + carT +"';"
      cursor.execute(updateDate)
      connection.commit()


      print("Rate updated!")


   elif option == 7:
      print("Thank you for using the Car Rental Database!")
      break

   else:
      print("Invalid option.")
      
      

connection.commit()
connection.close()
