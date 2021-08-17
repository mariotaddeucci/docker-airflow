ARG PYTHON_V=3.7
ARG AIRFLOW_V=2.1.2
FROM python:$PYTHON_V

RUN echo $PYTHON_V       
RUN echo $AIRFLOW_V  

ENV AIRFLOW_HOME=/
ENV AIRFLOW_VERSION=$AIRFLOW
ENV PYTHON_VERSION=$PYTHON_V
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

WORKDIR ${AIRFLOW_HOME}

ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

COPY ./script/ .

CMD ["python", "start.py"]
