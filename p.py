class FlatIterator:

    def __init__(self, list_of_list):
        self.flat_list = [item for sublist in list_of_list for item in sublist]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

