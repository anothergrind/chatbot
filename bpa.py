# ChatBot Introduction
print("I'm Noel, a chatbot that works for the Wolves Dealership")
print("First off, I would like to thank you for using visiting our Dealership")
print("I can help you with any questions that you have about the Dealership")

print("---------------------------------------------------------------------")
print()

def chatbot():
    # This inventory array basically holds important info about all of the cars
    inventory = [
        {"make": "Honda", "model": "Civic", "year": 2019, "color": "black", "price": 21000},
        {"make": "Toyota", "model": "Camry", "year": 2023, "color": "silver", "price": 23000},
        {"make": "Ford", "model": "F-150", "year": 2022, "color": "blue", "price": 19000},
        {"make": "Toyota", "model": "RAV-4", "year": 2018, "color": "red", "price": 17000},
        {"make": "Ford", "model": "Fusion", "year": 2016, "color": "white", "price": 16000},
        {"make": "Toyota", "model": "Corolla Hybrid", "year": 2014, "color": "black", "price": 11000},
        {"make": "Toyota", "model": "Prius Prime", "year": 2023, "color": "grey", "price": 21000},
        {"make": "Chevrolet", "model": "Silverado", "year": 2019, "color": "black", "price": 34000},
        {"make": "Honda", "model": "CR-V", "year": 2022, "color": "blue", "price": 30000},
        {"make": "Toyota", "model": "Tacoma", "year": 2023, "color": "orange", "price": 27000},
    ]
        
while True:
    user_input = input()

    # Checks if the users input has any one of the key words 
    # Ex: "sedans" or "suvs"
    if "cars" in user_input:
        print("We have a wide variety of cars available, including sedans, SUVs, and pick-up trucks")
        print("What type of car are you interested in? Sedans, SUVS, or Trucks?")
        car_type = input()
        if car_type == "sedans":
            print("We have a great selection of sedans, including")
        elif car_type == "suvs":
            print("We have a great selection of SUVs including")
        elif car_type == "trucks": 
            print("We have a great selection of trucks including the Ford F-150, Chevrolet Silvlerado, and Toyota Tacoma")
        elif "sales representative" in user_input: 
            print("Our sales representatives are available to answer any questions you may have. You can reach them at 512-555-5555")
        elif "hours" in user_input: 
            print("Our hours of operation are Monday-Friday: 9 AM to 9 PM and Saturday-Sunday: 10 AM to 8 PM.")
        elif "search" in user_input: 
            print("What type of car are you interested in?")
            model = input()
            found = False 
            for car in inventory: 
                if car["model"] == model:
                    print(f"{car['make']} {car['year']} {car['color']} {car['price']}")
                    found = True
                if not found:
                    print(f"Sorry, we don't have any {model} in our inventory.")
        elif search_critieria == "year":
            print("What year are your interested in searching for?")
            year = input()
            found = False 
            for car in inventory: 
                if car["year"] == year: 
                    print(f"{car['make']} {car['model']} {car['color']} {car['price']}")
                found = True 
            if not found: 
                print(f"Sorry, we don't have any cars from {year} in our inventory.")
        elif search_criteria == "color":
            print("What color are you interested in searching for?")
            color = input()
                
