def _wrap_with(code):

    def inner(text, bold=False):
        c = code
        if bold:
            c = '1;{c}'.format(c=c)
        return '\033[{c}m{text}\033[0m'.format(c=c, text=text)
    return inner

red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')

print(green("This text is green!"))