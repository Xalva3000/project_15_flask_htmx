from dataclasses import dataclass


@dataclass
class ClickerRepository:
    counter: int = 0

    def increase(self):
        self.counter += 1
        return self.counter
