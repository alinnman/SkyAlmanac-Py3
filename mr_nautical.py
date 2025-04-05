

# Delete all existing CSV files
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
        a_len = len (a)
        for i in range (a_len):
            g.write (filter_text(a[i]))
            if i < a_len-1:
                g.write (";")
        g.write ("\n")
    finally:
        g.close ()

def write_header_mr (filename : str, header : str):
    ''' Write header to empty CSV file '''
    try:
        g = get_file (filename + ".csv")
        g.write (header)
        g.write ("\n")
    finally:
        g.close ()

# Write headers for the almanac (CSV) files
write_header_mr ("planets",
"Timestamp;Aries_GHA;Venus_GHA;Venus_DECL;Mars_GHA;Mars_DECL;Jupiter_GHA;"+\
"Jupiter_DECL;Saturn_GHA;Saturn_DECL")
write_header_mr ("stars",
"Timestamp;Name;SHA;Dec")
write_header_mr ("venus-mars-hp",
"Timestamp;Venus_HP;Mars_HP")
write_header_mr ("sun-moon-sd",
"Timestamp;Sun_SD;Sun_v;Moon_SD")
write_header_mr ("sun-moon",
"Timestamp;Sun_GHA;Sun_DEC;Moon_GHA;Moon_v;Moon_DEC;Moon_d;Moon_HP")
