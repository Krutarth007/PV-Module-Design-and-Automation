import requests
import json
import numpy as np


# Clear Sky Insolation Incident on a Horizontal Surface

def CLRSKY_SFC_SW_DWN(la,lo):
	API_call = 'https://asdc-arcgis.larc.nasa.gov/cgi-bin/power/v1beta/DataAccess.py?request=execute&identifier=SinglePoint&parameters=CLRSKY_SFC_SW_DWN&startDate=20160101&endDate=20161201&userCommunity=SSE&tempAverage=CLIMATOLOGY&outputList=JSON&lat={}&lon={}'.format(la,lo)
	response = requests.get(API_call)
	data = response.json()
	dict_data = data['features'][0]['properties']['parameter']['CLRSKY_SFC_SW_DWN']
	info_data = [dict_data[i] for i in dict_data]	
	return info_data


# Maximum NO-SUN Or BLACK Days
def NO_SUN_BLACKDAYS_MAX(la,lo):
	API_call = 'https://asdc-arcgis.larc.nasa.gov/cgi-bin/power/v1beta/DataAccess.py?request=execute&identifier=SinglePoint&parameters=NO_SUN_BLACKDAYS_MAX&userCommunity=SSE&tempAverage=CLIMATOLOGY&outputList=JSON&lat={}&lon={}'.format(la,lo)
	response = requests.get(API_call)
	data = response.json()
	dict_data = data['features'][0]['properties']['parameter']['NO_SUN_BLACKDAYS_MAX']
	info_data = [dict_data[i] for i in dict_data][:-1]
	info_data.append(np.mean(info_data))
	return info_data

la = 23.0225
lo = 72.5714

if __name__ == '__main__':
	print (NO_SUN_BLACKDAYS_MAX(la,lo))

