classmates = ['Kate','HanMeimei','Tom']
print('classmates长度是：%s' %len(classmates))
print('索引[0]:%s' %classmates[0])
print('索引[1]:%s' %classmates[1])
print('索引[2]:%s' %classmates[2])
# print('超出索引：%s' %classmates[3])
print('获取最后的一个元素：classmates[-1] = %s' %classmates[-1])
classmates.append('Adam')
print('classmates.append(\'Adam\'):%s' %classmates)
classmates.pop(1)
print('classmates.pop(1):%s' %classmates)
classmates.pop(0)
print('classmates.pop(0):%s,括号中是索引的位置' %classmates)
classmates[0] = 'David'
print('替换指定下标的元素 classmates[0] = \'David\' %s' %classmates)