file = open("datasp1.txt",  encoding= "utf8" , mode = "r")


datas = file.read().split("\n")

data = list(datas)


am = ["shopid","price_min","price_max","rating_star","shop_location","stock","sold","price"]
for i in range(len(data)):
	if data[i] in am:
		data[i] = data[i] +":" + data[i + 1]
	elif data[i] =="name":
		data[i] = data[i] +":" + data[i + 1] + data[i + 2] + data[i + 3]
	elif data[i] == "rating_count":
		data[i] = data[i] + "\n 5 sao" + ":" +  data[i + 1] + "\n 4 sao" + ":" +  data[i + 2] + "\n 3 sao" +  ":" + data[i + 3] + "\n 2 sao" + ":" + data[i + 4] + "\n 1 sao" + ":" +  data[i + 5] + "\n Số bình luận" + ":" +  data[i + 6] + "\n"

	else:
		data[i] = ""

unempty_lines = []
for i in range(len(data)):
	if data[i] != "":
		unempty_lines.append(data[i])
data = unempty_lines

file = open("Shpp.txt", encoding= "utf8" , mode = "w")
for i in range (len(data)):
	file.write(data[i] + "\n")


