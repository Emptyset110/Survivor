# coding = utf-8
import time
def gmt_to_timestamp( datetimestring ):
	timestamp = time.mktime(time.strptime(datetimestring, '%a, %d %b %Y %H:%M:%S GMT'))
	return timestamp
