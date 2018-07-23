import logging
import pika
import ssl

logging.basicConfig(level=logging.INFO)
context = ssl.create_default_context(
    cafile="./client_certs/req.pem")
context.load_cert_chain("./client_certs/cert.pem",
                        "./client_certs/key.pem")
ssl_options = pika.SSLOptions(context, "10.15.208.89")
conn_params = pika.ConnectionParameters(port=5671,
                                        ssl_options=ssl_options)

with pika.BlockingConnection(conn_params) as conn:
    ch = conn.channel()
    ch.queue_declare("foobar")
    ch.publish("", "foobar", "Hello, world!")
    print(ch.basic_get("foobar"))
