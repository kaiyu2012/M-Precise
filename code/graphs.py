

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import seaborn as sns

PNGS = {
    'tcell': ["Diff_TCell.png", "T Cell Chart"],
    'bcell': ["Diff_BCell.png","B Cell Chart"],
    "mono": ["Diff_Mono.png","Monotypes Chart"],
    "neu": ["Diff_Neu.png","neutrophils Chart"]
}


def plot_diff(diff_data, cate):
    # x-coordinates of left sides of bars 
    left = list(range(0, len(diff_data)))
  
    # heights of bars
    height = []
  
    # labels for bars
    tick_label = []

    for x in diff_data:
        tick_label.append(x)
        height.append(diff_data[x])

    print("\n\n\n\n\n--------Height Test------------")
    print(height)
    # plt.plot(left, height, color='green', linestyle='dashed', linewidth = 1,
    #      marker='o', markerfacecolor='blue', markersize=3)
    # plt.bar(left, h, 
    #     width = 0.8, color = ['red', 'green'])

    plt.scatter(left, height, label= "stars", color= "green", 
            marker= "*", s=3)
    
    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title(PNGS[cate][1])
    
    # function to show the plot
    # plt.show()
    plt.savefig(PNGS[cate][0])



def plot_d(diff_data, cate):
    # x-coordinates of left sides of bars 
    left = list(range(0, len(diff_data)))
  
    # heights of bars
    height = []
  
    # labels for bars
    tick_label = []

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title(PNGS[cate][1])


    for x in diff_data:
        tick_label.append(x)
        height.append(diff_data[x])

    fig = plt.figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)


    plt.scatter(left,height,alpha=0.7,cmap=cm.Paired, s=1)
    # plt.show()
    plt.savefig(PNGS[cate][0])

