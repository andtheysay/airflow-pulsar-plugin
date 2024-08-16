FROM docker.io/apache/airflow:2.9.3-python3.12

# Create folders
RUN mkdir -p /opt/airflow/include/custom_operators && \
    mkdir -p /opt/airflow/include/custom_hooks

# Install packages in one layer to reduce image size
RUN pip3 install --no-cache-dir \
    requests \
    scdl \
    osrsreboxed \
    numpy \
    pulsar-client[all]

# Download and extract the latest plugin version
RUN LATEST_URL=$(curl -s https://api.github.com/repos/andtheysay/airflow-pulsar-plugin/releases/latest | grep "tarball_url" | cut -d '"' -f 4) && \
    curl -L ${LATEST_URL} | tar -xz -C /tmp && \
    mv /tmp/yourusername-airflow-pulsar-plugin-*/src/airflow_pulsar_plugin/* /opt/airflow/include/ && \
    rm -rf /tmp/yourusername-airflow-pulsar-plugin-*

# Set env variable PYTHONPATH to /opt/airflow/include
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/include"