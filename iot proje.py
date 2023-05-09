import Adafruit_DHT
import time
import board
import adafruit_bmp280

# Sensör pimlerini tanımlama
dht_pin = 4
bmp_sda = board.SDA
bmp_scl = board.SCL

# Sıcaklık, nem ve basınç eşiklerini belirleme
threshold_temp = 20
threshold_humid = 50
threshold_pressure = 1013.25

# Sensörleri tanımlama
dht_sensor = Adafruit_DHT.DHT11
bmp_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)


while True:
    # Sensör değerlerini okuma
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    pressure = bmp_sensor.pressure
    
    # Ortam sıcaklığı ve basıncını ölçme
    bmp_sensor.sea_level_pressure = pressure
    altitude = bmp_sensor.altitude
    
    # Sensör değerleri uygun değilse
    if humidity is None or temperature is None or temperature > threshold_temp or humidity > threshold_humid or pressure < threshold_pressure:
        print("Meyve-sebze reyonunda uygun olmayan sıcaklık, nem veya basınç değeri tespit edildi!")
        
        # Uyarı mesajı gönderme işlemi
        # Uyarı mesajını belirli bir kanala veya sunucuya gönderme
        print("Meyve-sebze reyonunda belirli bir sıcaklık, nem veya basınç eşiğinin altında olan meyve tespit edildi!")
        print("Sıcaklık: ", temperature, "°C")
        print("Nem: ", humidity, "%")
        print("Basınç: ", pressure, "hPa")
        print("Rakım: ", altitude, "m")
        
    time.sleep(1)
