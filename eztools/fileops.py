import json
import logging
from os import environ
from os.path import basename, getsize, getmtime, splitext, exists

import arrow


def get_file_info(file_path):
    valid_file_types = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.txt', '.log', '.csv']
    if not exists(file_path):
        logging.error('File not found: {}'.format(file_path))

    elif splitext(file_path)[1].lower() not in valid_file_types:
        logging.error('Invalid file type: {}'.format(splitext(file_path)[1]))

    elif getsize(file_path) == 0:
        logging.error('File is empty: {}'.format(file_path))

    else:
        return {'name': basename(file_path),
                'file_byte_size': getsize(file_path),
                'file_created_time': str(arrow.get(getmtime(file_path)))}


def env_to_json():
    """convert current env variables to json text."""
    return json.dumps(dict(environ))
