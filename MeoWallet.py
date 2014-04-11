#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json

APIKEY = # Your API Key
authorization_header = "WalletPT " + APIKEY

api_endpoint = "https://services.wallet.pt/api/v2/"
#api_endpoint = "https://services.wallet.codebits.eu/api/v2/" USE FOR CODEBITS SANDBOX!

accept_endpoint = # Your Accept Callback Endpoint
cancel_endpoint = # Your Cancel Callback Endpoint

headers = {"content-type": "application/json",
	"Authorization": authorization_header}

# Checkout

def checkout(client, amount, currency, items, internal_transaction_id):
	''' Create payment order
		https://developers.wallet.pt/procheckout/resources#apiv2checkout'''
	payload = {"payment": {
					"client" : client,
					"amount" : amount,
					"currency": currency,
					"items" : items
					},
				"url_confirm" : accept_endpoint + str(internal_transaction_id),
				"url_cancel": cancel_endpoint + str(internal_transaction_id),
	}

	r = requests.post(api_endpoint + "checkout", 
		data=json.dumps(payload), headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s['id'], s['url_redirect'], s
	else:
		raise Exception(s['code'], s['message'], s)

def get_checkout(transaction_id):
	'''	Get payment order. Returns if it has been paid or not.
		https://developers.wallet.pt/procheckout/resources#get_checkout'''
	r = requests.get(api_endpoint +"checkout/" + str(transaction_id),
		 headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s
	else:
		raise Exception(s['code'], s['message'], s)

def delete_checkout(transaction_id):
	'''	Delete non paid checkout.
		https://developers.wallet.pt/procheckout/resources#delete_checkout'''
	r = requests.delete(api_endpoint + "checkout/" + str(transaction_id),
		 headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s
	else:
		raise Exception(s['code'], s['message'], s)

# OPERATIONS
def get_operations(limit = 10):
	'''	Get All operations.
		https://developers.wallet.pt/procheckout/resources#get_operations'''
	payload = {"limit" : limit}
	r = requests.get(api_endpoint +"operations/", 
			params = payload, headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s
	else:
		raise Exception(s['code'], s['message'], s)

def get_operation(operation_id):
	'''	Get certain operation
		https://developers.wallet.pt/procheckout/resources#get_operation'''
	r = requests.get(api_endpoint +"operations/" + str(operation_id),
		 headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s
	else:
		raise Exception(s['code'], s['message'], s)

def refrund(transaction_id):
	'''	Refund a certain transaction. It doesn't work for all.
		https://developers.wallet.pt/procheckout/resources#refund'''
	r = requests.post(api_endpoint +"operations/" + str(transaction_id) +"/refund",
		 headers = headers)
	
	s = r.json()
	if r.status_code == requests.codes.ok:
		return s
	else:
		raise Exception(s['code'], s['message'], s)


if __name__ == "__main__":
	client = {"name": "Jar Jar Binks",
			  "email": "jarjar@gungan.naboo",
			  "address": {
			  	"country": "pt",
			  	"address": "Sala Tejo, Mesa Lagostas",
			  	"city": "Lisbon",
			  	"postalcode" : "1000-000"
			  }
	  		}
	items = [{"ref":123,
			  "name": "proj3 stock",
			  "descr": "cenas",
			  "qt":2}]
	print checkout(client, 10, "EUR", items, 1)