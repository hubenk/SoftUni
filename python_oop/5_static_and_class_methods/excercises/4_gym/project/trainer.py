class Trainer:

    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result
