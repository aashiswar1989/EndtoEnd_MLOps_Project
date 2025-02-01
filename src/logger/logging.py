import logging
from pathlib import Path
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR = Path('logs')
if not LOG_DIR.is_dir():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILEPATH = LOG_DIR/LOG_FILE

logging.basicConfig(
    level = logging.INFO,
    filename=LOG_FILEPATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)