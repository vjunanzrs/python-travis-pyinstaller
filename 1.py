#! python3
# -*- coding: utf-8 -*-
import os

html1 = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title></title>
  <style>
    p{
      text-align: center;
    }
    img{
      width: 600px;
      height: 450px;
    }
  </style>
</head>
<body>'''
html2 = '''
  <p>abc</p>
  <p><img src="image/xyz" /></p>
  <hr>'''
html3 = '''
</body>
</html>'''

# a
# fileList = ['a.png', 'b.png']

# b
filePath = os.path.join(os.getcwd(), 'image')
fileList = os.listdir(filePath)

body = ''

for i in range(len(fileList)):
  htmlFileText = html2.replace('abc', fileList[i]).replace('xyz', fileList[i])
  body = body + htmlFileText

html = html1 + body +html3

htmlFileName = 'index.html'
with open(htmlFileName, 'w', encoding='utf-8') as f:
  f.write(html)
print('all done.')
