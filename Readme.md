# Readme

## Correr como root

`sudo -E env PATH=$PATH ./sample.py`

## Paquetes

### Sistema

* `libglib2.0-dev`
* `bluetooth bluez*`

### Python

* `pip install -r requirements.txt`

## VENV

Por el amor de Dios, usa un venv.

Teniendo el paquete instalao (`sudo apt install python3-venv`), es tan fácil como ejecutar en la raíz:

> `python3 -m venv venv` (o llamarlo como quieras)

Y activarlo con el `activate` / `deactivate`

## Rootles Bluetooth [OJO QUE NO FUNKA]

Dos cosicas:

* Meter al usuario que tengas en el grupo bluetooth
```
sudo usermod -aG bluetooth caraculo
```

* Meter la siguiente política al `/etc/dbus-1/system.d/bluetooth.conf`
```
<policy user="caraculo">
    <allow send_destination="org.bluez"/>
    <allow send_interface="org.bluez.Agent1"/>
    <allow send_interface="org.bluez.GattCharacteristic1"/>
    <allow send_interface="org.bluez.GattDescriptor1"/>
    <allow send_interface="org.freedesktop.DBus.ObjectManager"/>
    <allow send_interface="org.freedesktop.DBus.Properties"/>
  </policy>
```

## Notas

Parece que las features se añaden al cargar la app. Es decir, parece que no puedo mandar la máscara desde bluetooth. Confirmarlo.

## Rabbit

### Configurarlo

* Instalarlo con apt
* `rabbitmq-plugins enable rabbitmq_management` -> la web
* `rabbitmq-plugins enable rabbitmq_mqtt` -> el mqtt
* `sudo ufw allow 15672` -> ojo la pared de fuego
* `rabbitmqctl add_user user password` -> crear unas credenciales ultraseguras para que te arrepientas de tenerlas en un gitub público
* `rabbitmqctl set_user_tags user administrator` y `rabbitmqctl set_permissions -p / user ".*" ".*" ".*"` -> configurarte el usuario

> Apt y el puerto es en la raspberry; en AWS depende de la distro + firewall y no olvidar los security groups (más abajo)

### Encolar el mqtt

Para pruebas, cada lectura de temperatura se encola en el exchange amq.topic, con el routing key del topic que encolamos

#### PERSISTENCIA

OJO !!

- A nivel de persistencia hay que marcar que los mensajes en las colas (además de ser durable), tengan el delivery_mode = 2. Sin esto da igual que la cola sea durable, ya que por defecto si no el mensaje es de tipo 1 no persistente!!
- Esta configuración la he hecho en el propio bind, pero no parece funcionar si no encolo los mensajes en mqtt con:
-- QoS 1
-- Durable true


En rigor solo lo he probado una vez con las dos opciones, así que igual con una basta


** Queda ver el rendimiento y que no se pierden mensajes **

### Reglas AWS

### Reglas AWS
----
IPv4	Custom TCP	TCP	4369	0.0.0.0/0	epmd
IPv6	Custom TCP	TCP	4369	::/0	epmd
IPv4	Custom TCP	TCP	15674	0.0.0.0/0	–
IPv6	Custom TCP	TCP	15674	::/0	–
IPv6	Custom TCP	TCP	5672	::/0	–
IPv6	Custom TCP	TCP	1883	::/0	–
IPv6	Custom TCP	TCP	8883	::/0	–
IPv6	Custom TCP	TCP	25672	::/0	–
IPv4	Custom TCP	TCP	15672	0.0.0.0/0	–
IPv4	Custom TCP	TCP	5672	0.0.0.0/0	–
IPv4	Custom TCP	TCP	35197	0.0.0.0/0	–
IPv4	Custom TCP	TCP	8883	0.0.0.0/0	–
IPv4	Custom TCP	TCP	15675	0.0.0.0/0	–
IPv6	Custom TCP	TCP	35197	::/0	–
IPv4	Custom TCP	TCP	25672	0.0.0.0/0	–
IPv6	Custom TCP	TCP	15672	::/0	–
IPv4	Custom TCP	TCP	1883	0.0.0.0/0	–
IPv6	Custom TCP	TCP	15675	::/0	–
IPv4	Custom TCP	TCP	3000 - 10000	0.0.0.0/0	Custom range tcp ipv4
IPv4	PostgreSQL	TCP	5432	0.0.0.0/0	PSQL ipv4
IPv4	Custom UDP	UDP	3000 - 10000	0.0.0.0/0	Custom range udp ipv4
IPv4	MYSQL/Aurora	TCP	3306	0.0.0.0/0	MYSQL ipv4
IPv4	HTTPS	TCP	443	0.0.0.0/0	HTTPS ipv4
IPv4	HTTP	TCP	80	0.0.0.0/0	HTTP ipv4
----

## Referencias

* https://github.com/STMicroelectronics/BlueSTSDK_Python
* https://www.st.com/content/dam/AME/2019/technology-tour-2019/minneapolis/presentations/T3S1_Minneapolis_SensorTileBox_HandsOn_A.Vitali.pdf
* https://forum.digikey.com/t/cloud-logging-with-sensortile-box-and-aws/13312
* https://www.hackster.io/felipsz/sensortile-sensor-data-monitoring-using-a-raspberry-pi-7a3663
* https://www.st.com/resource/en/user_manual/dm00550659-getting-started-with-the-bluest-protocol-and-sdk-stmicroelectronics.pdf
* https://stackoverflow.com/questions/12792856/what-ports-does-rabbitmq-use
