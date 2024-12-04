#create dictionary for cars

cars = {

    "Toyota":"Blue",
    "Mazda":"Green",
    "Benz":"White"


}

#methods belonging to dictionary
print(cars)

print(cars["Mazda"])

print(cars.keys()) #first value is the key
print(cars.values())
print(cars.items())

## add new car to dictionary

cars["Ford"] = "Black"
print(cars)

#this can also add a car to a dictionary
cars["VW"] = input("Enter the colour of the car: ")
print(cars)