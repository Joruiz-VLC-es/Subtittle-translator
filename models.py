from dataclasses import dataclass, field

@dataclass(slots=True)
class Subtitle:
    index: int
    start: str
    end: str
    lines: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @text.setter
    def text(self, value: str) -> None:
        self.lines = value.splitlines()
        from dataclasses import dataclass, field

@dataclass(slots=True)
class Subtitle:
    index: int
    start: str
    end: str
    lines: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @text.setter
    def text(self, value: str) -> None:
        self.lines = value.splitlines()
