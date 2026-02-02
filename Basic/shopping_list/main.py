shop_list = []

while True:
    print('1.Add item to cart ')
    print('2.modify item in cart ')
    print('3.Delete item in cart  ')
    print('4.View cart ')
    print('5.Exit')
    try :
        u_input =  int(input('Enter your choice : '))
        match u_input:
            case 1:
                item = input('Enter item name :  ')
                shop_list.append(item)
                print('item addded sucessfully...')
            case 2:
                for ind,item in enumerate(shop_list):
                    print(f'{ind + 1} : {item}')
                old_item = input('Enter item name to modify : ')
                if old_item in shop_list:
                    shop_list.insert(shop_list.index(old_item),input('enter your new item : '))
                    shop_list.remove(old_item)
                else:
                    print('Item not found')
            case 3:
                for ind,item in enumerate(shop_list):
                    print(f'{ind + 1} : {item}')
                item = input('Enter your item to delete : ')
                if item in shop_list:
                    shop_list.remove(item)
                else:
                    print('Item not found...')
            case 4:
                if not(shop_list):
                    print('items not yet added...')
                for ind,item in enumerate(shop_list):
                    print(f'{ind + 1} : {item}')
            case 5:
                print('Thank You Visit Again....')
                break
    except ValueError:
        print('Wrong input...')
        continue