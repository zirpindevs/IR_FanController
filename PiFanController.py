import time
import serial


ser = serial.Serial("/dev/ttyACM0", baudrate=9600) #Modificar el puerto serie de ser necesario


# function to compare string
# based on the number of digits
def compare_strings(str1, str2):
    count1 = 0
    count2 = 0

    for i in range(len(str1)):
        if str1[i] >= "0" and str1[i] <= "9":
            count1 += 1

    for i in range(len(str2)):
        if str2[i] >= "0" and str2[i] <= "9":
            count2 += 1

    return count1 == count2

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

        print(compare_strings("read_new", "Encendido"))
        print(compare_strings("read_new", "Apagado"))



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