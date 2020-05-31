import sys
import getopt


if __name__ == '__main__':

    cmd_line_args = sys.argv[1:]

    unix_args = 'hn:os'
    gnu_args = ['help','comicnum=','print','save-image']

    oplist, args = getopt.getopt(cmd_line_args,unix_args,long_args)

    print(args) #Extra arguments that are not part of the uni_args or gnu_args
    print(oplist) #oplist is a list of tuples
