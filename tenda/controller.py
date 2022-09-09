
from tenda.dataobj import PrivateWiFiObject, GuestWiFiObject

import os
import requests
from urllib.error import HTTPError


class TendaController :

	def __init__(self, base_url: str, password_hash: str) :
		self._url    = base_url
		self._hash   = password_hash
		self._cookie = None
	
	def connect(self) :
		url = os.path.join(self._url, 'login/Auth')
		headers = {
			'Origin': self._url,
			'Referer': os.path.join(self._url, 'login.html'),
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		if self._cookie :
			headers['Cookie'] = self._cookie
		payload = {
			'username': 'admin',
			'password': self._hash
		}
		response = requests.post(url, headers=headers, data=payload, allow_redirects=False)
		if not response.ok :
			raise HTTPError(f"Request to {url} returned with code {response.status_code}")
		if 'password' in response.cookies :
			self._cookie = f"password={response.cookies['password']}"
		else :
			raise ValueError('Impossible to connect with password')

	def getConfig(self) -> str :
		# TODO
		return None
	
	def getPrivateWiFiState(self) -> PrivateWiFiObject :
		res = PrivateWiFiObject()
		url = os.path.join(self._url, 'goform/WifiBasicGet')
		headers = {
			'Referer': os.path.join(self._url, 'wireless_ssid.html'),
			'Cookie': self._cookie
		}
		response = requests.get(url, headers=headers)
		if not response.ok :
			raise HTTPError(f"Request to {url} returned with code {response.status_code}")
		res.loadDict(response.json())
		return res
	
	def getGuestWiFiState(self) -> GuestWiFiObject :
		res = GuestWiFiObject()
		# TODO
		return res
	
	def setPrivateWiFiState(self, enable_2_4: bool, enable_5: bool) :
		config = self.getPrivateWiFiState()
		prev_2_4 = config.wrlEn
		prev_5   = config.wrlEn_5g
		config.wrlEn    = "1" if enable_2_4 else "0"
		config.wrlEn_5g = "1" if enable_5   else "0"
		if prev_2_4 == config.wrlEn and prev_5 == config.wrlEn_5g :
			return
		url = os.path.join(self._url, 'goform/WifiBasicSet')
		headers = {
			'Origin': self._url,
			'Referer': os.path.join(self._url, 'wireless_ssid.html'),
			'Content-Type': 'application/x-www-form-urlencoded',
			'Cookie': self._cookie
		}
		response = requests.post(url, headers=headers, data=config.getDict())
		if not response.ok :
			raise HTTPError(f"Request to {url} returned with code {response.status_code}")
		response_json = response.json()
		if response_json['errCode'] != 0 :
			raise HTTPError(f"Request to {url} yielded error code {response_json['errCode']}")

	def setGuestWiFiState(self, enable_2_4: bool, enable_5: bool, validity: int) :
		if validity < 0 or validity > 24 :
			raise ValueError(f"Invalid value for guest Wi-Fi validity : {validity}")
		config = self.getGuestWiFiState()
		config.guestEn    = "1" if enable_2_4 else "0"
		config.guestEn_5g = "1" if enable_5   else "0"
		config.effectiveTime = str(validity)
		# TODO
