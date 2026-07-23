def reducer(data):
    result = {}

    for key, value in data:
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result