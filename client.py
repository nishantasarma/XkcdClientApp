import requests
import ast
import sys
import getopt


class XkcdClient():


    def api_call(self, url):
        self.urls = url

        r = requests.get(url = self.urls)
        byte_str = r.content
        dict_str = byte_str.decode("UTF-8")
        my_data = ast.literal_eval(dict_str)
        return my_data

    def get_image(self,img_url):
        self.img_name = img_url.split('/')[-1]
        img_data = requests.get(img_url).content
        with open(self.img_name+'.png', 'wb') as handler:
            handler.write(img_data)



# client = XkcdClient()
# response = client.api_call('https://xkcd.com/info.0.json')
# print(response)


if __name__ == '__main__':

    cmd_line_args = sys.argv[1:]
    unix_args = 'hn:os'
    gnu_args = ['help','comicnum=','print','save-image']

    oplist, args = getopt.getopt(cmd_line_args,unix_args,gnu_args)

    print(args) #Extra arguments that are not part of the uni_args or gnu_args
    print(oplist) #oplist is a list of tuples
    comic_num = ''
    client = XkcdClient()
    url_latest = 'https://xkcd.com/info.0.json'
    for opt, arg in oplist:
        print(opt)
        print(arg)

        if opt == '-h' or opt == '--help':
            print('help message')
            print('Use -n or --comicnum to specify the comic number you want use 0 as argument for latest comic')
            print('Use -o or --print to get info in text/json format')
            print('Use -s or --save-image to download image in this directory')
        elif opt == '-n' or opt == '--comicnum':
            comic_num = arg
            if comic_num is '0': #default get the latest comic
                print('Get the comic number ' + str(arg))
                response = client.api_call(url_latest)
                print(response)
            else:
                url_specific = 'http://xkcd.com/'+arg+'/info.0.json'
                response = client.api_call(url_specific)
        elif opt == '-o' or opt == '--print':
            response = client.api_call('https://xkcd.com/info.0.json')
            print('print output in format json/text')
            print(response)
        elif opt == '-s' or opt == '--save-image':
            if comic_num:
                img_url = response['img']
                client.get_image(img_url)
            else:
                print('Set the -n parameter first')
