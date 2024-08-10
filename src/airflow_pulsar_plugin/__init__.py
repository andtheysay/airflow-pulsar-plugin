from airflow.plugins_manager import AirflowPlugin
from airflow_pulsar_plugin.hooks.pulsar_hook import PulsarHook
from airflow_pulsar_plugin.operators.pulsar_operator import PulsarOperator

class AirflowPulsarPlugin(AirflowPlugin):
    name = "pulsar_plugin"
    hooks = [PulsarHook]
    operators = [PulsarOperator]