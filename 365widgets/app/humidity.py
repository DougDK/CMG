class Humidities:
    dict_humidities = dict()
    def __init__(self):
        return

    def handle(self, message):
        splited = message.split(" ")
        known_humidity = splited[2]
        humidity_name = splited[4]
        humidity_value = splited[5]
        humidity = self.dict_humidities.get(humidity_name)
        if (not humidity):
            humidity = Humidity(humidity_name)
            self.dict_humidities.update({humidity_name: humidity})
        humidity.evaluate_live(known_humidity, humidity_value)
        return

class Humidity:
    name = None
    def __init__(self, name):
        self.name = name
        return
    
    def evaluate_static(self, values):
        return
    
    def evaluate_live(self, known_humidity, new_value):
        return "keep" # or discard