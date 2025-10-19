import math
from typing import Any


class Dictionary:
    def __init__(self, bucket: int = 8) -> None:
        # Number of buckets
        self.__bucket = bucket
        # Hash table of size bucket
        self.__table = [[] for _ in range(bucket)]
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:

        checker_2_3 = math.floor((2 / 3) * self.__bucket)
        if self.__len__() >= checker_2_3:
            self.__bucket *= 2
            copy_table = self.__table.copy()
            self.__table = [[] for _ in range(self.__bucket)]

            for slot in copy_table:
                for lst in slot:
                    self.__setitem__(lst[0], lst[2])

    def hashfunction(self, key: Any) -> tuple[int, int]:
        hash_key = hash(key)
        index = hash_key % self.__bucket
        return hash_key, index

    def __setitem__(self, key: Any, value: Any) -> None:
        self.resize()
        hash_key, index = self.hashfunction(key)

        lst = [key, hash_key, value]

        # Create
        if not self.__table[index]:
            self.__table[index].append(lst)
            return

        # Update
        for i, existing in enumerate(self.__table[index]):
            if existing[0] == key:
                self.__table[index][i] = lst
                return

        self.__table[index].append(lst)

    def __getitem__(self, key: Any) -> Any | None:
        hash_key, index = self.hashfunction(key)

        for lst in self.__table[index]:
            if lst[0] == key:
                return lst[2]

        raise KeyError(f"Key '{key}' not found")
