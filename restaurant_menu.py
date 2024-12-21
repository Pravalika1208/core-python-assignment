def add(menu,item):
    menu.append(item)
    return menu
def remove(menu,item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        print(f"Item '{item}' is not present in the menu")
        return menu
def check_avail(menu,item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")
menu=['rice','pasta','soups']
print("current menu:",menu)
add_item=input("add_item=")
remove_item=input("remove_item=")
check_item=input("check_item=")
menu=add(menu,add_item)
menu=remove(menu,remove_item)
check_avail(menu,check_item)
print("Updated menu:",menu)