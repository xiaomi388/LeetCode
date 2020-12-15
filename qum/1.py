# 13:50

def intersect(l1, l2):
    s1, s2 = set(l1), set(l2)
    return list(s1.intersect(s2))