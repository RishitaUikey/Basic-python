'''How to merge to dictinoary 
we use update command or we use **'''

'''x={'a':1,'b':2,'c':3}
y={'d':4,'e':5,'f ':6}

x.update(y)
print(x)'''

x={'a':1,'b':2,'c':3}
y={'d':4,'e':5,'f ':6}
merge_xy={**x,**y}
print(merge_xy)
