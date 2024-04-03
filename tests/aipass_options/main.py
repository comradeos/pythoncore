class Option:
    def __init__(self, pages, _pass):
        self.pages = pages
        self.value = _pass

    def __str__(self):
        return f"{self.pages} + {self.value}" if self.value else self.pages


class Tool:
    def __init__(self, options):
        self.options = options
    
    def get_option(self, data):
        result = None
        for opt in self.options:
            if opt.pages == data['pages'] and opt.value == data['pass']:
                return opt


# OPTIONS:
# 1-2 pages
# 3-4 pages 
# 1-2 pages + BYPASS
# 3-4 pages + BYPASS
# 1-2 pages + BYPASS + H-PASS
# 3-4 pages + BYPASS + H-PASS
# 1-2 pages + BYPASS + H-PASS + Z-PASS
# 3-4 pages + BYPASS + H-PASS + Z-PASS

if __name__ == "__main__":
    opt1 = Option('1-2 pages', [])
    opt2 = Option('3-4 pages', [])
    opt3 = Option('1-2 pages', ['BYPASS'])
    opt4 = Option('3-4 pages', ['BYPASS'])
    opt5 = Option('1-2 pages', ['BYPASS', 'H-PASS'])
    opt6 = Option('3-4 pages', ['BYPASS', 'H-PASS'])
    opt7 = Option('1-2 pages', ['BYPASS', 'H-PASS', 'Z-PASS'])
    opt8 = Option('3-4 pages', ['BYPASS', 'H-PASS', 'Z-PASS'])
    
    options = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8]

    data = {
        'pages': '1-2 pages',
        'pass': [
            'BYPASS',
            'H-PASS',
            'Z-PASS'
        ]
    }

    tool = Tool(options)

    option = tool.get_option(data)
    print(option)


