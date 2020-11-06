from flask import Flask, url_for, render_template, redirect, request
import requests
import json

json_response = None

app = Flask(__name__)

@app.route('/')
# @app.route('/?<page>')
def start():
    page = request.args.get('page')
    if page == None:
        page = 0
    page = int(page)
    print(page)
    org = 'walmartlabs'
    repo = 'thorax'

    url = 'https://api.github.com/repos/' + org + '/' + repo + '/issues'

    # TODO!
    # Do a GET request on url
    global json_response
    if page == 0:
        json_response = requests.get(url).json()
    elif page < 0:
        return render_template('400.html'), 400

    print(page+1)
    # return render_template('main_page.html', issues=json_response);
    _issues = json_response[10*page : min(len(json_response), 10*(page+1))]
    show_prev = True
    show_next = True

    _len_next = min(len(json_response), 10*(page+1)) - 10*page

    # Should the Previous and Next button be functional?
    if _len_next < 1:
        show_next = False
    if page == 0:
        show_prev = False

    return render_template('main_page.html', issues=_issues, _page=page, sn=show_next, sp=show_prev)

@app.route('/issue/<int:id>')
def detailed_view(id):
    # Find the Issue ID
    global json_response
    ret = None
    for resp in json_response:
        if resp['id'] == id:
            ret = resp
            print(ret.keys())
            break

    if ret == None:
        return render_template('404.html'), 404

    # Get comments
    comment_response = requests.get(resp['comments_url']).json()

    # Display the Template page
    return render_template('issue_id_t.html', details=ret, comments=comment_response)

if __name__ == '__main__':
    app.run()
