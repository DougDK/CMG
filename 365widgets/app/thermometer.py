import math

class Thermometers:
    dict_thermometers = dict()
    def __init__(self):
        return
    
    def handle(self, message):
        splited = message.split(" ")
        known_temperature = splited[1]
        thermometer_name = splited[4]
        thermometer_value = splited[5]
        thermometer = self.dict_thermometers.get(thermometer_name)
        if (not thermometer):
            thermometer = Thermometer(thermometer_name)
            self.dict_thermometers.update({thermometer_name: thermometer})
        thermometer.evaluate_live(known_temperature, thermometer_value)
        return


class Thermometer:
    name = None
    old_average = 0
    old_variance = 0
    n = 0

    def __init__(self, name):
        self.name = name
        return
    
    def __quality_control(self, average, standard_deviation, known_temperature):
        if(abs(average-known_temperature)<0.5 and standard_deviation<3):
            qc_evaluation = "ultra precise"
        if(abs(average-known_temperature)<0.5 and standard_deviation<5):
            qc_evaluation = "very precise"
        else:
            qc_evaluation = "precise"
        return qc_evaluation

    def evaluate_static(self, known_temperature, values):
        n = len(values)
        average = sum(values)/n

        standard_deviation = [(x - average) ** 2 for x in values]

        qc_evaluation = self.__quality_control(average, standard_deviation, known_temperature)

        return qc_evaluation

    def evaluate_live(self, known_temperature, new_value):
        global n, old_average, old_variance
        
        n += 1
        new_average = old_average*(n-1)/n + new_value/n
        new_variance = (n-1)/n * (old_variance + (old_average - new_value)**2/n)
        standard_deviation = math.sqrt(new_variance)

        qc_evaluation = self.__quality_control(new_average, standard_deviation, known_temperature)

        old_average = new_average
        old_variance = new_variance
        return qc_evaluation
