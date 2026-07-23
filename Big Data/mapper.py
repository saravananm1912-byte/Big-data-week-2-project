def mapper(log_line):
    parts = log_line.split()

    if len(parts) > 0:
        log_level = parts[0]
        return log_level, 1

    return None