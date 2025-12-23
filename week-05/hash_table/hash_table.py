class item:
    def __init__(self,key:str,value:int):
        self.key = key
        self.value = value
        
    
def linear_search(items,size,key) -> item:
    for i in range(size):
        if items[i].key == key:
            return items[i]
    return None

if __name__ == "__main__":
    items = []
    item1 = item("foo",10)
    item2 = item("bar",12)
    item3 = item("char",5)
    items.append(item1)
    items.append(item2)
    items.append(item3)
    print(items)
    num_items = len(items)
    
    found = linear_search(items=items,size=num_items,key ="foo")
    if (not found):
        print("1")
    
    print("linear_search: value of 'bob' is", found.value)
    
        