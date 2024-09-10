import logging

def setup_logging(app):
    log_path = 'app.log'
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_format)
    handler = logging.FileHandler(log_path)
    handler.setFormatter(logging.Formatter(log_format))
    app.logger.addHandler(handler)