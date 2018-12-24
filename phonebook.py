# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:21:41 2017

@author: msame
"""

import sys

phone_book_dict = {'Samir':['111','222'], 'Sarmad':['221','133'], 'Touseef':['422','155'], 'Saqib':['563','231']}

def _spaces_after_s_no(item):
    _spaces_got = ''
    _len = 5 - len(item)
    for x in range(0,_len):
        _spaces_got += ' '
    return _spaces_got

def _spaces_after_other(item):
    _spaces_got = ''
    _len = 12 - len(item)
    for x in range(0,_len):
        _spaces_got += ' '
    return _spaces_got

def _heading_spaces(item):
   _spaces_got = ''
   _len = len(item)
   _req_spaces = (20 - (int(_len/4)))
   for x in range(0,_req_spaces):
       _spaces_got += ' '
   return _spaces_got

def _view():
    print('\n\n')
    _line() 
    _view_heading = '***** CONTACTS *****'    
    print(_heading_spaces(_view_heading) , _view_heading)
    _line()   
    s_num = 1    
    if len(phone_book_dict) > 0:
        print(' S_No.', _spaces_after_s_no('  S_No.') , ' Name' , _spaces_after_other('Name') , 'Moblie' , _spaces_after_other('Moblie') , 'Mobile')
        print('', _spaces_after_s_no('') , '' , _spaces_after_other('') , '(Personal)' , _spaces_after_other('(Personal)') , '(Home/office)')
        
        _sorted = sorted(phone_book_dict)
        for _items in _sorted:
            try:
                _line()
                print(' ' , s_num , _spaces_after_s_no(str(s_num)) , _items , _spaces_after_other(_items) , _get_contact1(_items), _spaces_after_other(_get_contact1(_items)) , _get_contact2(_items))
#                print(s_num , _items)
#                print('\n  Mobile No.(Personal)   ' , _get_contact1(_items))
#                print('  Mobile No.(Home/Ofice) ' , _get_contact2(_items))                
                s_num += 1
            except:
                print(' Error in retrieving the contact..')
                _line()
    else:
        print(' Phonebook is empty..!!')
        _line()
        main()

def _get_contact1(item):
    _get_numbers = phone_book_dict[item]
    return _get_numbers[0]
#    for _values in phone_book_dict.values():        
#        con_list = _values
#        contact1 = con_list[0]
#        return contact1
        
def _get_contact2(item):
    _get_numbers = phone_book_dict[item]
    return _get_numbers[1]
#    for _values in phone_book_dict.values():
#        con_list = _values
#        contact2 = con_list[1]
#        return contact2
   
def _newname():
    _new_name = str(input('Enter name(less than 13 characters): '))
    return _new_name
    
def _add_new():
    print('\n\n')
    _line() 
    _add_heading = '***** ADD NEW CONTACT *****'
    print(_heading_spaces(_add_heading) , _add_heading)
    _line()
    _name = _newname()   
    if len(_name) < 13:
        if not _name in phone_book_dict:
            _con1 = str(input('Enter Mobile No.(Personal): '))
            _con2 = str(input('Enter Mobile No.(Home/Office): '))
            phone_book_dict[_name] = [_con1,_con2]
            print(' Contact added successfully..!')
        else:
            print(' Contact already exists..!')
            print(' Please try another name..!')
            _line()
            _add_new()
    else:
        print('Exceeded name length..!')
        print('Use length less than 13 characters..!')
        _add_new()
    

def _delete_else_choice():
    _del_else_choice = str(input('Delete any other contact(y / n)? :  '))
    _line()
    if _del_else_choice == 'y' or _del_else_choice == 'Y':
        _delete()
    elif _del_else_choice == 'n' or _del_else_choice == 'N':
        main()
    else:
        print(' Invalid option..!!')
        _delete_choice()
            

def _delete_choice(_contact, _warn):
    if _warn == 1:
        _del_choice = str(input('Do you want to delete this(y / n)? :  '))
        if _del_choice == 'y' or _del_choice == 'Y':
            _line()
            print(' Deleting...')
            del phone_book_dict[_contact]
            print(' Number deleted successfully..!')
            _line()
            _continue()        
        elif _del_choice == 'n' or _del_choice == 'N':
            _line()
            _delete_else_choice()
        else:
            print(' Invalid option..!!')
            _delete_choice()
    else:        
        del phone_book_dict[_contact]
        
def _delete():
    print('\n\n')
    _line()
    _delete_heading = '***** DELETE CONTACT *****'
    print(_heading_spaces(_delete_heading) , _delete_heading)
    _line()
    _name = str(input('Name of the contact to be deleted: '))
    _line()
    if _name in phone_book_dict:
        print(' Delete the below contact...!')
        _line()
        print(' ' , 'Name' , _spaces_after_other('Name') , 'Moblie' , _spaces_after_other('Moblie') , 'Mobile')
        print( '' , _spaces_after_other('') , '(Personal)' , _spaces_after_other('(Personal)') , '(Home/Office)')
        _line()
        print(' ' , _name , _spaces_after_other(_name) , _get_contact1(_name), _spaces_after_other(_get_contact1(_name)) , _get_contact2(_name))
        _line()
        _delete_choice(_name,1)
        
    else:
        print(' Invalid name entered..!')
        _retry = input('Try again to delete any contact? (y / n): ')
        if _retry == 'y' or _retry == 'Y':
            _line()
            _delete()
        elif _retry == 'n' or _retry == 'N':            
            _line()
            main()
        else:
            print(' Invalid option..!')
            _line()

def _retryy():
    _retry = input('Search again? (y / n): ')
    if _retry == 'y' or _retry == 'Y':
        _line()
        _search()
    elif _retry == 'n' or _retry == 'N':            
        _line()
        main()
    else:
        print(' Invalid option..!')
        _line()
        _retryy()
 
def _search():
    print('\n\n')
    _line()
    _search_heading = '***** SEARCH CONTACT *****' 
    print(_heading_spaces(_search_heading) , _search_heading)
    _line()
    _name = str(input('Enter Name(Case_Sensitive): '))
    _line()
    
    if _name in phone_book_dict:
       #  _search_found = phone_book_dict[_name]
       print(' Contact found..!')
       _line()
       print(' ' , 'Name' , _spaces_after_other('Name') , 'Moblie' , _spaces_after_other('Moblie') , 'Mobile')
       print( '' , _spaces_after_other('') , '(Personal)' , _spaces_after_other('(Personal)') , '(Home/Office)')
       _line()
       print(' ' , _name , _spaces_after_other(_name) , _get_contact1(_name), _spaces_after_other(_get_contact1(_name)) , _get_contact2(_name))
       _line()
       print(' Search complete..!!')
       
    else:
        print(' No contact found..!');
        _line()
        _retryy()

def _set_newname(old_name):
    _old_name = old_name
    _new_name = str(input('Enter new name: '))
    _line()
    _contact1 = _get_contact1(_old_name)
    _contact2 = _get_contact2(_old_name)
    if len(_new_name) < 13:
        if not _new_name in phone_book_dict:
            phone_book_dict[_new_name] = [_contact1,_contact2]
            print(' Contact updated successfully..!')
            _delete_choice(_old_name, 0)
        else:
            print(' Name already exists..!')
            print(' Please try another name..!')
            _line()
            _set_newname(_old_name)
    else:
        print('Exceeded name length..!')
        print('Use length less than 13 characters..!')
        _set_newname(_old_name)

def _change_cont_name():
    _old_name = str(input('Enter old name(case_sensitive): '))
    _line()
    if _old_name in phone_book_dict:        
        _set_newname(_old_name)
        _line()
    else:
        print('Invalid name entered..!')
        print('Try again..!')
        _line()
        _change_cont_name()
    _update()

def _set_new_mob_personal(name):
    _name = name
    _get_contact2(_name)
    _new_mob = str(input('Enter new mobile no.: '))
    _line()
    phone_book_dict[_name] = [_new_mob,_get_contact2(_name)]
    print(' Contact updated successfully..!')
    

def _change_mob_personal():
    _name = str(input('Name(Case_Sensitive): '))
    _line()
    if _name in phone_book_dict:        
        _set_new_mob_personal(_name)
        _line()
    else:
        print('Invalid name entered..!')
        print('Try again..!')
        _line()
        _change_mob_personal()
    _update()

def _set_new_mob_home(name):
    _name = name
    _get_contact1(_name)
    _new_mob = str(input('Enter new mobile no.: '))
    _line()
    phone_book_dict[_name] = [_get_contact1(_name),_new_mob]
    print(' Contact updated successfully..!')

def _change_mob_home():
    _name = str(input('Name(Case_Sensitive): '))
    _line()
    if _name in phone_book_dict:        
        _set_new_mob_home(_name)
        _line()
    else:
        print('Invalid name entered..!')
        print('Try again..!')
        _line()
        _change_mob_home()
    _update()
 
def _update_choice():
    _update_choice = ''
    _update_choice = input('Your option is? (1-4): ')
    _update_valid_choices = ['1','2','3','4']
    _line()
    def _update_choice_validity():      
        if _update_choice == '1':
            _change_cont_name()
        elif _update_choice == '2':
            _change_mob_personal()
        elif _update_choice == '3':
            _change_mob_home()
        elif _update_choice == '4':
            main()
           
    if _update_choice in _update_valid_choices:
        _update_choice_validity()
    else:
         print('Invalid option..!')
         _update_choice()
    
def _update():
    print('\n\n')
    _line()
    _modify_heading = '***** UPDATE CONTACT *****'
    print(_heading_spaces(_modify_heading) , _modify_heading)
    _line()
    _update_options = """UPDATE OPTIONS:
        1. Change Contact Name
        2. Change Mobile No.(Personal)
        3. Change Mobile No.(Home/Office)
        4. Back to home"""
    print(_update_options)
    _line()
    _update_choice()

def _continue():
    continue_choice = input('Back to home? (y / n): ') 
    _line()
    # (y --> Yes) and (n --> No )
    if continue_choice == 'y' or continue_choice == 'Y':
        main()        
    elif continue_choice == 'n' or continue_choice == 'N':
        _exit()
    else:
        print(' Invalid option..!!')
        _continue()

def _exit():
    print('\n\n')
    _line()
    _exit_heading = '***** EXIT *****'
    print(_heading_spaces(_exit_heading) , _exit_heading)
    _line()
    exit_choice = input('Exit? (y / n): ')
    _line()
    # (y --> Yes) and (n --> No )
    
    
    if exit_choice == 'y' or exit_choice == 'Y':
        try:
            sys.exit()
        except:
            print(' Program Exited Successfully..!')
            _line()
    elif exit_choice == 'n' or exit_choice == 'N':
        main()
    else:
        print(' Invalid option..!')
        _line()
        _exit()

def _invalid():
    print(' Invalid Option..!')
    print(' Try again..!')
    _line()
    main()

def _line():
    print('-----------------------------------------------------')
    
def main():
    _main_heading = '***** PHONEBOOK *****'
    options = """ OPTIONS:
        1. VIEW CONTACTS
        2. ADD NEW
        3. DELETE
        4. SEARCH
        5. UPDATE
        6. EXIT"""
    print('\n\n')
    _line()
    print(_heading_spaces(_main_heading) , _main_heading)
    _line()
    print(options)
    _line()
    try:
        
        choice = int(input('Choose your option(1-6): '))  
        _line()
        if choice == 1:                     
            _view()
            _line()
            _continue()
    
        elif choice == 2:                    
            _add_new()
            _line()
            _continue()
    
        elif choice == 3:                    
            _delete()
            _line()
            _continue()
    
        elif choice == 4:                   
            _search()
            _line()
            _continue()
        
        elif choice == 5:
            _update()
    
        elif choice == 6:
            _exit()
            
        else:
            _invalid()
            _line()
    except:
        _invalid()
        

# CALL TO THE MAIN PROGRAM      
main()