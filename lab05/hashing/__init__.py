class HashTable:
  def __init__(self):
      self.size = 11
      self.full = 0 #an accumulator for how full the table is as put() is called. 
      self.load = 0.60
      self.slots = [None] * self.size
      self.data = [None] * self.size

  def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots))
    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data
      self.full += 1
    else:
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data  #replace
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot,len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot]=key
          self.data[nextslot]=data
          self.full += 1
        else:
          self.data[nextslot] = data #replace
    if self.full/self.size > self.load: 
      #the accumulator will increase everytime something gets added to the hashtable, and when the acccumulator/size is greater than 65%, it will resize
      self.resize(self.size)
                   
  def resize(self, num):
      #resize to next prime number
      x = 0
      while x == 0:
          #the size will increase by 1 everytime the while loops runs 
          #it will increase by 1 until it hits a prime number
          num += 1
          #prime number finder 
          for i in range(2,num):
              if (num % i) == 0:
                x = 0
                break
              else:
                x = 1
      #storing the information of the current hashtable into temp
      tempSlots = self.slots
      tempData = self.data
      #re-initializing the size, slots, resetting data and accumulator
      self.size = num
      self.slots = [None] * num
      self.data = [None] * num
      self.full = 0
      #putting the erased data back into the resized hash table to their new positions
      for i in range(len(tempData)):
        if tempData[i] != None:
          self.put(tempSlots[i],tempData[i])
      return num

  def hashfunction(self,key,size):
       return key%size

  def rehash(self,oldhash,size):
      return (oldhash+1)%size

  def get(self,key):
    startslot = self.hashfunction(key,len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and  \
                         not found and not stop:
       if self.slots[position] == key:
         found = True
         data = self.data[position]
       else:
         position=self.rehash(position,len(self.slots))
         if position == startslot:
             stop = True
    return data

  def __getitem__(self,key):
    return self.get(key)

  def __setitem__(self,key,data):
    self.put(key,data)


H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)