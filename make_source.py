# coding:utf-8

import util
from flask import Flask, render_template, request
from pathlib import Path
import env

PER_PAGE = env.PER_PAGE
DESCRIPTION_LIMIT = env.DESCRIPTION_LIMIT
HOST_URL = env.HOST_URL
HTML_FILEPATH = env.HTML_FILEPATH
FAVICON_FILE = env.FAVICON_FILE
STATIC_FOLDER = env.STATIC_FOLDER
TEMPLATE_FOLDER = env.TEMPLATE_FOLDER

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)

@app.route("/") 
def render_source():
    wp_contents = util.get_data_api.make_source(HOST_URL, DESCRIPTION_LIMIT, PER_PAGE)
    return render_template(str(HTML_FILEPATH), wp_contents=wp_contents, host_url=request.host_url)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file(FAVICON_FILE)

if __name__ == '__main__':
    app.run(debug=True)
