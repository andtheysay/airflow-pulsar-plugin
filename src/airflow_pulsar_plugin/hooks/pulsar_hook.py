from airflow.hooks.base import BaseHook
import pulsar

class PulsarHook(BaseHook):
    def __init__(self, pulsar_conn_id='pulsar_default'):
        super().__init__()
        self.pulsar_conn_id = pulsar_conn_id
        self.client = None

    def get_conn(self):
        if self.client is None:
            conn = self.get_connection(self.pulsar_conn_id)
            pulsar_url = f"pulsar://{conn.host}:{conn.port}"
            self.client = pulsar.Client(pulsar_url)
        return self.client

    def get_producer(self, topic):
        return self.get_conn().create_producer(topic)

    def send_message(self, topic, message):
        with self.get_producer(topic) as producer:
            producer.send(message.encode('utf-8'))

    def close_connection(self):
        if self.client:
            self.client.close()
            self.client = None