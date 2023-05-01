from prefect import task, flow, get_run_logger
from data_validation import general_data_validation
from tiled.client import from_profile
from export import export

@task
def log_completion():
    logger = get_run_logger()
    logger.info("Complete")


@flow
def end_of_run_workflow(stop_doc):
    uid = stop_doc["run_start"]
    data_validation(uid)
    export(uid)
    log_completion()
