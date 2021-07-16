import csv
import numpy as ny

def setup():
    datapath = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data = dataRetrival(datapath)
    getcorrelationnumber(data)

def getcorrelationnumber(data):
    correlationnumber = ny.corrcoef(data["x"],data["y"])
    print(correlationnumber)

def dataRetrival(datapath):
    Temperature = []
    IceCream = []
    with open(datapath) as f:
        df = csv.DictReader(f)
        for i in df:
            Temperature.append(float(row["Temperature"]))
            IceCream.append(float(row["Ice-cream Sales( ₹ )"]))
    return {"x":Temperature,"y":IceCream}



setup()
