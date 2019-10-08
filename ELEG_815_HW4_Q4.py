import numpy as np
from scipy import spatial
from PIL import Image
import random
import operator

img = Image.open('D:\\Courses\\Fall 19\\ELEG 815 Statistical Learning\\HW4\\Homework4Files\\UD.jpg','r')
img = img.resize((400,300))
img = img.convert('RGB')
width, height = img.size
pix_lst = list(img.getdata())
k = 10
# ------------------ Create list of Clusters, Example [[],[],[]] for k = 3-------------------------
clusters = [[] for i in range(k)]
inital_centers = [0]*k
for i in range(k):   
    flag = True
    while flag:
        ind = random.randint(1,len(pix_lst))
        if pix_lst[ind] not in inital_centers:
            inital_centers[i] = pix_lst[ind]
            flag = False
        else:
            continue
print('Initial Centers :',inital_centers)
old_Centers = [0,0,0]
new_centers = inital_centers
iteration = 1
while old_Centers != new_centers:
    print('Converging Iteration :',iteration)
    iteration += 1
    old_Centers = new_centers
    for pixel in range(len(pix_lst)):
        distances = []
        for center in inital_centers:
            dist = spatial.distance.euclidean(center,pix_lst[pixel])
            distances.append(dist)
        ind = distances.index(min(distances))
        clusters[ind].append(pix_lst[pixel]) 
    #------------------Calculate New Centers--------------------------
    # https://stackoverflow.com/questions/497885/python-element-wise-tuple-operations-like-sum
    new_centers = []
    for cluster in clusters:
        t = (0,0,0)
        for pixelTuple in cluster:
            t = tuple(map(operator.add,t,pixelTuple))
        new_center = tuple(map(lambda x: int(x/len(cluster)),t))
        new_centers.append(new_center)

"""Reconstruct Image from Pixel Tuples"""
newImage = Image.new('RGB',(width,height))
rimg = newImage.load()
print('Reconstructing Image ...')
for i in range(height):
    for j in range(width):
        for index,cluster in enumerate(clusters):
            if(pix_lst[i*width+j]) in cluster:
                rimg[j,i] = new_centers[index]
newImage.save('D:\\Courses\\Fall 19\\ELEG 815 Statistical Learning\\HW4\\Homework4Files\\newUD.jpg','jpeg')
print('Finished !')
