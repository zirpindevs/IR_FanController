import time
import serial


ser = serial.Serial("/dev/ttyACM0", baudrate=9600) #Modificar el puerto serie de ser necesario

try:
    while True:
        comando = input("Ingresar comando (on/off): ")
        comando = comando + "\n"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        time.sleep(0.5)
        read = ser.readline()
        print("read", read)
        # if read.find("Encendido"):
        #     print("ok")
        read_new = str(read)
        print("new", read_new)

        name1 = 'Python is good'
        name2 = 'Python is good'
        if name1 == name2:
            print(name1, 'is equal to', name2)


        # if(read_new.find("cendido")):
        #     print("enciende")
        # elif(read_new.find("pagado")):
        #     print("apaga")

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")
finally:
    ser.close()