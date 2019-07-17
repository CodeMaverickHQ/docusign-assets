from flask import Flask, request
import docuSignModule

app = Flask(__name__)

@app.route('/')
def index():
    return ('<h1>welcome</h1> <a href="/assets">Assets</a>')

@app.route('/assets')
def assetIndex():
    return('<h1>Assets</h1> <ul><li><a href="assets/1231">1231</a></li></ul>')

@app.route('/assets/<asset>')
def assetShow(asset):
    return('<h1>Asset {}</h1> <p>Sent user agreement to </p><form method="POST" action="/sign/{}"><input placeholder="Name" name="name"><input placeholder="email" name="email"><input type="submit"></form>'.format(asset, asset))

@app.route('/sign/<asset>', methods=['GET', 'POST'])
def signRoute(asset):
    asset=asset.upper()
    testuser={'email':'', 'name':''}
    testuser['email']=request.form['email']
    testuser['name']=request.form['name']
    #specify the admin
    admin={'email':'admin.admin@theadminuser.com', 'name':'Admin of Admin'}
    docuSignModule.userAgreement(admin, testuser, asset)
    return('sign route {} for user {} - return <a href="/">home</a>'.format(asset, testuser['name']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
