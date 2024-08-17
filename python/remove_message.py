# coding=utf-8
import datetime
import requests

cookie = 'your cookie'	  # copy your cookie from browser
csrf   = 'your bili_jct'  # the value of bili_jct in cookie

def bili_message_remove(tid):
	url = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/remove_session' 

	headers = {
  		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Cookie': cookie
	}

	data = 'talker_id=' + str(tid) + '&session_type=1&build=0&mobi_app=web&csrf_token=' + csrf + '&csrf=' + csrf
	response = requests.post(url, data = data, headers = headers)
	print(response.text)

def bili_message_list():
	url = 'https://api.vc.bilibili.com/session_svr/v1/session_svr/get_sessions?session_type=1&group_fold=1&unfollow_fold=0&sort_rule=2'
	#&build=0&mobi_app=web&web_location=000.0000&w_rid=00000000000000000000000000000000&wts=1722934632
	headers = {
  		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
	    'Cookie': cookie
	}

	while True:
		response = requests.get(url, headers = headers)	
		
		response_json = response.json()
		code = response_json['code']
		if code != 0:
			print(response_json)
			break
		data = response_json['data']
		session_list = data['session_list']
		if session_list is None or len(session_list) == 0:
			break
		for item in session_list:
			tid = item['talker_id']
			print ('remove', tid)
			bili_message_remove(tid)


bili_message_list()