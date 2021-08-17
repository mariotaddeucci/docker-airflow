PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
AIRFLOW_VERSION=$1
echo $1
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Install custom python package if requirements.txt is present
if [ -e "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# initialize the database
airflow db init

airflow users create \
    --username airflow \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --password airflow \
    --email airflow@airflow.no.reply
