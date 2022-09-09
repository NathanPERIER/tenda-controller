
from dataobj import DataObject


class PrivateWiFiObject(DataObject) :
	def __init__(self) :
		self.wrlEn    = "1"
		self.wrlEn_5g = "1"
		self.security    = "wpawpa2psk"
		self.security_5g = "wpawpa2psk"
		self.ssid    = "Tenda_B615D0"
		self.ssid_5g = "Tenda_B615D0_5G"
		self.hideSsid    = "0"
		self.hideSsid_5g = "0"
		self.wrlPwd    = "password"
		self.wrlPwd_5g = "password_5g"

class GuestWiFiObject(DataObject) :
	def __init__(self) :
		self.guestEn    = "0"
		self.guestEn_5g = "0"
		self.guestSecurity    = "wpapsk"
		self.guestSecurity_5g = "wpapsk"
		self.guestSsid    = "Tenda_B615D0_Guest"
		self.guestSsid_5g = "Tenda_B615D0_Guest_5G"
		self.guestWrlPwd    = "password"
		self.guestWrlPwd_5g = "password_5g"
		self.effectiveTime = "4"
		self.shareSpeed = "0"