class CoffeeKiosk:
    def __init__(self, beans_grams, water_ml):
        self.beans = beans_grams
        self.water = water_ml

    def brew_espresso(self):
        if self.beans < 18.00 or self.water < 30.0:
            raise ValueError("Insufficient ingredients!")
        self.beans -= 18.00
        self.water -= 30.0
        