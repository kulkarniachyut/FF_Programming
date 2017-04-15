from collections import Counter

class Item :
    '''
    Creates an Item object with name and value attributes
    '''
    def __init__(self,name,value) :
        '''
        create a constructor and initialise the object with attributes
        '''
        self.name = name
        self.value = value

    def get_item(self) :
        '''
        returns the object itself
        '''
        return self

class ItemLists :
    '''
    Insert, get unique, get All items from list
    '''
    items_counter = Counter()
    items_set = set()

    def __init__(self) :
        '''
        initialise a dictionary and a set
        '''
        self.items_counter = Counter()
        self.items_set = set()

    def insert_item(self, item) :
        '''
        inserts an item into the dictionary
            if already exists updates the count

        also inserts into a set
            if already exists removes from set to maintain unique element constraint
        '''

        if item not in self.items_counter :
            self.items_set.add(item)
            self.items_counter[item] = 1
        else :
            self.items_counter[item]+=1
            if item in self.items_set :
                self.items_set.remove(item)


    def get_unique_items(self) :
        '''
        returns the unique items as a set
        '''
        return self.items_set


    def get_all_items(self) :
        '''
        returns the entire dictionary with items and their frequencies
        '''
        return self.items_counter



def main() :
    '''
    test some inputs
    '''
    x = Item("Achyut" , 100)
    a = Item("Achyut1" , 101)
    b = Item("Achyut2" , 102)
    c = Item("Achyut3" , 1004)

    y = ItemLists();

    y.insert_item(x)
    y.insert_item(b)
    y.insert_item(c)
    y.insert_item(x)

    for item in y.get_unique_items() :
        print item.name , item.value

    print y.get_all_items()


if __name__ == '__main__':
    main()
