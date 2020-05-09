from os import sep
from os.path import dirname, abspath, join


def get_swagger_file_path(module: str, swagger_file_name: str) -> str:
    try:
        return join(
            dirname(abspath(__file__)).rsplit(sep, 2)[0],
            "docs",
            module.rsplit(".")[-2],
            swagger_file_name,
        )
    except IOError:
        raise IOError("Not able to read swagger file")
    except Exception:
        raise Exception("Unexpected error occurred")
