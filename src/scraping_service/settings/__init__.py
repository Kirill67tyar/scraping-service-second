from .production import *
try:
    from .for_local import local
    if local:
        from .local_settings import *
except ImportError:
    pass
