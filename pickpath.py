#coding=utf-8
import os
#---生成的是无顺序的--
# def print_file(dirname):
	# f=open("./ingredient_test_patch128_353_featurelist.txt",'w')
	# for path,dirs,files in os.walk(dirname,False):
		
		# for file in files:
			# # file_name=os.path.join(path,file)
			# # f.write(file_name+'\n')
			# f.write(file+'\n')
	# f.close()
	
# print_file(r"/home/vipl/luozhengdong/china_food/feature_patch128/ingredient_test_patch128_353/")


#--生成的是有顺序的--
f = open("./ingredient_test_patch128_353_featurelist—1.txt",'w') #先创建一个空的文本
path =r"/home/vipl/luozhengdong/china_food/feature_patch128/ingredient_test_patch128_353/"   #指定需要读取文件的目录
files =os.listdir(path) #采用listdir来读取所有文件
files.sort() #排序
s= []                   #创建一个空列表
for file_ in files:     #循环读取每个文件名
#    print(path +file_)
    if not  os.path.isdir(path +file_):  #判断该文件是否是一个文件夹
        f_name = str(file_)
#        print(f_name)
        s.append(f_name)  # 把当前文件名返加到列表里
        f.write(f_name + '\n') # 写入之前的文本中
