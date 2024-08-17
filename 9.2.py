from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:

    res = 0
    if len(args) != 0:
        res = round(max(args) - min(args), 2)
    print(res)

    return res


difference(1, 2, 3)
difference(5, -5)
difference(10.2, -2.2, 0, 1.1, 0.5)
difference()
