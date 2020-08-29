# Last change: 2020/8/30 0:56

import re
import sys
import time
import matplotlib.pyplot as plt

time_fmt = '%Y-%m-%dT%H:%M:%SZ'

#####################################################
#   Part 1: Data input                              #
#                                                   #
#   Goal: For each spot in the datasets, record     #
#       its latitude, longitude and frequecy in     #
#       three different 1-dimension list.           #
#####################################################

file_name = sys.argv[1]
dataset = open(file_name, "r")
# Notice: the first two elements are useless, so pop them.
data_list = dataset.readlines()
data_list = data_list[2:]

user_list = []  # user_list[i] is ith spot's user. This list is useless temporarily.
time_list = []  # time_list[i] is ith spot's time.
lati_list = []  # lati_list[i] is ith spot's latitude.
logi_list = []  # logi_list[i] is ith spot's logitude.
loid_list = []  # freq_list[i] is ith spot's frequecy.

for i in data_list:
    if (i == ""
        and i == " "
        and i == "\n"):
        break
    line_array = re.split(',| ', i)
    user_list.append(int(line_array[0]))
    tmp_time = time.strptime(line_array[1], time_fmt)
    time_list.append(time.mktime(tmp_time))
    lati_list.append(float(line_array[2]))
    logi_list.append(float(line_array[3]))
    loid_list.append(int(line_array[4]))

print("Please input the time range you want.")
print("The form should be like \'" + time_fmt + "\' .")
print("You can also input 'Default' to make the begining as early as possible or make the ending as late as possible.")
print("For example:")
print("2020-08-21T09:30:00Z")
print("Or you may input:")
print("Default")

begin_index = 0
end_index = len(time_list) - 1

exp_begining = input('Input the begining:   ')
if exp_begining != 'Default':
    exp_begining = time.strptime(exp_begining, time_fmt)
    exp_begining = time.mktime(exp_begining)
    while time_list[begin_index] < exp_begining:
        begin_index += 1
exp_ending = input('Input the ending:   ')  
if exp_ending != 'Default':
    exp_ending = time.strptime(exp_ending, time_fmt)
    exp_ending = time.mktime(exp_ending)
    while time_list[end_index] > exp_ending:
        end_index -= 1
assert begin_index <= end_index

spot_cnt = begin_index - 1

plot_lati_list = []
plot_logi_list = []
plot_freq_list = []
tmp = begin_index
while tmp <= end_index:
    if loid_list[tmp] > spot_cnt:
        plot_lati_list.append(lati_list[tmp])
        plot_logi_list.append(logi_list[tmp])
        plot_freq_list.append(1)
        spot_cnt += 1
    else:
        plot_freq_list[spot_cnt] += 1
    tmp += 1

dataset.flush()
dataset.close()

plot_lati_max = plot_lati_list[0]
plot_lati_min = plot_lati_list[0]
plot_logi_max = plot_logi_list[0]
plot_logi_min = plot_logi_list[0]
plot_freq_max = plot_freq_list[0]
plot_freq_min = plot_freq_list[0]

for i in range(spot_cnt+1):
    if plot_lati_list[i] > plot_lati_max:
        plot_lati_max = plot_lati_list[i]
    elif plot_lati_list[i] < plot_lati_min:
        plot_lati_min = plot_lati_list[i]

    if plot_logi_list[i] > plot_logi_max:
        plot_logi_max = plot_logi_list[i]
    elif plot_logi_list[i] < plot_logi_min:
        plot_logi_min = plot_logi_list[i]

    if plot_freq_list[i] > plot_freq_max:
        plot_freq_max = plot_freq_list[i]
    elif plot_freq_list[i] < plot_freq_min:
        plot_freq_min = plot_freq_list[i]

print("Begin Plotting")

discrete = plot_freq_list
discrete.sort()
discrete = (list)(set(discrete))

darkest = len(discrete)
grey_list = []
for i in range(spot_cnt+1):
    grey_list.append( (discrete.index(plot_freq_list[i])/darkest)*0.3 + 0.7 )

plt.scatter(x=plot_logi_list, y=plot_lati_list, s=3, c=grey_list, cmap='cool')
plt.title(file_name, fontsize=20)
plt.xlabel("Longitude", fontsize=10)
plt.ylabel("Latitude", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()

print("End")