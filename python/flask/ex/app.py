from flask import Flask, request

app = Flask(__name__)

# you can return a wsgi application from a view
#@app.route('/')
#def index():
#    def rv(environ, start_response):
#        start_response('200 Ok', [('Content-type','text/plain')])
#        return ["hell yeah!"]
#    return rv


# examining request.endpoint
@app.route('/')
def indexo():
    return "endpoing is %s" % request.endpoint

# examining request.blueprint
@app.route('/')
def indexo():
    return "blueprint is %s" % request.blueprint

# examining request.url_rule.endpoint
@app.route('/')
def indexo():
    return "url_rule.endpoint is %s" % request.url_rule.endpoint

# examining request.mimetype
@app.route('/')
def indexo():
    return "mimetype is %s" % request.mimetype

# examining request.blueprint
#@app.route('/')
#def indexo():
#    return "blueprint is %s" % request.blueprint

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
