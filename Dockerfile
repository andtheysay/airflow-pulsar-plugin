FROM docker.io/apache/airflow:2.9.3-python3.12

# Install packages in one layer to reduce image size
RUN pip3 install --no-cache-dir \
    requests \
    scdl \
    osrsreboxed \
    numpy \
    pulsar-client[all] \
    pycouchdb

# Copy pulsar files
COPY src/airflow_pulsar_plugin/ /opt/airflow/include/

# Set env variable PYTHONPATH to /opt/airflow/include
ENV PYTHONPATH "/opt/airflow/include/"