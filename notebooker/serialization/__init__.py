import importlib
import inspect
import pkgutil

import notebooker.serializers


def iter_namespace(pkg):
    serializers = {}
    for _, name, ispkg in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
        module = importlib.import_module(name)
        szs = {cls: mod for (cls, mod) in inspect.getmembers(module, inspect.isclass) if mod.__module__ == name}
        serializers.update(szs)
    return serializers


ALL_SERIALIZERS = iter_namespace(notebooker.serializers)
