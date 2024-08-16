from airflow.plugins_manager import AirflowPlugin
from airflow_pulsar_plugin.hooks.pulsar_hook import PulsarHook
from airflow_pulsar_plugin.operators.pulsar_operator import PulsarOperator
from airflow_pulsar_plugin.sensors.pulsar_sensor import PulsarSensor

class AirflowPulsarPlugin(AirflowPlugin):
    name = "pulsar_plugin"
    hooks = [PulsarHook]
    operators = [PulsarOperator]
    sensors = [PulsarSensor]