import sys
import getopt


if __name__ == '__main__':

    cmd_line_args = sys.argv[1:]

    unix_args = 'hn:os'
    gnu_args = ['help','comicnum=','print','save-image']

    oplist, args = getopt.getopt(cmd_line_args,unix_args,gnu_args)

    print(args) #Extra arguments that are not part of the uni_args or gnu_args
    print(oplist) #oplist is a list of tuples

    for opt, arg in oplist:
        print(opt)
        print(arg)
        if opt == '-h' or opt == '--help':
            print('help message')
        elif opt == '-n' or opt == '--comicnum':
            print('Get the comic number ' + str(arg))
        elif opt == '-o' or opt == '--print':
            print('print output in format json/text')
        elif opt == '-s' or opt == '--save-image':
            print('Download image in this directory')
