from bingapi import bingapi

def getbingid():
	app_ID="F0EB80C0CD181F47B512016FD3A74CDB58D302B4"
	bing = bingapi.Bing(app_ID)
	return bing
