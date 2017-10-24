class Main:
    def __init__(self):
        window = Tk()
        self.input_str = StringVar()
        self.pad = StringVar()
        self.output = StringVar()
        
        
        
        
        
        #labels
        input_label = Label(window,text = "input")
        input_label.grid(row = 0,column = 0)
        pad_label = Label(window,text = "pad")
        pad_label.grid(row = 0,column = 1)
        output_label = Label(window,text = "output")
        output_label.grid(row = 0,column = 2)        
               
        
        #entries
        input_entry = Entry(window, textvariable =  self.input_str)
        input_entry.grid(row = 1, column = 0)
        pad_entry = Entry(window, textvariable =  self.pad)
        pad_entry.grid(row = 1, column = 1)   
        output_entry = Entry(window, textvariable = self.output)
        output_entry.grid(row = 1, column = 2)        

                  
            
        encryption_button = Button(window,text = "Encrypt!", command = self.encrypt)
        decryption_button = Button(window,text = "Decrypt!", command = self.decrypt)
        
        
        encryption_button.grid(row=3, column=0, padx=20, pady=10,columnspan = 2)
        decryption_button.grid(row=3, column=1, padx=20, pady=10,columnspan = 2)    
        
        window.mainloop()
        
    def encrypt(self):
        plain_txt = self.input_str.get()
        k = open_pad(self.pad.get())
        m = string_to_decimal(plain_txt)
        c = m_to_c(m, k)
        self.output.set(decimal_to_string(c))
        
        
    def decrypt(self):
        cipher_txt = self.input_str.get()
        k = open_pad(self.pad.get())
        c = string_to_decimal(cipher_txt)
        m = c_to_m(c, k)
        self.output.set(decimal_to_string(m))        
        
        
        
Main()