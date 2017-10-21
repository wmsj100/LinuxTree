def fibs(num):
    'this fn is for get fei bo na qi list'
    result = [0, 1];
    for i in range(num -2):
        result.append(result[-2] + result[-1]);
    return result;
