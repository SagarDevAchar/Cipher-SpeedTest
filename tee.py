import _io

LOG_FILE: _io.TextIOWrapper = None


def tee_print(s: str, end='\n'):
    global LOG_FILE
    
    if not LOG_FILE or LOG_FILE.closed:
        LOG_FILE = open("output.log", 'a')
    
    if end == '\n':
        LOG_FILE.write(s.replace('\r', '') + end)

    print(s, end=end)