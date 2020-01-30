''' Starting point for docusign-asset app with flask'''
from flask import Flask, request
import docuSignModule

APP = Flask(__name__)

@APP.route('/')
def index():
    ''' index route '''
    return '<h1>welcome</h1> <a href="/assets">Assets</a>'

@APP.route('/assets')
def asset_index():
    ''' asset route '''
    return '<h1>Assets</h1> <ul><li><a href="assets/1231">1231</a></li></ul>'

@APP.route('/assets/<asset>')
def asset_show(asset):
    ''' asset show route '''
    return '''<h1>Asset{0}</h1> <p>Sent user agreement to</p><form method="POST" action="/sign/{0}">
    <input placeholder="Name" name="name"><input placeholder="email" name="email">
    <input type="submit"></form>'''.format(asset)

@APP.route('/sign/<asset>', methods=['GET', 'POST'])
def sign_route(asset):
    ''' sign route '''
    asset = asset.upper()
    testuser = {'email':'', 'name':''}
    testuser['email'] = request.form['email']
    testuser['name'] = request.form['name']
    #specify the admin
    admin = {'email':'admin.admin@theadminuser.com', 'name':'Admin of Admin'}
    docuSignModule.userAgreement(admin, testuser, asset)
    return 'sign route {} for user {} - return <a href="/">home</a>'.format(asset, testuser['name'])

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)
