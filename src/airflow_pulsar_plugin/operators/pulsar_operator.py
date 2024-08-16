from airflow.utils.decorators import apply_defaults
from airflow.models import BaseOperator
from hooks.pulsar_hook import PulsarHook

class PulsarOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        topic,
        message,
        pulsar_url=None,
        pulsar_conn_id='pulsar_default',
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.topic = topic
        self.message = message
        self.pulsar_url = pulsar_url
        self.pulsar_conn_id = pulsar_conn_id

    def execute(self, context):
        hook = PulsarHook(pulsar_url=self.pulsar_url, pulsar_conn_id=self.pulsar_conn_id)
        hook.send_message(self.topic, self.message)
        hook.close_connection()