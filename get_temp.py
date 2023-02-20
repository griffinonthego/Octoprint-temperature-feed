import board
import adafruit_dht
import time

dhtDevice = adafruit_dht.DHT11(board.D4)

def get_data():
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = ("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
        print(data)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)

    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)






