def test(array):
    n = array.count(0)
    B=[i for i in array if ord(str(i)) != 48]
    return B+[0]*n


A = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
C = [0,1,None,2,False,1,0]

S=[1,2,0,0,0,2,3,0]
print(test(C))
print(ord("0"))

#),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
#([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])