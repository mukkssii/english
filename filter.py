some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]


def check_in(data):
    if type(data) is int:
        return data >= 500
    return False


filtered_data = list(filter(check_in, some_data))
print(filtered_data)
