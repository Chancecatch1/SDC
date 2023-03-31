from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':  
            self.is_td = True

    def handle_endtag(self, tag):
        if tag == 'td':  
            self.is_td = False

    def handle_data(self, data):
        if self.is_td:  
            print(data)     


with open('./Personal_Rent_files/대관신청회원_강화정_20230308.html', 'rb') as f:
    parser = MyHTMLParser()
    parser.feed(f.read().decode('utf-8'))