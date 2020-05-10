# coding:utf-8

from jinja2 import Template, Environment, FileSystemLoader

# HTML-jinja2 テンプレレンダリング
def render_html_souce(body, wp_contents):
    template = Template(body)

    data_temp = {
    'wp_contents': wp_contents,
    }
    body = template.render(data_temp)

    return body
