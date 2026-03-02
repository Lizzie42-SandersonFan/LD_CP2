import re

def is_valid_hexa_code(string):
    hexa_code = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
    return bool(re.match(hexa_code, string))

def get_midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)