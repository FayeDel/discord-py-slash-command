from asyncio import Lock
from typing import Optional

from interactions.api.models.attrs_utils import MISSING


class Limiter:

    lock: Lock
    reset_after: float
    def __init__(self, *, lock: Lock, reset_after: Optional[float] = MISSING) -> None: ...
    async def __aenter__(self) -> "Limiter": ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def release_lock(self): ...
