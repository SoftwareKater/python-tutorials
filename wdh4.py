# You are the IT-specialist of a car rental company. Your boss wants you to program a system, to 
# automatically monitor which cars are rented out and which are available. Your predecessor already 
# startet this project but had to leave the company:

class Car():
	def __init__(self, brand, model, km):
		self.brand = brand
		self.model = model
		self.km = km
		self.available = True

	def rentOut(self):
		self._________ = False

	def returnIn(self, km_driven):
		self.km = self.km + _________
		self.available = True

car1 = Car("Audi", "A3", 102867)
car2 = Car("Fiat", "500", 39860)
car3 = Car("VW", "T5", 156080)

ALL_CARS = [car1, car2, car3]

# a) Fill in the breaks to finish the program.
# b) Mr Smith rents the T5. Call the method rentOut of car3, to complete the renting process.
# c) Boss bought a brand new Audi A8. Instantiate a Car-objekt, to include the new car in the system.
# d) Don't forget to add the new car to the ALL_CARS-list.
# e) Mrs Obstfeld rents the Fiat. 
# f) Mr Smith returns in with the T5, he drove 200 km in total. 
# g) Boss likes your system and wants you to include more stuff: A car needs to be maintained every 20,000 km. 
#	 Write a new method for the Car-class. It should print out a maintenance-warning, if the milometer shows 
#	 a multiple of 20,000.
# h) Mrs Obstfeld returns in with the Fiat 500 after she drove 170 km.
# i) Loop over the ALL_CARS-list to check all cars for maintenance! 
# j) Boss: "I really don not want to miss maintenance deadlines. Why don't we automize the checking on returning 
#	 cars. And please include some buffer, so that we are notified some 200 km before maintenance deadline."
# k) Boss: "No one rents the Audi A3, manipulate its milometer down for a little more attractiveness. Let's say 38,700."
# l) A stranger rents out the A3 and returns it back in. He somehow managed to drive 1,200 km in one day.
# m) Boss remarks that a car could be rented although it is not available. This should not be the case!

# Go to the python documentation and look up the description of the class list. Try out all methods that this class implements.

A = [1, "Uludag", 2.34, 7]
A.append("me")


# Define a class that implements the functionalities of a bottle. 
# (attributes) What are the main characteristics of a bottle? What information do you need to describe a bottle?
# (methods) What can you do with a bottle? 



# Instantiate some bottle objects...



# Fill some bottles with different drinks and drink something...



# Add magic methods to your class that let you compare two bottles. A bottle should be greater than another bottle 
# if it has a higher filling quantity (or if it is actually filled more than the other, as you like). Two bottles 
# should be equal to each other, if they have the same filling quantity. One is greater or equal to another if its 
# filling quantity is greater or equal to the other. (Hint:  __gt__, __eq__ and __ge__)



# Compare some bottle objects. Since you implemented magic methods, you can compare bottles like numbers using the 
# symbols >, >= and ==. 



# For the last programming exercise go back to the car rental system. Extend it to a CRM system!
# a) Create a class Customer having ID, name, contact information and a list of all cars rented by this 
# 	 customer as attributes. The class should also have two methods that allow to manipulate the list 
#	 of all cars rented by a customer: 
#		 1) rentCar, called when customer rents a car, appends the car objet to the list of cars
#		 2) returnCar, called when customer returns a car, deletes the car object from the list of cars. 
# b) Add an attribute renterID to the Car class, where you can save the ID of the customer, if the car is rented out.
# c) Define a function which takes a Car object and a Customer object and rules the process of 
# 	 renting out the given car to the given customer. On success it should print a notification, on failure 
#	 however it should warn the user, that the process was not successful.
