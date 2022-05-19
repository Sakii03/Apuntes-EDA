class stack:
    def __init__(self):
        self.item= []
        
    def __len__(self):
        return len(self.item)
    
    def isEmpty(self):
        if len(self)== 0:
            return len(self)==0
        
           # return = True #también puedes poner return len(self) ==0
        
       # else:
        #    return False
        
    def __str__(self):
        return str(self.item)
    

    def push(self, e):
        self.item.append(e)
        
    
    def pop(self):
        if len(self) ==0:
            print("Lista Vacía")
            
        else:
            self.item.pop()
        
    def top(self):
        if len(self)==0:
            print("Lista Vacía")
        
        else:
            return self.item[-1]
        
        
def reverseword(a):
    S=stack()
    for i in a:
        S.push(i)
    w = ""
    while not S.isEmpty():
        w= w+S.pop()
    return w

print(reverseword("Abracadabra"))