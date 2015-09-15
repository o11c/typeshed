# Stubs for zlib (Python 2.7)

class error(Exception): ...

DEFLATED = ... # type: int
DEF_MEM_LEVEL = ... # type: int
MAX_WBITS = ... # type: int
ZLIB_VERSION = ... # type: str
Z_BEST_COMPRESSION = ... # type: int
Z_BEST_SPEED = ... # type: int
Z_DEFAULT_COMPRESSION = ... # type: int
Z_DEFAULT_STRATEGY = ... # type: int
Z_FILTERED = ... # type: int
Z_FINISH = ... # type: int
Z_FULL_FLUSH = ... # type: int
Z_HUFFMAN_ONLY = ... # type: int
Z_NO_FLUSH = ... # type: int
Z_SYNC_FLUSH = ... # type: int

def adler32(data: str, value: int = ...) -> int: ...
def compress(data: str, level: int = ...) -> str: ...
def crc32(data: str, value: int = ...) -> int: ...
def decompress(data: str, wbits: int = ..., bufsize: int = ...) -> str: ...

class compressobj:
    def __init__(level: int = ..., method: int = ..., wbits: int = ..., memlevel: int = ...,
                 strategy: int = ...): ...
    def compress(self, data: str) -> str
    def copy(self) -> _Compress
    def flush(self) -> NoneType

class decompressobj:
    def __init__(wbits: int = ...): ...
    def copy(self) -> _Compress
    def decompress(self, data: str) -> str
    def flush(self) -> NoneType