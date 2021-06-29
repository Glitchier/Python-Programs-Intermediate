import pandas

data = pandas.read_csv("weather_data.csv")

temp_col = data["temp"]
avg_temp = data["temp"].mean()
max_temp = data["temp"].max()

print(temp_col)
print(avg_temp)
print(max_temp)

print(data[data.day == "Monday"])
#or
monday=data[data.day == "Monday"]

print(monday.condition) #This will give the condition of monday
print(data[data.temp == data.temp.max()])

#monday temp in F

monday_temp=int(monday.temp)
temp_in_f = monday_temp * 9/5 + 32
print(temp_in_f)

#creating dic from scratch

data_dic = {
    "students" : ["Amy","James","Yue"],
    "scores" : [78,89,77]
}

data = pandas.DataFrame(data_dic)
data.to_csv("new_dic.csv")