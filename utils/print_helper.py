#Improve the readability of the code and ensure consistency when displaying tabular data. It can be reused across the project
def print_table(headers, rows):
    header_line = " | ".join([header.ljust(20) for header in headers])
    print(header_line)
    print('-' * len(header_line))
    for row in rows:
        print(" | ".join([str(item).ljust(20) for item in row]))