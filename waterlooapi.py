#  c307b2da8c14d41c946d8fe6a1724013



import json 

from uwaterlooapi import UWaterlooAPI 
uw = UWaterlooAPI(api_key="112713075ab3f36db9872dbc84ee874a")
# result = uw.current_weather()
# print result

a= uw.course_schedule("CS","246") 

# print (json.dumps(a, indent=2))


for i in a:
	classes = i["classes"][0]
	class_number = i["class_number"]
	section = i["section"]
	class_begin = classes["date"]["start_time"]
	class_end = classes["date"]["end_time"]
	weekdays = classes["date"]["weekdays"]
	if classes["instructors"]: 
		instructors = classes["instructors"][0] 
	else: 
		insructors = "N/A"
	if (classes["location"]["building"] and classes["location"]["room"]):
		location = classes["location"]["building"] + classes["location"]["room"]
	else:
		location = "N/A"
	open_spot = i["enrollment_capacity"] - i["enrollment_total"]

	print( "Section:\t\t{1}\nClass Number:\t{0}\nInstructors:\t{2}\nClass Time:\t\t{3}-{4}\nDays:\t\t\t{5}\nLocation:\t\t{6}\nSpots:\t\t\t{7}"\
		.format(class_number,section,instructors,class_begin,class_end,weekdays,location,open_spot))
	print( "\n*************************************************************\n")

# print a


