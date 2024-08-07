import logging


class ExcludeSeleniumLogsFilter(logging.Filter):
    def filter(self, record):
        # Exclude logs from the 'selenium' logger
        return ("seleniumwire" not in record.filename
                or "seleniumwire" not in record.name
                or "seleniumwire" not in record.pathname
                or "seleniumwire" not in record.module)
