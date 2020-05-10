# coding:utf-8

import requests
import json
from . import html_stripper
 
def request_data_api(host_url):
    request_url = host_url + '/wp-json/wp/v2/posts?_embed'

    request_results = requests.get(request_url)
 
    return request_results.json()

# wordpressから取得したデータを整形
def make_source(host_url, description_limit):
    wp_data = request_data_api(host_url)
    wp_contents = []

    for data in wp_data:
        wp_link = data['link']
        wp_date = data['date']
        wp_image = ''
        if 'wp:featuredmedia' in data['_embedded']:
            wp_image = data['_embedded']['wp:featuredmedia'][0]['media_details']['sizes']['thumb320']['source_url']
        wp_title = data['title']['rendered']
        wp_description = html_stripper.MyHtmlStripper(data['content']['rendered']).value.replace('\n','')[:description_limit] + '...'

        wp_contents.append({
                            'wp_link' : wp_link,
                            'wp_date' : wp_date,
                            'wp_image' : wp_image,
                            'wp_title' : wp_title,
                            'wp_description' : wp_description
                            })

    return wp_contents