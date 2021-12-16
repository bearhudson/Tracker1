def print_results(command, code):
    if code == 200:
        print(f"{command} successful")
    else:
        print(f"{command} failed -> HTTP Response {code}")
