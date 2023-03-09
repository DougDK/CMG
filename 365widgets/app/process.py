import re
from thermometer import Thermometers
from humidity import Humidities

TIMESTAMP_PATTERN = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$'
ROOM_VALUES_LENGTH = 3
ROOM_VALUES_DEGREE_INDEX = 1
ROOM_VALUES_HUMIDITY_INDEX = 2
SENSOR_SECTION_LENGTH = 2
SENSOR_FIRST_INDEX = 0
SENSOR_SECOND_INDEX = 1

sample_output = dict()
thermometers = Thermometers()
humidities = Humidities()

def parser(file_name):
    with open(file_name) as f:
        room_degree = None
        relative_humidity = None
        sensor_type = None
        sensor_name = None
        time = None
        values = []
        for line in f:
            splited = line.rstrip('\n').split(' ')
            if(len(splited)==ROOM_VALUES_LENGTH):
                room_degree = splited[ROOM_VALUES_DEGREE_INDEX]
                relative_humidity = splited[ROOM_VALUES_HUMIDITY_INDEX]
            if(len(splited)==SENSOR_SECTION_LENGTH):
                # Check if it is a Sensor (<type><name>) or a Reading (<time><value>)
                if(re.match(TIMESTAMP_PATTERN, splited[SENSOR_FIRST_INDEX])): # Reading
                    time = splited[SENSOR_FIRST_INDEX]
                    values = splited[SENSOR_SECOND_INDEX:]
                    message = "{} {} {} {} {} {}".format(
                        time,
                        room_degree,
                        relative_humidity,
                        sensor_type,
                        sensor_name,
                        " ".join(values))
                    if(sensor_type=="thermometer"):
                        thermometers.handle(message)
                    if(sensor_type=="humidity"):
                        humidities.handle(message)

                else: # Sensor
                    sensor_type = splited[SENSOR_FIRST_INDEX]
                    sensor_name = splited[SENSOR_SECOND_INDEX]