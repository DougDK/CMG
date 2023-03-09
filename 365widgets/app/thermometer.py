import math

class Thermometer:
    old_average = 0
    old_variance = 0
    n = 0

    def __init__():
        return

    def evaluate_static(values):
        average = sum(values)/len(values)

    def evaluate(message):
        global n, old_average, old_variance

        splited = message.split(" ")
        known_temperature = splited[1]
        new_value = splited[5]
        
        n += 1
        new_average = old_average*(n-1)/n + new_value/n
        new_variance = (n-1)/n * (old_variance + (old_average - new_value)**2/n)
        standard_deviation = math.sqrt(new_variance)

        if(abs(new_average-known_temperature)<0.5 and standard_deviation<3):
            qc_evaluation = "ultra precise"
        if(abs(new_average-known_temperature)<0.5 and standard_deviation<5):
            qc_evaluation = "very precise"
        else:
            qc_evaluation = "precise"

        old_average = new_average
        old_variance = new_variance
        return qc_evaluation
