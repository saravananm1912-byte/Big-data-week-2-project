def partition(data, number_of_partitions):
    partitions = [[] for i in range(number_of_partitions)]

    for key, value in data:
        position = hash(key) % number_of_partitions
        partitions[position].append((key, value))

    return partitions