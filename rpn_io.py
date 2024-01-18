def open_rpn_file():
    """Open-source-file function. Open a named
    file and reed lines into a list which is
    returned.
    """
    while True:
        try:
            fname = input("Enter RPN source: ")
            f = open(fname, "r")
            if not f:
                return None
            else:
                break
        except:
            print("File not found. Re-enter.")
    a_list = f.readlines()
    return a_list


def do_prints(s):
    """Carry out PRINTS directive by printing a
    string.
    """

    a_str = get_str(s)
    print(a_str, end="")


def do_println(s):
    """Carry out PRINTLN directive: print the
    optional string argument, if specified, and then
    print a newline, unconditionally."""
    if s:
        do_prints(s)
    print()


def get_str(s):
    """Helper function for do_prints"""
    a = s.find("'")
    b = s.rfind("'")
    if a == -1 or b == -1:
        return ""
    return s[a + 1 : b]


def do_printvar(s, sym_tab):
    """Carry out PRINTVAR directive; look up the
    variable name contained in the string s, and
    then look this name up in the symbol table.
    """
    wrd = s.split()[0]
    print(sym_tab[wrd], end=" ")


def do_input(s, sym_tab):
    """Carry out INPUT directive; get value input
    from the end user, then enter this value in the
    symbol table, for name contained in string s.
    """
    wrd = input()
    sym_tab[s] = float(wrd)
