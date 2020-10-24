from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            print '  {'
            for attr in attrs:
                if attr[0] == 'src':
                    print "    src: " + '"' + attr[1] + '",'
                if attr[0] == 'alt':
                    print "    caption: " + '"' + attr[1].replace('"','\\"') + '",'
            print '  },'
parser = MyHTMLParser()


file = open('media.txt', 'r')
PreviousLineFull = False
while True:
        line = file.readline()
        if not line:
            break
        if len(line) > 5:
            if not PreviousLineFull:
                print "media: ["
            parser.feed(line)
            PreviousLineFull = True
        else:
            if PreviousLineFull:
                print "]"
            PreviousLineFull = False
