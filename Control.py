from customtkinter import *
from serial import *
import json


class Window():

    def __init__(self):
        self.root = CTk()
        self.root.geometry("600x500")
        self.root.title("Serial Controller")
        
        self.Flag = 0

        self.OffColor = "#C21807"
        self.OnColor = "Green"

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=2)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=2)
        self.root.rowconfigure(4, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=1)

        self.Relay1_State: int = 0
        self.Relay2_State: int = 0
        self.Voltage = "N/A"
        self.Temperature = "N/A"
        
        
        try: 
            self.Port = Serial("COM7", 115200, timeout=0.1)
            
            if not(self.Port.readable()):
                self.Port.open()
    
            if self.Flag == 0:
                if (self.Port.readable()):
                    self.Port.write("\n".encode())
                    self.Port.read(500)
        
                    self.Port.write("Status\n".encode())
                    data = self.Port.read_until(b"\r").decode()
        
                    with open("data.json", 'w') as Json:
                        Json.write(data)
        
                with open("data.json", 'r') as Json:
                    data = json.loads(Json.read())
                
                if data:
                    self.Relay1_State = data["Relay 1"]
                    self.Relay2_State = data["Relay 2"]
                    self.Voltage = data["Voltage"]
                    self.Temperature = data["Temperature"]
                    
                self.Flag = 1
                
        except SerialException:
            print("could not open port 'COM7'")

        except ValueError as Error:
            print("Code has Error!")
            print(Error)
            
        FrameControl = CTkFrame(self.root, corner_radius=15)
        FrameControl.grid(row=1, column=1, sticky="nsew")
        
        
        
        self.Button_Relay1 = CTkButton(FrameControl,
                                       text="Relay 1",
                                       corner_radius=60,
                                       fg_color= self.OffColor if not self.Relay1_State else self.OnColor,
                                       hover_color=self.OnColor if not self.Relay1_State else self.OffColor,
                                       command=self.button_Relay1)

        self.Button_Relay1.place(relx=0.5,
                                 rely=0.25,
                                 anchor="center",
                                 relheight=0.3,
                                 relwidth=0.5)

        self.Button_Relay2 = CTkButton(FrameControl,
                                       text="Relay 2",
                                       corner_radius=60,
                                       fg_color= self.OffColor if not self.Relay2_State else self.OnColor,
                                       hover_color=self.OnColor if not self.Relay2_State else self.OffColor,
                                       command=self.button_Relay2)

        self.Button_Relay2.place(relx=0.5,
                                 rely=0.65,
                                 anchor="center",
                                 relheight=0.3,
                                 relwidth=0.5)

        FrameData = CTkFrame(self.root, corner_radius=15)
        FrameData.grid(row=3, column=1, sticky="nsew")

        self.VotageText = "Voltage: "
        self.Button_Voltage = CTkButton(FrameData,
                                        text=self.VotageText + str(self.Voltage),
                                        corner_radius=60,
                                        command=self.Button_Voltage,
                                        fg_color="#00002A",
                                        hover_color="#000038")

        self.Button_Voltage.place(relx=0.5,
                                  rely=0.25,
                                  anchor="center",
                                  relheight=0.3,
                                  relwidth=0.5)

        self.TemperetureText = "Tempereture: "
        self.Button_Temp = CTkButton(FrameData,
                                     text=self.TemperetureText + str(self.Temperature),
                                     corner_radius=60,
                                     command=self.Button_Temp,
                                     fg_color="#00002A",
                                     hover_color="#000038")

        self.Button_Temp.place(relx=0.5,
                               rely=0.65,
                               anchor="center",
                               relheight=0.3,
                               relwidth=0.5)

        self.root.mainloop()

    def button_Relay1(self):
        try:
            if (self.Relay1_State == 0):
                if (self.Port.readable()):

                    self.Port.write("\n".encode())
                    self.Port.read(500)

                    self.Port.write("Relay1 ON\n".encode())

                    self.Button_Relay1.configure(fg_color=self.OnColor,
                                                 hover_color=self.OffColor)

                    self.Relay1_State ^= 1

            elif (self.Relay1_State == 1):
                if (self.Port.readable()):
                    self.Port.write("\n".encode())
                    self.Port.read(500)

                    self.Port.write("Relay1 OFF\n".encode())

                    self.Button_Relay1.configure(fg_color=self.OffColor,
                                                 hover_color=self.OnColor)

                    self.Relay1_State ^= 1

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def button_Relay2(self):
        try:
            if (self.Relay2_State == 0):
                if (self.Port.readable()):
                    self.Port.write("\n".encode())
                    self.Port.read(500)

                    self.Port.write("Relay2 ON\n".encode())

                    self.Button_Relay2.configure(fg_color=self.OnColor,
                                                 hover_color=self.OffColor)
                    self.Relay2_State ^= 1

            elif (self.Relay2_State == 1):
                if (self.Port.readable()):
                    self.Port.write("\n".encode())
                    self.Port.read(500)

                    self.Port.write("Relay2 OFF\n".encode())

                    self.Button_Relay2.configure(fg_color=self.OffColor,
                                                 hover_color=self.OnColor)

                    self.Relay2_State ^= 1

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def Button_Voltage(self):
        try:
            if self.Flag:
                if (self.Port.readable()):
                    self.Port.write("\n".encode())
                    self.Port.read(500)
    
                    self.Port.write("Voltage\n".encode())
                    data = self.Port.read_until(b"\r").decode()
                    data = data.strip()
                    data = data.split('=')
    
                    self.Button_Voltage.configure(text=self.VotageText + data[1] +
                                                  "V")

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")

    def Button_Temp(self):
        try:
            if self.Flag:
                if (self.Port.readable()):
    
                    self.Port.write("\n".encode())
                    self.Port.read(500)
    
                    self.Port.write("Temperature\n".encode())
                    data = self.Port.read_until(b"\r").decode()
                    data = data.strip()
                    data = data.split('=')
                    self.Button_Temp.configure(text=self.TemperetureText +
                                               data[1] + "℃")

        except SerialException:
            print("could not open port 'COM7'")

        except:
            print("Code has Error!")


def main():

    APP = Window()


if __name__ == "__main__":
    main()
