import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = st.mean(data)
sd = st.stdev(data)
print("mean ",mean)
print("standard deviation ",sd)

def random_set(counter):
    dataset = []
    for i in range(0,counter):
        j = random.randint(0,len(data)-1)
        value = data[j]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


mean_list = []
for i in range(0,1000):
    set_mean = random_set(100)
    mean_list.append(set_mean)
mean2 = st.mean(mean_list)
print(mean2)   
sd2 = st.stdev(mean_list)
print(sd2)   

first_sd_start,first_sd_end = mean2-sd2,mean2+sd2
second_sd_start,second_sd_end = mean2-(2*sd2),mean2+(2*sd2)
third_sd_start,third_sd_end = mean2-(3*sd2),mean2+(3*sd2)

fig = ff.create_distplot([mean_list],["result"],show_hist = False)
fig.add_trace(go.scatter(x = [mean2,mean2],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.scatter(x = [first_sd_start,first_sd_start],y = [0,0.17],mode = "lines",name = "SD1"))
fig.add_trace(go.scatter(x = [first_sd_end,first_sd_end],y = [0,0.17],mode = "lines",name = "SD1"))
fig.add_trace(go.scatter(x = [second_sd_start,second_sd_start],y = [0,0.17],mode = "lines",name = "SD2"))
fig.add_trace(go.scatter(x = [second_sd_end,second_sd_end],y = [0,0.17],mode = "lines",name = "SD2"))
fig.add_trace(go.scatter(x = [third_sd_start,third_sd_start],y = [0,0.17],mode = "lines",name = "SD3"))
fig.add_trace(go.scatter(x = [third_sd_end,third_sd_end],y = [0,0.17],mode = "lines",name = "SD3"))
fig.show()

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean_data1 = st.mean(data)
sd_data1 = st.stdev(data)
print("mean ",mean_data1)
print("standard deviation ",sd_data1)

fig = ff.create_distplot([mean_list],["result"],show_hist = False)
fig.add_trace(go.scatter(x = [mean2,mean2],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.scatter(x = [mean_data1,mean_data1],y = [0,0.17],mode = "lines",name = "mean_data1"))
fig.add_trace(go.scatter(x = [first_sd_end,first_sd_end],y = [0,0.17],mode = "lines",name = "SD1"))
fig.show()


df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

mean_data2 = st.mean(data)
sd_data2 = st.stdev(data)
print("mean ",mean_data2)
print("standard deviation ",sd_data2)

fig = ff.create_distplot([mean_list],["result"],show_hist = False)
fig.add_trace(go.scatter(x = [mean2,mean2],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.scatter(x = [mean_data2,mean_data2],y = [0,0.17],mode = "lines",name = "mean_data2"))
fig.add_trace(go.scatter(x = [first_sd_end,first_sd_end],y = [0,0.17],mode = "lines",name = "SD1"))
fig.add_trace(go.scatter(x = [second_sd_end,second_sd_end],y = [0,0.17],mode = "lines",name = "SD2"))
fig.show()


df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_data3 = st.mean(data)
sd_data3 = st.stdev(data)
print("mean ",mean_data3)
print("standard deviation ",sd_data3)

fig = ff.create_distplot([mean_list],["result"],show_hist = False)
fig.add_trace(go.scatter(x = [mean2,mean2],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.scatter(x = [mean_data3,mean_data3],y = [0,0.17],mode = "lines",name = "mean_data3"))
fig.add_trace(go.scatter(x = [third_sd_end,third_sd_end],y = [0,0.17],mode = "lines",name = "SD3"))
fig.add_trace(go.scatter(x = [second_sd_end,second_sd_end],y = [0,0.17],mode = "lines",name = "SD2"))
fig.show()

#fig = ff.create_distplot([data],["Math_score"],show_hist = False)
#fig = ff.create_distplot([mean_list],["Math_score"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean2],y = [0,0.2],mode = "lines",name = "mean"))
#fig.show()