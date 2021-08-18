from subprocess import Popen
from os import path
import yaml


def load_secrets():
    if not path.exists("connections.yaml"):
        return

    with open("connections.yaml", "r") as stream:
        for conn_id, config in yaml.safe_load(stream).items():
            if isinstance(config, str):
                yield f"{conn_id} --conn-uri {config}"
            elif isinstance(config, dict):
                params = " ".join(
                    (
                        f"--conn-{k.replace('conn_', '')} {config[k]}"
                        for k in config.keys()
                    )
                )
                yield f"{conn_id} {params}"


# Install requirements
if path.exists("requirements.txt"):
    Popen("pip install -r requirements.txt", shell=True).wait()

processes = [
    Popen(f"airflow connections add {c}", shell=True) for c in load_secrets()]
[p.wait() for p in processes]

# Start Airflow
commands = [
    "webserver",
    "scheduler",
]
processes = [Popen(f"airflow {c}", shell=True) for c in commands]
[p.wait() for p in processes]
