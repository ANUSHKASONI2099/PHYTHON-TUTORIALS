import os 

if (not os.path.exists("Data")):
    os.mkdir("Data")


for i in range (0,50):
    os.mkdir(f"Data/day{i+1}")