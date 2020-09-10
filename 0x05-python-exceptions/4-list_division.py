#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except ValueError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except:
            pass
        finally:
            if new_list[i] == None:
                new_list[i] = 0
            else:
                new_list[i] = float(new_list[i])
    return new_list
