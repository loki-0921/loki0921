class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.brand} {self.model} engine started.")
        else:
            print("Engine is already running.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            self.speed = 0  # Speed resets when engine stops
            print(f"{self.brand} {self.model} engine stopped.")
        else:
            print("Engine is already off.")

    def accelerate(self, amount):
        if self.engine_on:
            self.speed += amount
            print(f"{self.brand} {self.model} accelerated. Current speed: {self.speed} km/h")
        else:
            print("Start the engine first.")

    def brake(self, amount):
        if self.speed > 0:
            self.speed -= amount
            if self.speed < 0:
                self.speed = 0
            print(f"Braked. Current speed: {self.speed} km/h")
        else:
            print("Car is already stationary.")

    def display_info(self):
        print(f"--- CAR INFORMATION ---")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")
        print(f"Speed : {self.speed} km/h")
        print(f"Engine: {'On' if self.engine_on else 'Off'}")
        print("------------------------")


# Example Usage
car1 = Car("Tesla", "Model S", 2023)

car1.display_info()
car1.start_engine()
car1.accelerate(30)
car1.brake(10)
car1.stop_engine()
