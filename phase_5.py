import paho.mqtt.client as mqtt
import ssl
import json

broker_address = "a3lafbeca71eu5-ats.iot.ap-southeast-1.amazonaws.com"
port = 8883
topic = "bai-kiem-tra-cuoi-ky"

ca_cert = "root_ca.pem"
certfile = "certificate.crt"
keyfile = "private_key.key"

def on_message(client, userdata, message):
    payload = json.loads(message.payload)  
    process_image(payload)

def process_image(image_data):
    print("Received image data:", image_data)

client = mqtt.Client()

# Set up TLS/SSL certificate based authentication
client.tls_set(ca_certs=ca_cert, certfile=certfile, keyfile=keyfile, cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLS, ciphers=None)

client.on_message = on_message

client.connect(broker_address, port=port)

client.subscribe(topic)

client.loop_forever()
