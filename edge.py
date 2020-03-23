# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:37:15 2020

@author: kunal
"""
import cv2
import requests
import time
import string
import random

edge_id = 7

URL_images = "http://localhost:8000/api/images/"
URL_edges = "http://localhost:8000/api/edges/"
URL_up ="http://localhost:8000/api/uploads/"


r_edges = requests.get(url = URL_edges)
edges = r_edges.json()
flag_edge = 0 

for i in edges:
    if i['id'] == edge_id:
        flag_edge = 1
        break
    
if not flag_edge:
    data = {'id':edge_id}
    r = requests.post(url = URL_edges, data = data)
    #print('posted')
    
inf = 1
#infinite loop
while inf:
    r_edges = requests.get(url = URL_edges)
    edges = r_edges.json()
    wait_time = 10
    gray_scale = False
    for i in edges:
        if i['id'] == edge_id:
            wait_time = i['time_setting']
            gray_scale = i['gray_scale_setting']
            break
    
    
    camera = cv2.VideoCapture(0)

    
    img_n = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 4))
    img_name = str(img_n)+'.png'
    #print(img_name)
    
    return_value, image = camera.read()
    if gray_scale:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    cv2.imwrite(img_name,image)
    del(camera)
    img = cv2.imread(img_name)
    files = {'image': open('image.jpg', 'rb')}
    res = requests.post(url = URL_up, files = files)
    #print(res.text)
    
    data_img = {'image': "http://localhost:8000/api/uploads/"+img_name ,
                'gray_scale': gray_scale,
                'edge_id':edge_id
                }
    r = requests.post(url = URL_images, data = data_img)        
    
    #print('executed')
    time.sleep(wait_time)
    

        
        