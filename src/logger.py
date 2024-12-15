import os
import logging 
from datetime import datetime

log_file =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"
log_dir_path = os.path.join(os.getcwd(), "logs", log_file)
os.makedirs(log_dir_path, exist_ok=True)

log_file_path = os.path.join(log_dir_path, log_file)

logging.basicConfig(

    filename=log_file_path,
    format ='[%(asctime)s] - %(lineno)d- %(name)s - %(message)s',    
    level = logging.INFO

)