from typing import AnyStr, Generic, Iterator, Literal, TypeVar, overload, Callable

# References:
# - https://github.com/google/re2/blob/main/re2/re2.h and
# - https://github.com/python/typeshed/blob/main/stdlib/re.pyi
# - and re2 implementation

_T = TypeVar("_T")

class error(Exception): ...

class Options:
    max_mem: int | None
    encoding: int
    posix_syntax: bool | None
    longest_match: bool | None
    log_errors: bool | None
    never_nl: bool | None
    dot_nl: bool | None
    never_capture: bool | None
    case_sensitive: bool | None
    perl_classes: bool | None
    word_boundary: bool | None
    one_line: bool | None

def compile(
    pattern: _Regexp[AnyStr] | AnyStr, options: Options | None = None
) -> _Regexp[AnyStr]: ...
@overload
def search(
    pattern: _Regexp[str] | str, text: str, options: Options | None = None
) -> _Match[str] | None: ...
@overload
def search(
    pattern: _Regexp[bytes] | bytes, text: bytes, options: Options | None = None
) -> _Match[bytes] | None: ...
@overload
def match(
    pattern: _Regexp[str] | str, text: str, options: Options | None = None
) -> _Match[str] | None: ...
@overload
def match(
    pattern: _Regexp[bytes] | bytes, text: bytes, options: Options | None = None
) -> _Match[bytes] | None: ...
@overload
def fullmatch(
    pattern: _Regexp[str] | str, text: str, options: Options | None = None
) -> _Match[str] | None: ...
@overload
def fullmatch(
    pattern: _Regexp[bytes] | bytes, text: bytes, options: Options | None = None
) -> _Match[bytes] | None: ...
@overload
def finditer(
    pattern: _Regexp[str] | str, text: str, options: Options | None = None
) -> Iterator[_Match[str]]: ...
@overload
def finditer(
    pattern: _Regexp[bytes] | bytes, text: bytes, options: Options | None = None
) -> Iterator[_Match[bytes]]: ...
@overload
def findall(
    pattern: _Regexp[str] | str, text: str, options: Options | None = None
) -> list[str]: ...
@overload
def findall(
    pattern: _Regexp[bytes] | bytes, text: bytes, options: Options | None = None
) -> list[bytes]: ...
@overload
def split(
    pattern: _Regexp[str] | str,
    text: str,
    maxsplit: int = 0,
    options: Options | None = None,
) -> list[str]: ...
@overload
def split(
    pattern: _Regexp[bytes] | bytes,
    text: bytes,
    maxsplit: int = 0,
    options: Options | None = None,
) -> list[bytes]: ...
@overload
def subn(
    pattern: _Regexp[str] | str,
    repl: str,
    text: str,
    count: int = 0,
    options: Options | None = None,
) -> tuple[str, int]: ...
@overload
def subn(
    pattern: _Regexp[bytes] | bytes,
    repl: bytes,
    text: bytes,
    count: int = 0,
    options: Options | None = None,
) -> tuple[bytes, int]: ...
@overload
def sub(
    pattern: _Regexp[str] | str,
    repl: str | Callable[[_Match[str]], str],
    text: str,
    count: int = 0,
    options: Options | None = None,
) -> str: ...
@overload
def sub(
    pattern: _Regexp[bytes] | bytes,
    repl: bytes | Callable[[_Match[bytes]], bytes],
    text: bytes,
    count: int = 0,
    options: Options | None = None,
) -> bytes: ...
def escape(pattern: AnyStr) -> AnyStr: ...
def purge() -> None: ...

class _Regexp(Generic[AnyStr]):
    def __init__(self, pattern: AnyStr, options: Options) -> None: ...
    @overload
    def search(
        self: _Regexp[str], text: str, pos: int | None = None, endpos: int | None = None
    ) -> _Match[str] | None: ...
    @overload
    def search(
        self: _Regexp[bytes],
        text: bytes,
        pos: int | None = None,
        endpos: int | None = None,
    ) -> _Match[bytes] | None: ...
    @overload
    def match(
        self: _Regexp[str], text: str, pos: int | None = None, endpos: int | None = None
    ) -> _Match[str] | None: ...
    @overload
    def match(
        self: _Regexp[bytes],
        text: bytes,
        pos: int | None = None,
        endpos: int | None = None,
    ) -> _Match[bytes] | None: ...
    @overload
    def fullmatch(
        self: _Regexp[str], text: str, pos: int | None = None, endpos: int | None = None
    ) -> _Match[str] | None: ...
    @overload
    def fullmatch(
        self: _Regexp[bytes],
        text: bytes,
        pos: int | None = None,
        endpos: int | None = None,
    ) -> _Match[bytes] | None: ...
    @overload
    def finditer(
        self: _Regexp[str], text: str, pos: int | None = None, endpos: int | None = None
    ) -> Iterator[_Match[str]]: ...
    @overload
    def finditer(
        self: _Regexp[bytes],
        text: bytes,
        pos: int | None = None,
        endpos: int | None = None,
    ) -> Iterator[_Match[bytes]]: ...
    @overload
    def findall(
        self: _Regexp[str], text: str, pos: int | None = None, endpos: int | None = None
    ) -> list[str]: ...
    @overload
    def findall(
        self: _Regexp[bytes],
        text: bytes,
        pos: int | None = None,
        endpos: int | None = None,
    ) -> list[bytes]: ...
    @overload
    def split(self: _Regexp[str], text: str, maxsplit: int = 0) -> list[str]: ...
    @overload
    def split(self: _Regexp[bytes], text: bytes, maxsplit: int = 0) -> list[bytes]: ...
    @overload
    def subn(
        self: _Regexp[str], repl: str, text: str, count: int = 0
    ) -> tuple[str, int]: ...
    @overload
    def subn(
        self: _Regexp[bytes], repl: bytes, text: bytes, count: int = 0
    ) -> tuple[bytes, int]: ...
    @overload
    def sub(
        self: _Regexp[str],
        repl: str | Callable[[_Match[str]], str],
        text: str,
        count: int = 0,
    ) -> str: ...
    @overload
    def sub(
        self: _Regexp[bytes],
        repl: bytes | Callable[[_Match[bytes]], bytes],
        text: bytes,
        count: int = 0,
    ) -> bytes: ...
    @property
    def pattern(self) -> AnyStr: ...
    @property
    def options(self) -> Options: ...
    @property
    def groups(self) -> int: ...
    @property
    def groupindex(self) -> dict[AnyStr, int]: ...
    @property
    def programsize(self) -> int: ...
    @property
    def reverseprogramsize(self) -> int: ...
    @property
    def programfanout(self) -> int: ...
    @property
    def reverseprogramfanout(self) -> int: ...
    def possiblematchrange(self, maxlen: int) -> tuple[AnyStr, AnyStr]: ...

class _Match(Generic[AnyStr]):
    def __init__(
        self,
        regexp: _Regexp[AnyStr],
        text: AnyStr,
        pos: int,
        endpos: int,
        spans: dict[int, tuple[int, int]],
    ) -> None: ...
    @overload
    def expand(self: _Match[str], template: str) -> str: ...
    @overload
    def expand(self: _Match[bytes], template: bytes) -> bytes: ...
    @overload
    def __getitem__(self: _Match[str], group: int | str) -> str | None: ...
    @overload
    def __getitem__(self: _Match[bytes], group: int | bytes) -> bytes | None: ...
    @overload
    def group(self: _Match[str], group: Literal[0] = 0, /) -> str: ...
    @overload
    def group(self: _Match[bytes], group: Literal[0] = 0, /) -> bytes: ...
    @overload
    def group(self: _Match[str], group: str | int, /) -> str: ...
    @overload
    def group(self: _Match[bytes], group: bytes | int, /) -> bytes: ...
    @overload
    def group(
        self: _Match[str], group1: str | int, group2: str | int, /, *groups: str | int
    ) -> tuple[str, ...]: ...
    @overload
    def group(
        self: _Match[bytes],
        group1: bytes | int,
        group2: bytes | int,
        /,
        *groups: bytes | int,
    ) -> tuple[bytes, ...]: ...
    @overload
    def groups(self: _Match[str]) -> tuple[str, ...]: ...
    @overload
    def groups(self: _Match[bytes]) -> tuple[bytes, ...]: ...
    @overload
    def groups(self: _Match[str], default: _T) -> tuple[str | _T, ...]: ...
    @overload
    def groups(self: _Match[bytes], default: _T) -> tuple[bytes | _T, ...]: ...
    @overload
    def groupdict(self: _Match[str]) -> dict[str, str]: ...
    @overload
    def groupdict(self: _Match[bytes]) -> dict[bytes, bytes]: ...
    @overload
    def groupdict(self: _Match[str], default: _T) -> dict[str, str | _T]: ...
    @overload
    def groupdict(self: _Match[bytes], default: _T) -> dict[bytes, bytes | _T]: ...
    def start(self, group: int = 0) -> int: ...
    def end(self, group: int = 0) -> int: ...
    def span(self, group: int = 0) -> tuple[int, int]: ...
    @property
    def re(self) -> _Regexp[AnyStr]: ...
    @property
    def string(self) -> AnyStr: ...
    @property
    def pos(self) -> int: ...
    @property
    def endpos(self) -> int: ...
    @property
    def lastindex(self) -> int | None: ...
    @property
    def lastgroup(self) -> int | None: ...

class Set:
    def __init__(self, anchor: int, options: Options | None = None) -> None: ...
    @classmethod
    def SearchSet(cls, options: Options | None = None) -> Set: ...
    @classmethod
    def MatchSet(cls, options: Options | None = None) -> Set: ...
    @classmethod
    def FullMatchSet(cls, options: Options | None = None) -> Set: ...
    def Add(self, pattern: AnyStr) -> int: ...
    def Compile(self) -> None: ...
    def Match(self, text: AnyStr) -> bool | None: ...

class Filter:
    def __init__(self) -> None: ...
    def Add(self, pattern: AnyStr, options: Options | None = None) -> int: ...
    def Compile(self) -> None: ...
    def Match(self, text: AnyStr, potential: bool = False) -> list[int]: ...
    def re(self, index: int) -> _Regexp[AnyStr]: ...
