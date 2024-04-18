from mod1 import decorator_factory
italic = "<em>%s</em>"
bold = "<strong>%s</strong>"

@decorator_factory()
def hello():
    return "hello world!"
