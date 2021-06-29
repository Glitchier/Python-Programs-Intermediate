import pandas

data = pandas.read_csv("CP_Squirrel_Data_2018.csv")

grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "Color" : ["Gray", "Red", "Black"],
    "Count" : [grey_sq_count, red_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dic)
df.to_csv("Squirrel_count.csv")