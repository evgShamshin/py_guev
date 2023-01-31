'''Базовое смещение элемента от уровня'''
base_offset = -3
'''Высота элемента'''
el_height = 3
'''Высота уровня'''
lvl_height = 3


def check_levels(base_offset, el_height, lvl_height):
    if base_offset >= 0:
        if base_offset + el_height <= lvl_height:
            return 0
        elif base_offset >= lvl_height:
            return 2
        elif base_offset + el_height > lvl_height:
            return 1

    if base_offset < 0:
        if base_offset + el_height > 0:
            return 1
        elif base_offset + el_height <= 0:
            return 2


check_levels(0.0, 3.0, 3.0)
check_levels(0.0, 2.0, 3.0)
check_levels(2.0, 1.0, 3.0)
check_levels(1.0, 1.0, 3.0)
check_levels(-1.0, 2.0, 3.0)
check_levels(0.0, 4.0, 3.0)
check_levels(-1.0, 4.0, 3.0)
check_levels(-1.0, 3.0, 3.0)
check_levels(1.0, 3.0, 3.0)
check_levels(-1.0, 5.0, 3.0)
check_levels(4.0, 3.0, 3.0)
check_levels(3.0, 3.0, 3.0)
check_levels(-4.0, 3.0, 3.0)
check_levels(-3.0, 3.0, 3.0)
