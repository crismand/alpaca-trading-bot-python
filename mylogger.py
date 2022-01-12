
import logging
import os
from datetime import datetime

# Create a folder for the logs
try:
    log_path = "./logs"
    os.mkdir(log_path)
except OSError:
    print("Log directory already exists.")
else:
    print("Successfully created log directory.")

# Create the log file for today
log_file = datetime.now().strftime("%Y-%m-%d.log")

# Configure logger with file for today, format, minimum level logging.DEBUG
logging.basicConfig(filename=log_path + "/" + log_file, format="%(asctime)s - %(levelname)s: %(message)s",
                    level=logging.DEBUG)

logging.getLogger().addHandler(logging.StreamHandler())

logging.info("Log initialized.")



