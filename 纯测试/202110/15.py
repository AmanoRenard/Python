from os import write


f = open('gushi.txt','w')
li = ['床前明月光，疑是地上霜。\n举头望明月，低头思故乡。']
f.writelines(li)

f.close()

f = open('gushi.txt','r')
copy = open('copy.txt','w')
copy.write(f.read())

f.close()
copy.close()