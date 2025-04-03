from datetime import datetime

def diff(d1_str, d2_str):
    fmt = '%Y-%m-%d'

    d1 = datetime.strptime(d1_str, fmt)
    d2 = datetime.strptime(d2_str, fmt)

    return (d2 - d1).total_seconds()

d1 = '2024-02-17'
d2 = '2024-02-18'
x = diff(d1, d2)
print(x)