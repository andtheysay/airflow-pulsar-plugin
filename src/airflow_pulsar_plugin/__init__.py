from airflow.plugins_manager import AirflowPlugin
from custom_hooks.pulsar_hook import PulsarHook
from custom_operators.pulsar_operator import PulsarOperator
from custom_sensors.pulsar_sensor import PulsarSensor

class AirflowPulsarPlugin(AirflowPlugin):
    name = "pulsar_plugin"
    hooks = [PulsarHook]
    operators = [PulsarOperator]
    sensors = [PulsarSensor]