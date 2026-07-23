from mapper import mapper
from partitioner import partition
from reducer import reducer
from multiprocessing import Pool


def process_log(log):
    return mapper(log)


def main():
    file = open("input.txt", "r")

    logs = file.readlines()

    file.close()

    with Pool() as pool:
        mapped_data = pool.map(process_log, logs)

    mapped_data = [data for data in mapped_data if data is not None]

    partitions = partition(mapped_data, 3)

    final_result = {}

    for part in partitions:
        result = reducer(part)

        for key in result:
            if key in final_result:
                final_result[key] += result[key]
            else:
                final_result[key] = result[key]

    print("REAL-TIME PARALLEL LOG AGGREGATION RESULT")
    print("------------------------------------------")

    for key, value in final_result.items():
        print(key, ":", value)


if __name__ == "__main__":
    main()