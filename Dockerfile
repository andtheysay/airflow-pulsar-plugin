FROM docker.io/apache/airflow:2.9.3-python3.12

# Create folders
RUN mkdir -p /opt/airflow/include/custom_operators && \
    mkdir -p /opt/airflow/include/custom_hooks && \
    mkdir -p /opt/airflow/include/custom_sensors

# Install packages in one layer to reduce image size
RUN pip3 install --no-cache-dir \
    requests \
    scdl \
    osrsreboxed \
    numpy \
    pulsar-client[all]

# Copy pulsar files
COPY src/pulsar_operator.py /opt/airflow/include/custom_operators/
COPY src/pulsar_hook.py /opt/airflow/include/custom_hooks/
COPY src/pulsar_sensor.py /opt/airflow/include/custom_sensors/

# Set env variable PYTHONPATH to /opt/airflow/include
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/include"