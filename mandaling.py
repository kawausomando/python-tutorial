class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # ↑のupdate()メソッドのプライベートコピー

class MappingSubclass(Mapping):
    # update()の新しいシグネチャを提供しつつ
    # 既存の__init__()は破壊せずに利用できる
    def update(self, iterable):
        for item in zip(keys, values):
            self.items_list.append(item)