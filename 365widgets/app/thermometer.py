import math

class Thermometers:
    dict_thermometers = dict()
    def __init__(self):
        return
    
    def handle(self, message):
        splited = message.split(" ")
        known_temperature = float(splited[1])
        thermometer_name = splited[4]
        thermometer_value = float(splited[5])
        thermometer = self.dict_thermometers.get(thermometer_name)
        if (not thermometer):
            thermometer = Thermometer(thermometer_name)
            self.dict_thermometers.update({thermometer_name: thermometer})
        thermometer.evaluate_live(known_temperature, thermometer_value)
        return
    
    def get_values(self):
        return {key: value.current_qc_evaluation for key,value in self.dict_thermometers.items()}


class Thermometer:
    name = None
    old_average = 0
    old_variance = 0
    n = 0
    current_qc_evaluation = None

    def __init__(self, name):
        self.name = name
        return
    
    def __quality_control(self, average, standard_deviation, known_temperature):
        if(abs(average-known_temperature)<=0.5 and standard_deviation<3):
            return "ultra precise"
        elif(abs(average-known_temperature)<=0.5 and standard_deviation<5):
            return "very precise"
        else:
            return "precise"
    
    def evaluate_static(self, known_temperature, values):
        n = len(values)
        average = sum(values)/n

        standard_deviation = [(x - average) ** 2 for x in values]

        qc_evaluation = self.__quality_control(average, standard_deviation, known_temperature)

        return qc_evaluation

    def evaluate_live(self, known_temperature, new_value):
        self.n += 1
        new_average = self.old_average*(self.n-1)/self.n + new_value/self.n
        new_variance = (self.n-1)/self.n * (self.old_variance + (self.old_average - new_value)**2/self.n)
        standard_deviation = math.sqrt(new_variance)

        self.current_qc_evaluation = self.__quality_control(new_average, standard_deviation, known_temperature)

        self.old_average = new_average
        self.old_variance = new_variance
        return self.current_qc_evaluation
