import logging
import os
from datetime import datetime


def initialize_logger():
    """Initialize custom logger settings, log folder and file structure."""
    # Create a folder for the logs
    log_path = "./logs"

    # Check for the Log directory, if not, attempt to make one
    if not os.path.isdir(log_path):

        try:
            os.mkdir(log_path)
        except OSError:
            print("Failed to create log directory.")
        else:
            print("Successfully created log directory.")

    # Create the log file for today
    date_format = datetime.now().strftime("%Y-%m-%d")
    log_file_name = log_path + "/" + date_format + ".log"

    file_exists = os.path.isfile(log_file_name)

    # Configure logger with file for today, format, minimum level logging.DEBUG
    logging.basicConfig(filename=log_file_name, format="%(asctime)s - %(levelname)s: %(message)s",
                        level=logging.DEBUG)

    logging.getLogger().addHandler(logging.StreamHandler())

    if not file_exists:
        logging.info("Log initialized.")
    else:
        logging.info("Logger re-initialized with existing log.")
