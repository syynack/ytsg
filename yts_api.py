#!/usr/bin/env python

import requests

API_LIST = 'http://yify.is/api/v2/list_movies.json?limit={}&page={}&query_term={}&{}&sort_by={}&order_by={}&with_rt_ratings={}'
API_DETAIL = 'http://yify.is/api/v2/movie_details.json?movie_id={}&with_images={}&with_cast={}'


def api_list_movies(limit, page, query_term, genre, sort_by, order_by, with_rt_ratings):
	if genre != 'All':
		response = requests.get(API_LIST.format(limit, page, query_term, 'genre=' + genre, sort_by, order_by, with_rt_ratings))
	else:
		response = requests.get(API_LIST.format(limit, page, query_term, '', sort_by, order_by, with_rt_ratings))

	status_code = response.status_code
	headers = response.headers
	content = response.content

	return {
		"status_code": status_code,
		"headers": headers,
		"content": content
	}


def api_movie_detail(self):
	response = requests.get(API_DETAIL.format(self.movie_id, self.with_images, self.with_cast))

	status_code = response.status_code
	headers = response.headers
	content = response.content

	return {
		"status_code": status_code,
		"headers": headers,
		"content": content
	}

