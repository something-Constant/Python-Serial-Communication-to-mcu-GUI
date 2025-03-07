from customtkinter import *
from serial import *


class App():

    def __init__(self):
        self.root = CTk()
        self.root.geometry("600x500")
        self.root.title("Serial Controller")

        self.OffColor = "Red"
        self.OnColor = "Green"

        self.Button_Relay1 = CTkButton(self.root,
                                       command=self.button_Relay1,
                                       text="Relay 1",
                                       fg_color=self.OffColor,
                                       hover_color=self.OffColor)

        # self.Button_Relay1.grid(row=0, column=1, padx=20, pady=10)
        self.Button_Relay1.place(relx=0, rely=0.1)

        self.Button_Relay2 = CTkButton(self.root,
                                       command=self.button_Relay2,
                                       text="Relay 2",
                                       fg_color=self.OffColor,
                                       hover_color=self.OffColor)

        self.Button_Relay2.grid(row=1, column=1, padx=20, pady=10)

        self.Button_Voltage = CTkButton(self.root,
                                        command=self.Button_Voltage,
                                        text="Voltage",
                                        fg_color=self.OnColor,
                                        hover_color=self.OffColor)

        self.Button_Voltage.grid(row=2, column=1, padx=20, pady=10)

        self.Lable_Voltage = CTkLabel(self.root,
                                      text="N/A",
                                      bg_color="White",
                                      text_color="Black",
                                      height=25,
                                      width=75)
        self.Lable_Voltage.grid(row=2, column=0, padx=20, pady=10)

        self.Button_Temp = CTkButton(self.root,
                                     command=self.Button_Temp,
                                     text="Tempereture",
                                     fg_color=self.OnColor,
                                     hover_color=self.OffColor)

        self.Button_Temp.grid(row=3, column=1, padx=20, pady=10)

        self.Lable_Temp = CTkLabel(self.root,
                                   text="N/A",
                                   bg_color="White",
                                   text_color="Black",
                                   font=("Gentona", 22))
        self.Lable_Temp.grid(row=3, column=0, padx=20, pady=10)

        self.Relay1_State: int = 0
        self.Relay2_State: int = 0

        self.root.mainloop()

    def button_Relay1(self):
        try:
            if (self.Relay1_State == 0):
                Port = Serial("COM7", 115200, timeout=0.1)
                if (Port.readable()):
                    with Port as ST:
                        ST.write("\n".encode())
                        ST.read(500)

                        ST.write("Relay1 ON\n".encode())

                    self.Button_Relay1.configure(fg_color=self.OnColor,
                                                 hover_color=self.OnColor)

            elif (self.Relay1_State == 1):
                Port = Serial("COM7", 115200, timeout=0.1)
                if (Port.readable()):
                    with Port as ST:
                        ST.write("\n".encode())
                        ST.read(500)

                        ST.write("Relay1 OFF\n".encode())

                    self.Button_Relay1.configure(fg_color=self.OffColor,
                                                 hover_color=self.OffColor)

            self.Relay1_State ^= 1

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def button_Relay2(self):
        try:
            if (self.Relay2_State == 0):
                Port = Serial("COM7", 115200, timeout=0.1)
                if (Port.readable()):
                    with Port as ST:
                        ST.write("\n".encode())
                        ST.read(500)

                        ST.write("Relay2 ON\n".encode())

                    self.Button_Relay2.configure(fg_color=self.OnColor,
                                                 hover_color=self.OnColor)

            elif (self.Relay2_State == 1):
                Port = Serial("COM7", 115200, timeout=0.1)
                if (Port.readable()):
                    with Port as ST:
                        ST.write("\n".encode())
                        ST.read(500)

                        ST.write("Relay2 OFF\n".encode())

                self.Button_Relay2.configure(fg_color=self.OffColor,
                                             hover_color=self.OffColor)

            self.Relay2_State ^= 1

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def Button_Voltage(self):
        try:
            Port = Serial("COM7", 115200, timeout=0.1)
            if (Port.readable()):
                with Port as ST:
                    ST.write("\n".encode())
                    ST.read(500)

                    ST.write("Voltage\n".encode())
                    data = ST.read_until(b"\r").decode()
                    data = data.strip()
                    data = data.split('=')
                    print(data[1])

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def Button_Temp(self):
        try:
            Port = Serial("COM7", 115200, timeout=0.1)
            if (Port.readable()):
                with Port as ST:
                    ST.write("\n".encode())
                    ST.read(500)

                    ST.write("Temperature\n".encode())
                    data = ST.read_until(b"\r").decode()
                    data = data.strip()
                    data = data.split('=')
                    print(data[1])
                    self.Lable_Temp.configure(text=data[1])

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")


def main():

    # app = App()

    Window = CTk()
    Window.geometry("600x500")
    Window.title("Serial Controller")

    Button_Relay1 = CTkButton(Window, text="Relay 1")
    Button_Relay1.place(relx=0.5,
                        rely=0.2,
                        anchor="center",
                        relwidth=0.3,
                        relheight=0.09)

    Button_Relay2 = CTkButton(Window, text="Relay 2")
    Button_Relay2.place(relx=0.5,
                        rely=0.3,
                        anchor="center",
                        relwidth=0.3,
                        relheight=0.09)

    Button_Voltage = CTkButton(Window, text="Voltage: N/A")
    Button_Voltage.place(relx=0.5,
                         rely=0.5,
                         anchor="center",
                         relwidth=0.3,
                         relheight=0.09)

    Button_Temp = CTkButton(Window, text="Tempereture: N/A")
    Button_Temp.place(relx=0.5,
                      rely=0.6,
                      anchor="center",
                      relwidth=0.3,
                      relheight=0.09)

    # Lable_Voltage = CTkLabel(Window, text="N/A", height=25, width=75)
    # Lable_Voltage.place(relx= 0.0, rely=0.3)

    # Lable_Temp = CTkLabel(Window, text="N/A", font=("Gentona", 22))
    # Lable_Temp.place(relx= 0.0, rely=0.5)

    Window.mainloop()


if __name__ == "__main__":
    main()
