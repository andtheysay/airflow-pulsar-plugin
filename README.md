# Airflow Pulsar Plugin

This plugin integrates Apache Pulsar with Apache Airflow, allowing you to interact with Pulsar topics and manage Pulsar-related tasks within your Airflow DAGs.

## Features

- Create Pulsar producers and consumers in Airflow tasks
- Send messages to Pulsar topics
- Consume messages from Pulsar topics
- Custom Pulsar operators for common Pulsar operations

## Installation

To install the Airflow Pulsar Plugin, run:

```bash
pip install airflow-pulsar-plugin
```

## Configuration

Add the following to your Airflow configuration file (`airflow.cfg`):

```
[pulsar]
pulsar_admin_url = http://localhost:8080
pulsar_service_url = pulsar://localhost:6650
```

Replace the URLs with your Pulsar cluster's admin and service URLs.

## Usage

Here's a simple example of how to use the Airflow Pulsar Plugin in your DAG:

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow_pulsar_plugin.operators.pulsar_produce_operator import PulsarProduceOperator

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'pulsar_example_dag',
    default_args=default_args,
    description='A simple DAG using Pulsar operators',
    schedule_interval=None,
)

send_message = PulsarProduceOperator(
    task_id='send_message_to_pulsar',
    topic='my-topic',
    message='Hello, Pulsar!',
    dag=dag,
)

send_message
```

This DAG creates a task that sends a message to a Pulsar topic.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).