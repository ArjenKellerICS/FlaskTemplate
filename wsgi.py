# imports
import logging
from server import create_server

# set up logging and log to file
logging.basicConfig(filename="GLOBALDUMP.log", level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(process)d - %(name)s - %(message)s')

# start root logger instance
logger = logging.getLogger()

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(process)d - %(name)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# create server with application factory
server = create_server()

# Run if file is executed
if __name__ == '__main__':
    logger.info("Starting WSGI server")
    # start the server
    server.run()
