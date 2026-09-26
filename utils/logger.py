import sys
from loguru import logger as _loguru_logger

_configured = False


def _configure_once():
    global _configured

    if _configured:
        return

    _configured = True

    # Remove default Loguru handler
    _loguru_logger.remove()

    # Vercel/serverless-friendly logging:
    # Write logs to stdout/stderr instead of creating files.
    _loguru_logger.add(
        sys.stdout,
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
        enqueue=False,
    )


def get_logger(name=None):
    _configure_once()

    if name:
        return _loguru_logger.bind(name=name)

    return _loguru_logger
