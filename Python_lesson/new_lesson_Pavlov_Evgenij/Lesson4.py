import os
import logging.config

LOGGING_CFG = {
    "version": 1,
    'formatters': {
        'lesson4_format': {
        'format': '% (asctime) s [% (levelname) s]%
        (filename) s:% (lineno) i% (message) s'
        },
    },
"handlers": {
    "lesson4_handle": {
        "level": "INFO",
        "class": "logging.FileHandler",
        'formatter': 'lesson4_format',
        "filename": os.path.join (os.getcwd (), "../
        lesson4.log"),
    }
},
    "loggers": {
        "lesson4_log": {
        "handlers": ["lesson4_handle"],
        "level": "INFO",
        },
    },
}

logging.config.dictConfig (LOGGING_CFG)
logger = logging.getLogger (lesson4_log)
logger.info ('test')