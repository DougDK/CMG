class Humidities:
    dict_humidities = dict()
    def __init__(self):
        return

    def handle(self, message):
        splited = message.split(" ")
        known_humidity = float(splited[2])
        humidity_name = splited[4]
        humidity_value = float(splited[5])
        humidity = self.dict_humidities.get(humidity_name)
        if (not humidity):
            humidity = Humidity(humidity_name)
            self.dict_humidities.update({humidity_name: humidity})
        humidity.evaluate_live(known_humidity, humidity_value)
        return

    def get_values(self):
        return {key: value.current_qc_evaluation for key,value in self.dict_humidities.items()}

class Humidity:
    name = None
    old_average = 0
    n = 0
    current_qc_evaluation = None

    def __init__(self, name):
        self.name = name
        return
    
    def  __quality_control(self, average, known_humidity):
        if(abs(average-known_humidity)<=1):
            return "keep"
        else:
            return "discard"

    def evaluate_static(self, known_humidity, values):
        n = len(values)
        average = sum(values)/n

        qc_evaluation = self.__quality_control(average, known_humidity)

        return qc_evaluation
    
    def evaluate_live(self, known_humidity, new_value):
        self.n += 1
        new_average = self.old_average*(self.n-1)/self.n + new_value/self.n
        self.current_qc_evaluation = self.__quality_control(new_average, known_humidity)
        self.old_average = new_average
        return self.current_qc_evaluation