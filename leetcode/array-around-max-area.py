# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def array_around_max_area(array):

    area, i, j = 0, 0, len(array)-1
    while i <= j:
        width = j - i
        if array[i] <= array[j]:
            height = array[i]
            i += 1
        else:
            height = array[j]
            j -= 1
        if area < width * height:
            area = width * height
    return area


if __name__ == '__main__':
    print array_around_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
