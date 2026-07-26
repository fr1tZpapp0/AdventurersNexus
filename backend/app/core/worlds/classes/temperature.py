from dataclasses import dataclass
from uuid import UUID


@dataclass
class Temperature():
    id: UUID

    spring: tuple[int, int]
    summer: tuple[int, int]
    autumn: tuple[int, int]
    winter: tuple[int, int]


