from typing import (
    AnyStr,
    Callable,
    Generic,
    Iterator,
    Literal,
    TypeVar,
    overload,
)

from typing_extensions import TypeAlias

# References:
# - https://github.com/google/re2/blob/main/re2/re2.h and
# - https://github.com/python/typeshed/blob/main/stdlib/re.pyi
# - and re2 implementation

_T = TypeVar("_T")

_Pattern: TypeAlias = _Regexp[str] | str | _Regexp[bytes] | bytes

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
def search(
    pattern: _Pattern, text: AnyStr, options: Options | None = None
) -> _Match[AnyStr] | None: ...
def match(
    pattern: _Pattern, text: AnyStr, options: Options | None = None
) -> _Match[AnyStr] | None: ...
def fullmatch(
    pattern: _Pattern, text: AnyStr, options: Options | None = None
) -> _Match[AnyStr] | None: ...
def finditer(
    pattern: _Pattern, text: AnyStr, options: Options | None = None
) -> Iterator[_Match[AnyStr]]: ...
def findall(
    pattern: _Pattern, text: AnyStr, options: Options | None = None
) -> list[AnyStr]: ...
def split(
    pattern: _Pattern,
    text: AnyStr,
    maxsplit: int = 0,
    options: Options | None = None,
) -> list[AnyStr]: ...
def subn(
    pattern: _Pattern,
    repl: AnyStr | Callable[[_Match[AnyStr]], AnyStr],
    text: AnyStr,
    count: int = 0,
    options: Options | None = None,
) -> tuple[AnyStr, int]: ...
def sub(
    pattern: _Pattern,
    repl: AnyStr | Callable[[_Match[AnyStr]], AnyStr],
    text: AnyStr,
    count: int = 0,
    options: Options | None = None,
) -> AnyStr: ...
def escape(pattern: AnyStr) -> AnyStr: ...
def purge() -> None: ...

# re2 regexps produce match objects based on the text to match regardless
# of the initial pattern the regexp was constructed with. Introduce a separately
# constrained AnyStr which is uncorrelated with the string type the regexp
# was originally constructed with to represent this re2 feature.
_AnyStr2 = TypeVar("_AnyStr2", str, bytes)

class _Regexp(Generic[AnyStr]):
    def __init__(self, pattern: AnyStr, options: Options) -> None: ...
    def search(
        self, text: _AnyStr2, pos: int | None = None, endpos: int | None = None
    ) -> _Match[_AnyStr2] | None: ...
    def match(
        self, text: _AnyStr2, pos: int | None = None, endpos: int | None = None
    ) -> _Match[_AnyStr2] | None: ...
    def fullmatch(
        self, text: _AnyStr2, pos: int | None = None, endpos: int | None = None
    ) -> _Match[_AnyStr2] | None: ...
    def finditer(
        self, text: _AnyStr2, pos: int | None = None, endpos: int | None = None
    ) -> Iterator[_Match[_AnyStr2]]: ...
    def findall(
        self, text: _AnyStr2, pos: int | None = None, endpos: int | None = None
    ) -> list[_AnyStr2]: ...
    def split(self, text: _AnyStr2, maxsplit: int = 0) -> list[_AnyStr2]: ...
    def subn(
        self,
        repl: _AnyStr2 | Callable[[_Match[_AnyStr2]], _AnyStr2],
        text: _AnyStr2,
        count: int = 0,
    ) -> tuple[_AnyStr2, int]: ...
    def sub(
        self,
        repl: _AnyStr2 | Callable[[_Match[_AnyStr2]], _AnyStr2],
        text: _AnyStr2,
        count: int = 0,
    ) -> _AnyStr2: ...
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
    def expand(self: _Match[AnyStr], template: str) -> AnyStr: ...
    def __getitem__(self, group: int | str) -> AnyStr | None: ...
    @overload
    def group(self, group: Literal[0] = 0, /) -> AnyStr: ...
    @overload
    def group(self, group: AnyStr | int, /) -> AnyStr: ...
    @overload
    def group(
        self: _Match[str],
        group1: AnyStr | int,
        group2: AnyStr | int,
        /,
        *groups: AnyStr | int,
    ) -> tuple[AnyStr, ...]: ...
    @overload
    def groups(self) -> tuple[AnyStr, ...]: ...
    @overload
    def groups(self, default: _T) -> tuple[AnyStr | _T, ...]: ...
    @overload
    def groupdict(self: _Match[AnyStr]) -> dict[AnyStr, AnyStr]: ...
    @overload
    def groupdict(self, default: _T) -> dict[AnyStr, AnyStr | _T]: ...
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
