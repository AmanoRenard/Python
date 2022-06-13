def is_kazu(num):
    if type(num) is not str:
        raise ValueError('parameter must be a string.')
    if len(num) > 2 and num.count('.',1,-1) == 1:
        num=num.replace('.','',1)
    if num.isnumeric():
        return True
    else:
        return False

print(is_kazu('1.2.3'))