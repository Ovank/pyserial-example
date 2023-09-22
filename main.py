"""
    File         :   main.py
    Description  :   This Python program creates two virtual serial ports and uses two threads 
                     to write to and read from the ports simultaneously. The writer thread writes a formatted
                     text to the first port, while the reader thread reads the data from the second port and prints
                     it to the console. The program uses the multiprocessing module to create the two threads 
                     and manage them
    Author       :   Om Vats.
    Date         :   September 23, 2023.
"""


import os,serial,time,multiprocessing

SLEEPTIME = 0.2

WRITE_PORT = os.environ.get('HOME') + "/COM1"

READ_PORT = os.environ.get('HOME') + "/COM2"

class Scaner():
    '''
        Scan for open serial.
    '''

    def __init__(self) :

        pass

    def __scan_for_virtualPort():
        '''
            Check if any virtual serial port is present.
        '''
        #This contain all the usable/available serial ports.
        com_port_list= []

        #Note :- I tried to use python -m serial.tools.list_ports from pyserial
        #module, but this does not work in Ubuntu/Linux environment.
        #So, i used a adhoc solution, just to scan for specific type of serial
        #port by using format-able port file path, and using Serial to connect and
        #validated it, if present i append to the available 
        for port_number in range(256):
            
            try:
                
                #Try to connect to the serial port. If exist no error and 
                #pushed to available list of port.
                serial.Serial(f"/dev/pts/{i}")
                
                com_ports.append(f"/dev/pts/{i}")

            except serial.SerialException:
                
                pass

        return com_ports
    
    def scan(self) :

        return self.__scan_for_virtualPort

class Writer():
    '''
        Writer class
    '''

    def __init__(self,Port : str) :

        #This is the port our program will be writing data to.
        #port is the path to the port file created by socat tool.
        self.port = Port    
    
    def write_tovirtualPort(self) :
        ''''
            Write to a virtual port
        '''
        #Open a connection to provided Write port.
        write_port = serial.Serial(port=self.port)

        print(f"Writing to Virtual Serial Port : {write_port.name}")

        #A flag to see the recent data counter.
        count =0

        #Formatted text that is going to be written to the write port.
        writer_text = f"{count + 1 }. I am writing to Port {write_port.name}.Hello World !\n"

        #This is a infinite loop which continue to write formatted text to the write port.
        while True : 

            #Writing each character at a time with sleep time, to appear as a typing effect.
            #This is for the fun, complete block of text can be written at a time.
            for word in writer_text :

                #Only byte type data can be written, so using encode to convert to byte type data.
                write_port.write(word.encode('utf-8'))

                #Flushing the content from the port so that repeated data does not appears.
                write_port.flush()

                #After writing to the port, sleep for predefined time.
                time.sleep(SLEEPTIME)
            #increasing the flag counter.
            count +=1

            #Updating the write text block.
            writer_text = f"{count + 1}. I am writing to Port {write_port.name}.Hello World !\n"

class Reader():
    '''
        Reader Class.
    '''
    def __init__(self,Port):

        #This is the port our program will be reading data from.
        #port is the path to the port file created by socat tool.
        self.port = Port

    def read_fromvirtualPort(self) :
        '''
            Read data from virtual port.
        '''

        #Open a connection to provided Read port.
        read_port = serial.Serial(port=self.port)

        print(f"Reading from Virtual Serial Port : {read_port.name}")

        #This is a infinite loop which continue to read byte data from the port.
        while True : 

            #This is a function call to read 1 byte of data or 1 character at a time.
            data = read_port.read(size=1)

            #This prints the read data to stander output, to the terminal.
            print(data.decode('utf-8'),end='',flush=True)


def main():

    #Initiate a writer class object.
    writer = Writer(WRITE_PORT)

    #Initiate a reader class object.
    reader = Reader(READ_PORT)

    #Initiate Reader Thread process.
    read_thread = multiprocessing.Process(target=reader.read_fromvirtualPort)
    
    #Initiate Writer thread process.
    write_thread = multiprocessing.Process(target=writer.write_tovirtualPort)
    

    # Start the threads
    write_thread.start()

    read_thread.start()
    
    # Wait for the two thread to finish
    write_thread.join()
    read_thread.join()


if __name__ == "__main__":

    main()
