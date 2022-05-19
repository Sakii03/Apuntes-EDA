def isPalindrome(w):
    D=Dlist()
    for i in w:
      D.addlast(i)
    current1= self._head
    current2= self._tail
    for i in range(len(D)-2)//2):
      if current1.elem!= current2.elem:
       return False
      current1=current.next
      current2=current.prev
        
    return True"""

         

