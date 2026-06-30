from typing import AsyncGenerator, Any

class StreamContext:
    """
    Interface for producing and consuming streamed partial data (e.g. LLM tokens).
    """
    def __init__(self):
        self._chunks = []

    def push(self, chunk: Any) -> None:
        self._chunks.append(chunk)

    async def consume(self) -> AsyncGenerator[Any, None]:
        # A full implementation would use asyncio.Queue for actual stream consumption
        for chunk in self._chunks:
            yield chunk
