import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import uping
from dht import DHT11


led = Pin(2, Pin.OUT)
sensor = DHT11(Pin(15, Pin.IN, Pin.PULL_UP))

station = network.WLAN(network.STA_IF)
station.active(True)

# connection normale
no61 = False
station.connect("SFR_F688","a9leffeadiceracychlo")
while station.isconnected() == False:
	pass

SERVER = '192.168.1.61'
if uping.ping(SERVER)[1]==0:
    station.disconnect()
    print('no 61')
    no61 = True

while station.isconnected() == True:
  pass

if no61:
	# connection tenda si li ping avec 192.168.1.61 a 0 paquets reçus sur 4
	SERVER = '192.168.0.175'
	station.connect("Tenda_8C2A30","existnose620")
	while station.isconnected() == False:
		pass

print('Connection successful')
print(station.ifconfig())

#flash once 
led.value(1)
sleep(0.1)
led.value(0)
sleep(1)

#SERVER = 'node02.myqtthub.com' #MQTT Server address ip = 185.195.98.58 using ping to get
CLIENT_ID = 'ESP8266_sensor'
TOPIC = b'temp_humidity'
USER = 'sensor'
PASSW = 'sensor01'
PORT = 0

#client = MQTTClient(CLIENT_ID, SERVER) #, PORT, USER, PASSW)
client = MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSW)
#print(client)
state = client.connect()
#print(state)

#flash once
led.value(1)
sleep(0.1)
led.value(0)
sleep(1)

#msg = (b'DH11 speaking ....')
#client.publish(TOPIC, msg)

while True:
    try:
        sensor.measure()
        sleep(0.1)
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, int) and isinstance(h, int):
            #msg = (b'0, 0')
            #client.publish(TOPIC, msg)
            msg = (b'{0:3.1f}, {1:3.1f}'.format(t,h))
            client.publish(TOPIC, msg)
            #flash twice
            led.value(1)
            sleep(0.1)
            led.value(0)
            sleep(0.1)
            led.value(1)
            sleep(0.1)
            led.value(0)
            print(msg)
            sleep(20)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
        
        try:
            client.connect()
        except:
            led.value(1)
            sleep(0.1)
            led.value(0)
        
    
