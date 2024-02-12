from tkinter import *


array_2d = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
phone_book = {}


def hash(data):
    try:
        hash = ord(data[0]) % 4
        return hash
    except IndexError:
        pass


def append(array_2d, data):
    try:
        v_index = hash(data)
        state = is_full(array_2d, data)
        if state == False:
            if array_2d[v_index][(len(array_2d[v_index]) - 1)] == None:
                for index in range(len(array_2d[v_index])):
                    if array_2d[v_index][index] == None:
                        array_2d[v_index][index] = phone_book[data]
                        break
        elif state == True:
            new_array = resize(array_2d[v_index], len(array_2d[v_index] * 2))
            array_2d[v_index] = new_array
            for index in range(len(array_2d[v_index])):
                if array_2d[v_index][index] == None:
                    array_2d[v_index][index] = phone_book[data]
                    break
    except TypeError:
        pass


def search(array_2d, data):
    try:
        v_index = hash(data)
        h_index = 0
        key = phone_book.get(data)
        if key == None:
            return None
        for h_index in range(len(array_2d[v_index])):
            if key == array_2d[v_index][h_index]:
                return v_index, h_index
                break
    except IndexError and TypeError:
        pass


def resize(h_array, new_size):
    new_array = [None] * (new_size)
    for elements in range(len(h_array)):
        new_array[elements] = h_array[elements]
    return new_array


def is_full(array_2d, data):
    row = hash(data)
    if array_2d[row][(len(array_2d[row]) - 1)] != None:
        return True
    else:
        return False


######## end

def should_return_same_hash():
    expected_data = 1
    current_data = hash("Aaron2005")
    assert expected_data == current_data, f"expected: {expected_data}, but got: {current_data}"


def should_return_different_hash():
    test_data1 = hash("Aaron2005")
    test_data2 = hash("Badudu2003")
    assert test_data1 != test_data2, f"expected: {test_data1}, but got: {test_data2}"


def should_add_new_data():
    array_2d = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    name = 'Agung'
    birth = '1945'
    data = name.capitalize() + birth
    phone_number = '081319990556'
    phone_book[data] = name, birth, phone_number
    append(array_2d, data)
    expected = [[None, None, None, None], [('Agung', '1945', '081319990556'), None, None, None],
                [None, None, None, None], [None, None, None, None]]
    assert expected == array_2d, f"expected:{expected}, but got: {array_2d}"


def should_add_new_data_and_resize():
    array_2d = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345')],
                [None, None, None, None], [None, None, None, None]]
    name = 'Asep'
    birth = '2007'
    data = name.capitalize() + birth
    phone_number = '1234512345123'
    phone_book[data] = name, birth, phone_number
    append(array_2d, data)
    expected = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345'),
                                           ('Asep', '2007', '1234512345123'), None, None, None],
                [None, None, None, None], [None, None, None, None]]
    assert expected == array_2d, f"expected: {expected}, but got:{array_2d}"


def should_return_data_with_v_and_h_index():
    array_2d = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    name = 'Aaron'
    birth = '2003'
    phone_number = '081312349683'
    data = name + birth
    phone_book[data] = name, birth, phone_number
    append(array_2d, data)
    current = search(array_2d, data)
    expected = 1, 0
    assert current == expected, f"expected: {expected}, but got:{current}"


def should_not_return_data():
    array_2d = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    name = 'Aaron'
    birth = '2003'
    data = name + birth
    current = search(array_2d, data)
    expected = None
    assert current == expected, f"expected: {expected}, but got: {current}"


def should_get_new_horizontal_array_with_new_length_2times__after_insert():
    array_2d = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345')],
                [None, None, None, None], [None, None, None, None]]
    name = 'Asep'
    birth = '2007'
    data = name.capitalize() + birth
    phone_number = '1234512345123'
    phone_book[data] = name, birth, phone_number
    append(array_2d, data)
    expected = [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345'),
                ('Asep', '2007', '1234512345123'), None, None, None]
    current = array_2d[1]
    assert expected == current, f"expected: {expected}, but got:{current}"


def should_return_array_2d_with_the_same_length_like_before_after_insert():
    array_2d = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345'), None],
                [None, None, None, None], [None, None, None, None]]
    name = 'Asep'
    birth = 2007
    data = name.capitalize() + birth
    phone_number = 1234512345123
    phone_book[data] = name, birth, phone_number
    append(array_2d, data)
    expected = [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345'),
                ('Asep', '2007', '1234512345123')]
    current = array_2d[1]
    assert expected == current, f"expected: {expected}, but got:{current}"


def should_return_true_when_array_full():
    array_2d = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), ('Aciang', '1948', '081318942345')],
                [None, None, None, None], [None, None, None, None]]
    name = 'Aaron'
    birth = 2003
    data = name + birth
    current = is_full(array_2d, data)
    expected = True
    assert current == expected, f"expected: {expected}, but got:{current}"


def should_return_false_when_array_is_not_null():
    array_2d = [[None, None, None, None], [('Agung', '1945', '081319990556'), ('Agatha', '1946', '081367890887'),
                                           ('Aaron', '2003', '081312345432'), None], [None, None, None, None],
                [None, None, None, None]]
    name = 'Aaron'
    birth = 2003
    data = name + birth
    current = is_full(array_2d, data)
    expected = False
    assert current == expected, f"expected: {expected}, but got:{current}"


######

def test():
    print("Test starts")
    print("...")
    should_return_same_hash()
    should_return_different_hash()
    should_add_new_data()
    should_return_data_with_v_and_h_index()
    should_add_new_data_and_resize()
    should_not_return_data()
    should_get_new_horizontal_array_with_new_length_2times__after_insert()
    print("Test ended")


#####
def main():

        try:
            root = Tk()
            root.title('Mein Telefonbuch')
            dash = Label(root,text='-------------------')
            dash.pack()
            Title = Label(root,text="Mein Telefonbuch")
            Title.pack()
            choice = IntVar()
            Option1 = Radiobutton(root,text='1. Add new number',variable=choice,value=1)
            Option1.deselect()
            Option1.pack(anchor=W)
            Option2 = Radiobutton(root,text='2. Search by name',variable=choice,value=2)
            Option2.deselect()
            Option2.pack(anchor=W)
            Option3 = Radiobutton(root, text='Exit',variable=choice,value=3)
            Option3.deselect()
            Option3.pack(anchor=W)

            def Click(choice):
                if choice != 1 and choice != 2 and choice != 3:
                    text = 'Wrong input, please try again.'
                    warning = Label(root,text=text).pack()

                if choice == 1:
                    Add = Toplevel()
                    Add.title('Add new name')
                    loop = True
                    while (loop == True):
                        askname = Label(Add, text="Enter your name:").pack()
                        name = Entry(Add,width=30,borderwidth=5)
                        name.pack()
                        askbirth = Label(Add, text="Enter your birthdate:").pack()
                        birth = Entry(Add, width=30, borderwidth=5)
                        birth.pack()
                        def check():
                            data = name.get().capitalize() + birth.get()
                            if data in phone_book:
                                text = 'Cannot add data, Already exists'
                                msg2 = Label(Add,text=text).pack()
                            else:
                                def check2():
                                    phone_book[data] = name.get().capitalize(), str(birth.get()), str(phone.get())
                                    append(array_2d, data)
                                    Add.destroy()
                                askphone = Label(Add, text="Enter your phone number").pack()
                                phone = Entry(Add,width=30,borderwidth=5)
                                phone.pack()
                                btn2 = Button(Add, text='confirm',
                                              command=check2).pack()


                        btn1 = Button(Add,text='confirm',command=check).pack()
                        loop = False


                if choice == 2:
                    Search = Toplevel()
                    Search.title('Search by name')
                    askname = Label(Search, text="Enter your name:").pack()
                    name = Entry(Search, width=30, borderwidth=5)
                    name.pack()
                    askbirth = Label(Search, text="Enter your birthdate:").pack()
                    birth = Entry(Search, width=30, borderwidth=5)
                    birth.pack()
                    data = name.get().capitalize() + str(birth.get())

                    def Click_search():
                        name_value = name.get()
                        birth_value = birth.get()
                        data = name_value.capitalize() + str(birth_value)
                        result = search(array_2d, data)
                        
                        if result is not None:
                            v, h = result
                            Phone_num = Label(Search, text=f'Phone Number: {array_2d[v][h][2]}').pack()
                        else:
                            text = 'Phone Number: Not Found'
                            warning2 = Label(Search, text=text).pack()

                    btn3 = Button(Search,text='confirm',command=Click_search).pack()

                if choice == 3:
                    root.destroy()

            choice_button = Button(root,text='Confirm choice',command=lambda: Click(choice.get())).pack()
            dash2 = Label(root,text='-------------------')
            dash2.pack()
            root.mainloop()

        except IndexError:
            pass




if __name__ == '__main__':
    test()
    main()




