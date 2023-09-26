import typing
from typing import List, Tuple, Dict, TypeAlias, Any, Callable, Union, Optional, Literal

Int: TypeAlias = Union[int, float]
Bool: TypeAlias = Union[bool, Literal[0, 1]]
Vector3: TypeAlias = Tuple[float, float, float]
Quaternion: TypeAlias = Tuple[float, float, float, float]
