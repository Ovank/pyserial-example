# Setup Information


**Environment** : *Ubuntu (Linux)*\
**Python** : *3.10.12*

I am using  ***socat*** to initiate a pair of connected serial port on the system for this Demo.


You can install this application using following command. 
```
apt-get install socat
```

## To run the Script

Open a terminal (you can use CTRL+t). USe below command to start a bidirectional data transfer link between a pair of virtual serial port(COM! and COM2)

```bash
socat -d -d pty,raw,echo=0,link=$HOME/COM1 pty,raw,echo=0,link=$HOME/COM2
```

#### Quick Explanation on command. 

    
    -d -d : To enable debug mode, to print the details from socat.

    pty: This specifies that you want to create a pseudo-terminal (pty) as the first endpoint.  

    raw: This option configures the pty in raw mode,Data is transferred as-is, byte by byte.

    echo=0: This disables local echo. When set to 0, characters you type into this pty won't be echoed back to the terminal.

    link=$HOME/COM1: This creates a symbolic link named COM1 in your home directory ($HOME) that points to the first pty. 
                      This allows you to access the virtual serial port using the COM1 name.


you can start by cloning the github repo.
```bash
    git clone https://github.com/Ovank/pyserial-example.git
```

Once you are done with cloning you can use following command.
```bash
    cd pyserial-example

    pip install virtualenv

    python -m venv venv

    source venv\bin\activate

    pip install -r requirements.txt
```

You can start the program by using following command.

```bash
    python main.py
```

## Script Run Result.
![Script Run](./asset/work.gif)


