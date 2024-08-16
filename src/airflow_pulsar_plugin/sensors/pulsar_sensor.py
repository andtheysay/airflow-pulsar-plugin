from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults
from airflow_pulsar_plugin.hooks.pulsar_hook import PulsarHook

class PulsarSensor(BaseSensorOperator):
    @apply_defaults
    def __init__(
        self,
        topic,
        pulsar_conn_id='pulsar_default',
        poke_interval=60,
        timeout=60*60,  # 1 hour
        *args,
        **kwargs
    ):
        super().__init__(poke_interval=poke_interval, timeout=timeout, *args, **kwargs)
        self.topic = topic
        self.pulsar_conn_id = pulsar_conn_id
        self.hook = None

    def poke(self, context):
        if not self.hook:
            self.hook = PulsarHook(pulsar_conn_id=self.pulsar_conn_id)
        
        client = self.hook.get_conn()
        consumer = client.subscribe(self.topic, "airflow-sensor-subscription")
        
        try:
            message = consumer.receive(timeout_millis=1000)  # 1 second timeout
            if message:
                consumer.acknowledge(message)
                return True
        except Exception:
            # No message received within the timeout
            pass
        finally:
            consumer.close()
        
        return False

    def execute(self, context):
        # Once poke returns True, we clean up the consumer
        if self.hook:
            self.hook.close_connection()
        return super().execute(context)