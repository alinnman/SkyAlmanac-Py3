

from pathlib import Path
for p in Path(".").glob("*.csv"):
    p.unlink()

def get_file (filename : str):
    ''' Get a file handle to mr data file '''
    f = open (filename, "a", encoding="UTF8")
    return f

def filter_text (s : str) -> str:
    ''' Filter out LaTEX from string '''
    t = s.replace ("$^\\circ$",":")
    t_len = len(t)
    if t[t_len-1] == '\'':
        t = "0:" + t[0:t_len-1]
    return t

def write_out_mr (filename : str, a : list[str]):
    ''' Writing out data on machine readable almanac '''
    try:
        g = get_file (filename + ".csv")
        for s in a:
            g.write (filter_text(s))
            g.write (";")
        g.write ("\n")
    finally:
        g.close ()