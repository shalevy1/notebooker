import logging
import os
from enum import Enum

from notebooker.serialization.mongo import MongoResultSerializer
from notebooker.serializers.pymongo import PyMongoResultSerializer
from . import ALL_SERIALIZERS


logger = logging.getLogger(__name__)


def serializer_kwargs_from_os_envs():
    return {
        "user": os.environ.get("MONGO_USER"),
        "password": os.environ.get("MONGO_PASSWORD"),
        "mongo_host": os.environ.get("MONGO_HOST"),
        "database_name": os.environ.get("DATABASE_NAME"),
        "result_collection_name": os.environ.get("RESULT_COLLECTION_NAME"),
    }


def get_serializer_from_cls(serializer_cls: str, **kwargs: dict) -> MongoResultSerializer:
    serializer = ALL_SERIALIZERS.get(serializer_cls)
    if serializer is None:
        raise ValueError("Unsupported serializer {}".format(serializer_cls))
    return serializer(**kwargs)


def get_fresh_serializer() -> MongoResultSerializer:
    serializer_cls = os.environ.get("NOTEBOOK_SERIALIZER", PyMongoResultSerializer.get_name())
    serializer_kwargs = serializer_kwargs_from_os_envs()
    return get_serializer_from_cls(serializer_cls, **serializer_kwargs)


if __name__ == "__main__":
    from . import ALL_SERIALIZERS

    print(ALL_SERIALIZERS)
