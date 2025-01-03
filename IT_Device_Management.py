import sqlite3
import os
import art
#add logging
#add database integration
#add authenction
#add UI (maybe)

class Device_DB:
    def __init__(self):
        self.conn = sqlite3.connect("it_device.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS devices(
                                brand TEXT, serial_number TEXT,model TEXT,
                                CPU TEXT, RAM TEXT, hard_drive TEXT, PRIMARY KEY(brand,serial_number)''')
        
class Equipment:
    def __init__(self,brand,model,serial_number):

        self.__brand = brand
        self.__model = model
        self.__serial_number = serial_number 

    def get_maker(self):
        return self.__brand


    def set_maker(self,brand):
        self.__brand = brand


    def get_model(self):
        return self.__model

    def set_model(self,model):
        self.__model = model

    def get_serial_number(self):
        return self.__serial_number

    def set_serial_number(self,serial_number):
        self.__serial_number = serial_number

class Computer(Equipment):
    def __init__(self,brand,model,serial_number,CPU,RAM,hard_drive):
        super().__init__(brand,model,serial_number)
        self.__CPU = CPU
        self.__RAM = RAM
        self.__hard_drive = hard_drive

    def get_CPU(self):
        return self.__CPU

    def set_CPU(self,CPU):
        self.__CPU = CPU

    def get_RAM(self):
        return self.__RAM

    def set_RAM(self,RAM):
        self.__RAM = RAM

    def get_hard_drive(self):
        return self.__hard_drive

    def set_hard_drive(self,hard_drive):
        self.__hard_drive = hard_drive

    def item_summary(self):
        return {
            "Brand": self.get_maker(),
            "Model": self.get_model(),
            "Serial Num": self.get_serial_number(),
            "CPU": self.get_CPU(),
            "RAM": self.get_RAM(),
            "Hard Drive": self.get_hard_drive()
            
            }
    def __str__(self):
        return f'CPU: {self.get_CPU()}, RAM: {self.get_RAM()}'



class Network(Equipment):

    def __init__(self,brand,model,serial_number,ip_address):
        super().__init__(brand,model,serial_number)
        self.__ip_address = ip_address

    def get_IP_ADDRESS(self):
        return self.__ip_address

    def set_IP_ADDRESS(self,ip_address):
        self.__ip_address = ip_address


def computer_device_information():
    try:
        comp_brand=  input("Enter the brand of the computer: ")
        model_type=  input("Enter the specific model of the computer: ")
        serial_number=  int(input("SERIAL NUMBER: "))
        RAM_Amount=  float(input("Enter the amount of RAM it has: "))
        CPU_spec=  input("Enter the CPU name: ")
        driver_spec=  input("Name of hard drive: ")
        
    except TypeError as e:
        print("incorrect type")


    computer_info = Computer(comp_brand,model_type,serial_number,RAM_Amount,CPU_spec,driver_spec)

    print("Device added")
    #print(computer_info.item_summary())
    print(computer_info)




def network_device_information():
    try:
        network_brand = input("Enter the brand of the net device: ")
        model_net = input("Enter the model name of the net device: ")
        serial_net = input("Enter the serial number of the device: ")
        Ip = int(input("Enter Ip address info: "))
    except TypeError as e:
        print("Need another input")
    
    network_device = Network(network_brand,model_net,serial_net,IP)


def text_menu():
    print("IT Device Managment")
    print("Select an option")
    print("1.Add a computer device")
    print("2.Add a networking device")
    print("3.Changes & Logs")
    print("4.Item Lookup")
    print("5.Exit")
    IT_selection = int(input("enter a selection"))
    return IT_selection


def main():
    IT_selection =text_menu()
    if IT_selection == 1:
        computer_device_information()
    elif IT_selection == 2:
        network_device_information()
    elif IT_selection == 5:
        exit()
main()        
