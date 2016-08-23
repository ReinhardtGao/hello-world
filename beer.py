n = 10 # n 为 买酒钱
all = n // 2    # all 为 所能喝到的酒
a = n // 2	# a 为 剩余的啤酒瓶子
b =  n // 2	# b 为剩余的啤酒盖
def f(a, b):    # 定义当前所能换到的酒
	return (a // 2) + (b // 4 )
while True:
	x = f(a,b)    
	all = all + x
	a = a % 2 + x
	b = b % 4 + x
	if a < 2 and b < 4 : break
print(all,a ,b )	# 总共喝的酒，剩余的瓶子、盖子

'''作者：在剑
链接：http://www.zhihu.com/question/35726119/answer/78117220
来源：知乎
著作权归作者所有，转载请联系作者获得授权。'''

