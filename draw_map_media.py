import matplotlib.pyplot as plt

#####################################################
#   Part 1: Data input                              #
#                                                   #
#   Goal: For each spot in the datasets, record     #
#       its latitude, longitude and frequecy in     #
#       three different 1-dimension list.           #
#####################################################

print("Please input a single number, 1 or 2.")
print("1 is for brightkite.checkin.")
print("2 is for gowalla.checkin.")
input_num = input()
if input_num == '1':
    file_name = 'brightkite.checkin'
elif input_num == '2':
    file_name = 'gowalla.checkin'
else:
    print("Unexpected input!")
    exit()

dataset = open(file_name, "r")
# The first two lines are irrelavant data.
dataset.readline()
dataset.readline()

lati_list = []  # lati_list[i] is ith spot's latitude.
logi_list = []  # logi_list[i] is ith spot's logitude.
freq_list = []   # num_list[i] is ith spot's frequecy.
spot_cnt = -1   # spot_cnt records the biggest # of among all spots.
                # If spot_cnt == -1, it means that there has not been
                #     any spot read.

pnt = dataset.readline()
while (pnt != "" 
    and pnt != " " 
    and pnt != "\n"):
    line_array = pnt.split(" ")

    if (int)(line_array[-1]) > spot_cnt:
        lati_list.append(line_array[-3])
        logi_list.append(line_array[-2])
        freq_list.append(1)
        spot_cnt += 1
    else:
        freq_list[(int)(line_array[-1])] += 1
    
    pnt = dataset.readline()

dataset.flush()
dataset.close()

for i in range(spot_cnt+1):
    lati_list[i] = (float)(lati_list[i])
    logi_list[i] = (float)(logi_list[i])
    freq_list[i] = (int)(freq_list[i])

lati_max = lati_list[0]
lati_min = lati_list[0]
logi_max = logi_list[0]
logi_min = logi_list[0]
freq_max = freq_list[0]
freq_min = freq_list[0]

for i in range(spot_cnt+1):
    if lati_list[i] > lati_max:
        lati_max = lati_list[i]
    elif lati_list[i] < lati_min:
        lati_min = lati_list[i]

    if logi_list[i] > logi_max:
        logi_max = logi_list[i]
    elif logi_list[i] < logi_min:
        logi_min = logi_list[i]

    if freq_list[i] > freq_max:
        freq_max = freq_list[i]
    elif freq_list[i] < freq_min:
        freq_min = freq_list[i]

print("Begin Plotting")

discrete = freq_list
discrete.sort()
discrete = (list)(set(discrete))

darkest = len(discrete)
grey_list = []
for i in range(spot_cnt+1):
    grey_list.append( (discrete.index(freq_list[i])/darkest)*0.3 + 0.7 )

plt.scatter(x=logi_list, y=lati_list, s=3, c=grey_list, cmap='cool')
plt.title(file_name, fontsize=20)
plt.xlabel("Longitude", fontsize=10)
plt.ylabel("Latitude", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()



print("End")
