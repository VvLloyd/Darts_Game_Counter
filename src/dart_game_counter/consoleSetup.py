import pandas as pd

def consoleSetup():
    # To display all log data in Python console
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    pd.set_option('display.float_format', '{:.0f}'.format)

    return
