import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import  tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
root=tk.Tk()

canvas=tk.Canvas(root, height=700, width=800)
canvas.pack()

bi=tk.PhotoImage(file='suresync-suite-background.png')
bl=tk.Label(root, image=bi)
bl.place(relheight=1, relwidth=1)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0, rely=0, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0.8, rely=0, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0.8, rely=0.8, relheight=0.2, relwidth=0.2)



def Run():
      button_text.set("Data_Extraction....")
      x="Program Ran Successfully \nExtracted data downloaded to root folder\nAll Charts Loaded \nThank You."
     
      import API_Module
      API_Module.data_extraction()
      df=API_Module.df
      df.to_csv('data.csv')
      button_text.set("Charts_Loading........")
      import data_cleaning_module
      data_cleaning_module.data_cleaning(df)
      df_viz=data_cleaning_module.df_clean
      
      import visualization_module
      visualization_module.plot_charts(df_viz)
      button_text.set("Run") 
        
      text_box=tk.Text(frame, height=1, width=10, padx=15, pady=15 )
      text_box.insert(1.0, x)
      text_box.place(relx=0.1, rely=0.7, relheight=0.3, relwidth=0.8)

frame=tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

Label=tk.Label(frame, text="This Software Scrapes Stop&Search data_set via API and Return Charts. \n \n Click the Run button below to run the Program and \
await the Charts; Charts will open in a new window\
 \n(CLOSE EACH CHART TO OPEN THE NEXT).\n \n ENSURE YOU ARE CONNECTED TO INTERNET FACILITY\nIT MIGHT TAKE UP TO 30 MINUTES BEFORE CHARTS COMES UP, KINDLY WAIT", bg='gray')
Label.place(relx=0.1, rely=0.2, relheight=0.3, relwidth=0.8)

button_text=tk.StringVar()
button=tk.Button(frame, textvariable=button_text, bg='gray', command=lambda: Run())
button_text.set("Run")
button.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.2)

root.mainloop()





