import os


def get_my_envvar():
    envvar = os.getenv('MY_ENVVAR')

    if envvar is None:
        raise OSError('MY_ENVVAR is not set.')

    return envvar
