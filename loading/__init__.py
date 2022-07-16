import logging

from .loading import Loading

logging.basicConfig(level=logging.DEBUG, filename="loading.log", filemode='w',
                        format="%(asctime)s - %(levelname)s - %(message)s")

loader = Loading()
# __all__ = (
#     room,
#     entity,
#     character,
# )