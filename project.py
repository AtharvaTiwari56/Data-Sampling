import statistics as st
import pandas as pd
import plotly.figure_factory as pff
import random

dataframe = pd.read_csv('medium_data.csv')
reading_time = dataframe['reading_time'].to_list()
pop_mean = st.mean(reading_time)

mean_data = []

for i in range(0, 100):
    sample_data = []
    for i in range(0, 30):
        rand_ind = random.randint(0, len(reading_time) - 1)
        ind_val = reading_time[rand_ind]
        sample_data.append(ind_val)        
    meanofsam = st.mean(sample_data)
    mean_data.append(meanofsam)

sam_mean = st.mean(mean_data)

fig = pff.create_distplot([mean_data], ['MEANS OF SAMPLE DATA'])
fig.show()

print('Population Mean: '+str(pop_mean))
print('Sample Mean: '+str(sam_mean))