import tkinter
import tkinter.messagebox
import customtkinter
import visual
import time


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def fcfs(pname,burst,arriv,prior):

    def home():
        app1.destroy()
        import simulator


    def show_visual():
        visual.fcfs_visualization(arriv,pname,compl,wait,trnar)

    def show(n):
        global remtime,timer,get_remtime,get_status,num
        if remtime[n] > 0:
            tot = (burst[n]-remtime[n]+1)/burst[n]
            remtime[n] -= 1
            get_remtime[n].configure(state="normal")
            get_remtime[n].delete(0,5)
            get_remtime[n].insert(0,remtime[n])
            get_remtime[n].configure(state="disabled")
            get_status[n].set(tot)
            timer += 1
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            tint.after(1000,show,n)
        else:
            sim()



    def sim():
        global timer,readyq,num,n,order
        
        if len(readyq) > 0:
            qint.configure(state="normal")
            cint.configure(state="normal")
            cpu = readyq[0]
            readyq.pop(0)
            cint.delete(0,5)
            cint.insert(0,cpu)
            qint.delete(0,3*num)
            qint.insert(0,readyq)
            qint.configure(state="disabled")
            cint.configure(state="disabled")
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            show(order[n])
            n += 1
        else:
            qint.configure(state="normal")
            qint.delete(0,75)
            qint.insert(0,"EMPTY")
            qint.configure(state="disabled")
            cint.configure(state="normal")
            cint.delete(0,5)
            cint.insert(0,"IDLE")
            cint.configure(state="disabled")
            


    global num,qint,cint,timer,readyq,remtime,n,get_remtime,get_status,order
    
    num = len(pname)
    timer = 0
    n = 0

    order = []
    arv = arriv.copy()
    arv.sort()
    for i in range(num):
        order.append(arriv.index(arv[i]))


    app1 = customtkinter.CTk()
    app1.title("FIRST COME FIRST SERVE SCHEDULING")
    app1.geometry("1200x750+50+50")

    app1.grid_rowconfigure((0,1,2,3,4), weight=1)
    app1.grid_columnconfigure((0, 1,2), weight=1)

    base_frame = customtkinter.CTkFrame(master=app1)
    base_frame.grid(row=0, column=0, columnspan=3, rowspan=4, padx=10, pady=(10,5), sticky="nsew")

    lab1 = customtkinter.CTkLabel(master=base_frame,
                                    text="Process ID",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab1.place(relx=0.05, rely=0.03,anchor=customtkinter.CENTER)

    lab2 = customtkinter.CTkLabel(master=base_frame,
                                    text="Arrival Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.14, rely=0.03, anchor=customtkinter.CENTER)

    lab3 = customtkinter.CTkLabel(master=base_frame,
                                    text="Burst Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab3.place(relx=0.23, rely=0.03, anchor=customtkinter.CENTER)

    lab4 = customtkinter.CTkLabel(master=base_frame,
                                    text="Priority",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab4.place(relx=0.31, rely=0.03, anchor=customtkinter.CENTER)

    lab5 = customtkinter.CTkLabel(master=base_frame,
                                    text="Completion\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab5.place(relx=0.40, rely=0.03, anchor=customtkinter.CENTER)

    lab6 = customtkinter.CTkLabel(master=base_frame,
                                    text="Turnaround\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab6.place(relx=0.485, rely=0.03, anchor=customtkinter.CENTER)

    lab7 = customtkinter.CTkLabel(master=base_frame,
                                    text="Waiting\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab7.place(relx=0.565, rely=0.03, anchor=customtkinter.CENTER)

    lab8 = customtkinter.CTkLabel(master=base_frame,
                                    text="Status",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab8.place(relx=0.75, rely=0.03, anchor=customtkinter.CENTER)

    lab9 = customtkinter.CTkLabel(master=base_frame,
                                    text="Remaining\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab9.place(relx=0.94, rely=0.03, anchor=customtkinter.CENTER)

    top_frame = customtkinter.CTkScrollableFrame(master=base_frame)
    top_frame.pack(pady=(40,10), padx=(10,10), fill="both", expand=True)

    com = 0
    trnar = []
    wait = []
    get_status = []
    get_remtime = []
    status = []
    remtime = []
    readyq = []

    compl = [0] * num
    time = 0
    for i in range(num):
        if arriv[i] > time:
            time = arriv[i]
        compl[i] = time + burst[i]
        time = compl[i]

    for i in range(num):
        trnar.append(compl[i] - arriv[i])
        wait.append(trnar[i] - burst[i])

    for i in range(num):

        for j in range(7):

            if j%7 == 0:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=pname[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 1:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=arriv[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 2:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=burst[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 3:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=prior[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 4:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=compl[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 5:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=trnar[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 6:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=wait[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

        progressbar = customtkinter.CTkProgressBar(master=top_frame, width=300, height=5)
        progressbar.set(0)
        progressbar.grid(row=i, column=j+1, padx=(20, 20), pady=10)
        get_status.append(progressbar)
        rem = customtkinter.CTkEntry(master=top_frame,width=80)
        rem.insert(0,burst[order[i]])
        rem.grid(row=i, column=j+2, padx=10, pady=10)
        rem.configure(state="disabled")
        get_remtime.append(rem)

    for i in range(num):
        remtime.append(int(get_remtime[i].get()))
        status.append(get_status[i].get())
        readyq.append(pname[i])

    base2_frame = customtkinter.CTkFrame(master=app1,height=100)
    base2_frame.grid(row=4, column=0, columnspan=3,rowspan=1, padx=10, pady=(5,10), sticky="nsew")


    qlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Ready Queue",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    qlab.place(relx=0.08, rely=0.20,anchor=customtkinter.CENTER)

    qint = customtkinter.CTkEntry(master=base2_frame,
                                    width=500)
    qint.insert(0,readyq)
    qint.place(relx=0.35, rely=0.20, anchor=customtkinter.CENTER)

    clab = customtkinter.CTkLabel(master=base2_frame,
                                    text="CPU",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    clab.place(relx=0.63, rely=0.20, anchor=customtkinter.CENTER)

    cint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    cint.insert(0,"IDLE")
    cint.place(relx=0.70, rely=0.20, anchor=customtkinter.CENTER)

    tlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Timer",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tlab.place(relx=0.83, rely=0.20, anchor=customtkinter.CENTER)

    tint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    tint.insert(0,timer)
    tint.place(relx=0.90, rely=0.20, anchor=customtkinter.CENTER)

    at1 = "Throughput : "
    wavg = str(round((num/compl[num-1]),2))
    at1 = at1 + wavg
    
    awlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    awlab.place(relx=0.1, rely=0.48,anchor=customtkinter.CENTER)

    at1 = "Average Turnaround Time : "
    wavg = str(round((sum(trnar)/len(trnar)),2))
    at1 = at1 + wavg

    atlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    atlab.place(relx=0.15, rely=0.66,anchor=customtkinter.CENTER)

    at1 = "Average Waiting Time : "
    wavg = str(round((sum(wait)/len(wait)),2))
    at1 = at1 + wavg

    tptlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tptlab.place(relx=0.14, rely=0.85,anchor=customtkinter.CENTER)

    sim_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Simulation",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=sim)
    sim_btn.place(relx=0.66, rely=0.7, anchor=customtkinter.CENTER)

    vis_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Visualization",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=show_visual)
    vis_btn.place(relx=0.78, rely=0.7, anchor=customtkinter.CENTER)

    back_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Home",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=home)
    back_btn.place(relx=0.90, rely=0.7, anchor=customtkinter.CENTER)

    app1.mainloop() 


def sjf(pname,burst,arriv,prior):

    def home():
        app2.destroy()
        import simulator as s
        s.home()

    def show_visual():
        visual.sjf_visualization(arriv,pname,compl,wait,trnar,burst)

    def show(n):
        global remtime,timer,get_remtime,get_status,num
        if remtime[n] > 0:
            tot = (burst[order[n]]-remtime[n]+1)/burst[order[n]]
            remtime[n] -= 1
            get_remtime[n].configure(state="normal")
            get_remtime[n].delete(0,5)
            get_remtime[n].insert(0,remtime[n])
            get_remtime[n].configure(state="disabled")
            get_status[n].set(tot)
            timer += 1
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            tint.after(1000,show,n)
        else:
            sim()



    def sim():
        global timer,readyq,num,n,order
        
        if len(readyq) > 0:
            qint.configure(state="normal")
            cint.configure(state="normal")
            cpu = readyq[0]
            readyq.pop(0)
            cint.delete(0,5)
            cint.insert(0,cpu)
            qint.delete(0,3*num)
            qint.insert(0,readyq)
            qint.configure(state="disabled")
            cint.configure(state="disabled")
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            show(n)
            n += 1
        else:
            qint.configure(state="normal")
            qint.delete(0,75)
            qint.insert(0,"EMPTY")
            qint.configure(state="disabled")
            cint.configure(state="normal")
            cint.delete(0,5)
            cint.insert(0,"IDLE")
            cint.configure(state="disabled")
            


    global num,qint,cint,timer,readyq,remtime,n,get_remtime,get_status,order
    
    num = len(pname)
    timer = 0
    n = 0

    order = []
    arv = burst.copy()
    arv.sort()
    for i in range(num):
        order.append(burst.index(arv[i]))


    app2 = customtkinter.CTk()
    app2.title("SHORTEST JOB FIRST SCHEDULING")
    app2.geometry("1200x750+50+50")

    app2.grid_rowconfigure((0,1,2,3,4), weight=1)
    app2.grid_columnconfigure((0, 1,2), weight=1)

    base_frame = customtkinter.CTkFrame(master=app2)
    base_frame.grid(row=0, column=0, columnspan=3, rowspan=4, padx=10, pady=(10,5), sticky="nsew")

    lab1 = customtkinter.CTkLabel(master=base_frame,
                                    text="Process ID",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab1.place(relx=0.05, rely=0.03,anchor=customtkinter.CENTER)

    lab2 = customtkinter.CTkLabel(master=base_frame,
                                    text="Arrival Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.14, rely=0.03, anchor=customtkinter.CENTER)

    lab3 = customtkinter.CTkLabel(master=base_frame,
                                    text="Burst Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab3.place(relx=0.23, rely=0.03, anchor=customtkinter.CENTER)

    lab4 = customtkinter.CTkLabel(master=base_frame,
                                    text="Priority",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab4.place(relx=0.31, rely=0.03, anchor=customtkinter.CENTER)

    lab5 = customtkinter.CTkLabel(master=base_frame,
                                    text="Completion\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab5.place(relx=0.40, rely=0.03, anchor=customtkinter.CENTER)

    lab6 = customtkinter.CTkLabel(master=base_frame,
                                    text="Turnaround\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab6.place(relx=0.485, rely=0.03, anchor=customtkinter.CENTER)

    lab7 = customtkinter.CTkLabel(master=base_frame,
                                    text="Waiting\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab7.place(relx=0.565, rely=0.03, anchor=customtkinter.CENTER)

    lab8 = customtkinter.CTkLabel(master=base_frame,
                                    text="Status",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab8.place(relx=0.75, rely=0.03, anchor=customtkinter.CENTER)

    lab9 = customtkinter.CTkLabel(master=base_frame,
                                    text="Remaining\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab9.place(relx=0.94, rely=0.03, anchor=customtkinter.CENTER)

    top_frame = customtkinter.CTkScrollableFrame(master=base_frame)
    top_frame.pack(pady=(40,10), padx=(10,10), fill="both", expand=True)

    com = 0
    compl = []
    trnar = []
    wait = []
    get_status = []
    get_remtime = []
    status = []
    remtime = []
    readyq = []

    compl = [0] * num
    remaining_burst_time = burst.copy()
    time = 0

    while True:
        min_burst_time = float('inf')
        min_burst_time_index = -1
        for i in range(num):
            if arriv[i] <= time and remaining_burst_time[i] < min_burst_time and remaining_burst_time[i] > 0:
                min_burst_time = remaining_burst_time[i]
                min_burst_time_index = i

        if min_burst_time_index == -1:
            break

        compl[min_burst_time_index] = time + remaining_burst_time[min_burst_time_index]
        remaining_burst_time[min_burst_time_index] = 0
        time += burst[min_burst_time_index]

    for i in range(num):
        trnar.append(compl[i] - arriv[i])
        wait.append(trnar[i] - burst[i])

    for i in range(num):

        for j in range(7):

            if j%7 == 0:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=pname[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 1:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=arriv[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 2:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=burst[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 3:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=prior[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 4:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=compl[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 5:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=trnar[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 6:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=wait[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

        progressbar = customtkinter.CTkProgressBar(master=top_frame, width=300, height=5)
        progressbar.set(0)
        progressbar.grid(row=i, column=j+1, padx=(20, 20), pady=10)
        get_status.append(progressbar)
        rem = customtkinter.CTkEntry(master=top_frame,width=80)
        rem.insert(0,burst[order[i]])
        rem.grid(row=i, column=j+2, padx=10, pady=10)
        rem.configure(state="disabled")
        get_remtime.append(rem)

    for i in range(num):
        remtime.append(int(get_remtime[i].get()))
        status.append(get_status[order[i]].get())
        readyq.append(pname[order[i]])

    base2_frame = customtkinter.CTkFrame(master=app2,height=100)
    base2_frame.grid(row=4, column=0, columnspan=3,rowspan=1, padx=10, pady=(5,10), sticky="nsew")


    qlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Ready Queue",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    qlab.place(relx=0.08, rely=0.20,anchor=customtkinter.CENTER)

    qint = customtkinter.CTkEntry(master=base2_frame,
                                    width=500)
    qint.insert(0,readyq)
    qint.place(relx=0.35, rely=0.20, anchor=customtkinter.CENTER)

    clab = customtkinter.CTkLabel(master=base2_frame,
                                    text="CPU",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    clab.place(relx=0.63, rely=0.20, anchor=customtkinter.CENTER)

    cint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    cint.insert(0,"IDLE")
    cint.place(relx=0.70, rely=0.20, anchor=customtkinter.CENTER)

    tlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Timer",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tlab.place(relx=0.83, rely=0.20, anchor=customtkinter.CENTER)

    tint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    tint.insert(0,timer)
    tint.place(relx=0.90, rely=0.20, anchor=customtkinter.CENTER)

    at1 = "Throughput : "
    wavg = str(round((num/compl[num-1]),2))
    at1 = at1 + wavg
    
    awlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    awlab.place(relx=0.1, rely=0.48,anchor=customtkinter.CENTER)

    at1 = "Average Turnaround Time : "
    wavg = str(round((sum(trnar)/len(trnar)),2))
    at1 = at1 + wavg

    atlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    atlab.place(relx=0.15, rely=0.66,anchor=customtkinter.CENTER)

    at1 = "Average Waiting Time : "
    wavg = str(round((sum(wait)/len(wait)),2))
    at1 = at1 + wavg

    tptlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tptlab.place(relx=0.14, rely=0.85,anchor=customtkinter.CENTER)

    sim_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Simulation",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=sim)
    sim_btn.place(relx=0.66, rely=0.7, anchor=customtkinter.CENTER)

    vis_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Visualization",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=show_visual)
    vis_btn.place(relx=0.78, rely=0.7, anchor=customtkinter.CENTER)

    back_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Home",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=home)
    back_btn.place(relx=0.90, rely=0.7, anchor=customtkinter.CENTER)

    app2.mainloop() 


def priority(pname,burst,arriv,prior):

    def home():
        app3.destroy()
        import simulator

    def show_visual():
        visual.ps_visualization(arriv,pname,compl,wait,trnar,burst,prior)

    def show(n):
        global remtime,timer,get_remtime,get_status,num
        if remtime[n] > 0:
            tot = (burst[order[n]]-remtime[n]+1)/burst[order[n]]
            remtime[n] -= 1
            get_remtime[n].configure(state="normal")
            get_remtime[n].delete(0,5)
            get_remtime[n].insert(0,remtime[n])
            get_remtime[n].configure(state="disabled")
            get_status[n].set(tot)
            timer += 1
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            tint.after(1000,show,n)
        else:
            sim()


    def sim():
        global timer,readyq,num,n,order
        
        if len(readyq) > 0:
            qint.configure(state="normal")
            cint.configure(state="normal")
            cpu = readyq[0]
            readyq.pop(0)
            cint.delete(0,5)
            cint.insert(0,cpu)
            qint.delete(0,3*num)
            qint.insert(0,readyq)
            qint.configure(state="disabled")
            cint.configure(state="disabled")
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")
            show(n)
            n += 1
        else:
            qint.configure(state="normal")
            qint.delete(0,75)
            qint.insert(0,"EMPTY")
            qint.configure(state="disabled")
            cint.configure(state="normal")
            cint.delete(0,5)
            cint.insert(0,"IDLE")
            cint.configure(state="disabled")

    def calculate_completion_time(arrival_time, burst_time, priority):
        n = len(arrival_time)
        completion_time = [0] * n
        remaining_time = burst_time.copy()
        total_time = 0
        completed = 0

        while completed != n:
            highest_priority = float('inf')
            highest_priority_index = -1

            for i in range(n):
                if arrival_time[i] <= total_time and priority[i] < highest_priority and remaining_time[i] > 0:
                    highest_priority = priority[i]
                    highest_priority_index = i

            if highest_priority_index == -1:
                total_time += 1
                continue

            total_time += remaining_time[highest_priority_index]
            completion_time[highest_priority_index] = total_time
            remaining_time[highest_priority_index] = 0
            completed += 1

        return completion_time
            


    global num,qint,cint,timer,readyq,remtime,n,get_remtime,get_status,order
    
    num = len(pname)
    timer = 0
    n = 0

    order = []
    arv = prior.copy()
    arv.sort()
    for i in range(num):
        order.append(prior.index(arv[i]))


    app3 = customtkinter.CTk()
    app3.title("PRIORITY SCHEDULING")
    app3.geometry("1200x750+50+50")

    app3.grid_rowconfigure((0,1,2,3,4), weight=1)
    app3.grid_columnconfigure((0, 1,2), weight=1)

    base_frame = customtkinter.CTkFrame(master=app3)
    base_frame.grid(row=0, column=0, columnspan=3, rowspan=4, padx=10, pady=(10,5), sticky="nsew")

    lab1 = customtkinter.CTkLabel(master=base_frame,
                                    text="Process ID",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab1.place(relx=0.05, rely=0.03,anchor=customtkinter.CENTER)

    lab2 = customtkinter.CTkLabel(master=base_frame,
                                    text="Arrival Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.14, rely=0.03, anchor=customtkinter.CENTER)

    lab3 = customtkinter.CTkLabel(master=base_frame,
                                    text="Burst Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab3.place(relx=0.23, rely=0.03, anchor=customtkinter.CENTER)

    lab4 = customtkinter.CTkLabel(master=base_frame,
                                    text="Priority",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab4.place(relx=0.31, rely=0.03, anchor=customtkinter.CENTER)

    lab5 = customtkinter.CTkLabel(master=base_frame,
                                    text="Completion\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab5.place(relx=0.40, rely=0.03, anchor=customtkinter.CENTER)

    lab6 = customtkinter.CTkLabel(master=base_frame,
                                    text="Turnaround\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab6.place(relx=0.485, rely=0.03, anchor=customtkinter.CENTER)

    lab7 = customtkinter.CTkLabel(master=base_frame,
                                    text="Waiting\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab7.place(relx=0.565, rely=0.03, anchor=customtkinter.CENTER)

    lab8 = customtkinter.CTkLabel(master=base_frame,
                                    text="Status",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab8.place(relx=0.75, rely=0.03, anchor=customtkinter.CENTER)

    lab9 = customtkinter.CTkLabel(master=base_frame,
                                    text="Remaining\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab9.place(relx=0.94, rely=0.03, anchor=customtkinter.CENTER)

    top_frame = customtkinter.CTkScrollableFrame(master=base_frame)
    top_frame.pack(pady=(40,10), padx=(10,10), fill="both", expand=True)

    com = 0
    trnar = []
    wait = []
    get_status = []
    get_remtime = []
    status = []
    remtime = []
    readyq = []

    compl = calculate_completion_time(arriv,burst,prior)
    time = 0

    for i in range(num):
        trnar.append(compl[i] - arriv[i])
        wait.append(trnar[i] - burst[i])

    for i in range(num):

        for j in range(7):

            if j%7 == 0:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=pname[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 1:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=arriv[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 2:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=burst[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 3:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=prior[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 4:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=compl[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 5:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=trnar[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 6:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=wait[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

        progressbar = customtkinter.CTkProgressBar(master=top_frame, width=300, height=5)
        progressbar.set(0)
        progressbar.grid(row=i, column=j+1, padx=(20, 20), pady=10)
        get_status.append(progressbar)
        rem = customtkinter.CTkEntry(master=top_frame,width=80)
        rem.insert(0,burst[order[i]])
        rem.grid(row=i, column=j+2, padx=10, pady=10)
        rem.configure(state="disabled")
        get_remtime.append(rem)

    for i in range(num):
        remtime.append(int(get_remtime[i].get()))
        status.append(get_status[order[i]].get())
        readyq.append(pname[order[i]])

    base2_frame = customtkinter.CTkFrame(master=app3,height=100)
    base2_frame.grid(row=4, column=0, columnspan=3,rowspan=1, padx=10, pady=(5,10), sticky="nsew")


    qlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Ready Queue",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    qlab.place(relx=0.08, rely=0.20,anchor=customtkinter.CENTER)

    qint = customtkinter.CTkEntry(master=base2_frame,
                                    width=500)
    qint.insert(0,readyq)
    qint.place(relx=0.35, rely=0.20, anchor=customtkinter.CENTER)

    clab = customtkinter.CTkLabel(master=base2_frame,
                                    text="CPU",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    clab.place(relx=0.63, rely=0.20, anchor=customtkinter.CENTER)

    cint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    cint.insert(0,"IDLE")
    cint.place(relx=0.70, rely=0.20, anchor=customtkinter.CENTER)

    tlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Timer",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tlab.place(relx=0.83, rely=0.20, anchor=customtkinter.CENTER)

    tint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    tint.insert(0,timer)
    tint.place(relx=0.90, rely=0.20, anchor=customtkinter.CENTER)

    at1 = "Throughput : "
    wavg = str(round((num/compl[num-1]),2))
    at1 = at1 + wavg
    
    awlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    awlab.place(relx=0.1, rely=0.48,anchor=customtkinter.CENTER)

    at1 = "Average Turnaround Time : "
    wavg = str(round((sum(trnar)/len(trnar)),2))
    at1 = at1 + wavg

    atlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    atlab.place(relx=0.15, rely=0.66,anchor=customtkinter.CENTER)

    at1 = "Average Waiting Time : "
    wavg = str(round((sum(wait)/len(wait)),2))
    at1 = at1 + wavg

    tptlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tptlab.place(relx=0.14, rely=0.85,anchor=customtkinter.CENTER)

    sim_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Simulation",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=sim)
    sim_btn.place(relx=0.66, rely=0.7, anchor=customtkinter.CENTER)

    vis_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Visualization",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=show_visual)
    vis_btn.place(relx=0.78, rely=0.7, anchor=customtkinter.CENTER)

    back_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Home",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=home)
    back_btn.place(relx=0.90, rely=0.7, anchor=customtkinter.CENTER)

    app3.mainloop() 

def rrobin(pname,burst,arriv,prior,quant):

    quant = int(quant)

    def home():
        app4.destroy()
        import simulator

    def show_visual():
        visual.rr_visualization(arriv,pname,wait,trnar,burst,quant)

    def show(n):
        global num, remtime
        if n == -1:
            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")

            qint.configure(state="normal")
            cint.configure(state="normal")
            cpu = readyq[n]
            cint.delete(0,5)
            cint.insert(0,"IDLE")
            qint.delete(0,75)
            qint.insert(0,"EMPTY")
            qint.configure(state="disabled")
            cint.configure(state="disabled")

        else:

            tot = (burst[n]-remtime[n])/burst[n]
            get_remtime[n].configure(state="normal")
            get_remtime[n].delete(0,5)
            get_remtime[n].insert(0,remtime[n])
            get_remtime[n].configure(state="disabled")
            get_status[n].set(tot)

            tint.configure(state="normal")
            tint.delete(0,5)
            tint.insert(0,timer)
            tint.configure(state="disabled")

            qint.configure(state="normal")
            cint.configure(state="normal")
            cpu = readyq[n]
            newq = []
            newq = readyq.copy()
            fqu = []
            for i in range(n, num):
                fqu.append(newq[i])
            for i in range(n):
                fqu.append(newq[i])
            for i in range(num):
                if remtime[i] == 0:
                    newq[i] = '*'
            for i in range(len(fqu)):
                if fqu[i] not in newq:
                    fqu[i] = '_'
            cint.delete(0,5)
            cint.insert(0,cpu)
            qint.delete(0,3*num)
            qint.insert(0,fqu)
            qint.configure(state="disabled")
            cint.configure(state="disabled")


    def sim():
        global n, cflag, num, timer, remtime
    
        if cflag == quant:
            cflag = 0
            if n < num -1:
                n += 1
            else:
                n = 0            
        
        if remtime[n] != 0:
            remtime[n] -= 1
            timer += 1
            show(n)
            cflag += 1
            tint.after(1000,sim)
        else:
            if sum(remtime) == 0:
                show(-1)
            else:
                if n < num -1:
                    n += 1
                else:
                    n = 0
                tint.after(1000,sim)

    def calculate_completion_time(arrival_time, burst_time, time_quantum):
        n = len(arrival_time)
        remaining_burst_time = list(burst_time)
        completion_time = [0] * n
        current_time = 0
        while True:
            all_processes_completed = True
            for i in range(n):
                if remaining_burst_time[i] > 0:
                    all_processes_completed = False
                    if remaining_burst_time[i] <= time_quantum:
                        current_time += remaining_burst_time[i]
                        completion_time[i] = current_time
                        remaining_burst_time[i] = 0
                    else:
                        current_time += time_quantum
                        remaining_burst_time[i] -= time_quantum
            if all_processes_completed:
                break
        return completion_time
            


    global num,qint,cint,timer,readyq,remtime,n,get_remtime,get_status,order,cflag
    
    num = len(pname)
    timer = 0
    n = 0
    cflag = 0

    order = []
    arv = arriv.copy()
    arv.sort()
    for i in range(num):
        order.append(arriv.index(arv[i]))


    app4 = customtkinter.CTk()
    app4.title("ROUND ROBIN SCHEDULING")
    app4.geometry("1200x750+50+50")

    app4.grid_rowconfigure((0,1,2,3,4), weight=1)
    app4.grid_columnconfigure((0, 1,2), weight=1)

    base_frame = customtkinter.CTkFrame(master=app4)
    base_frame.grid(row=0, column=0, columnspan=3, rowspan=4, padx=10, pady=(10,5), sticky="nsew")

    lab1 = customtkinter.CTkLabel(master=base_frame,
                                    text="Process ID",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab1.place(relx=0.05, rely=0.03,anchor=customtkinter.CENTER)

    lab2 = customtkinter.CTkLabel(master=base_frame,
                                    text="Arrival Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab2.place(relx=0.14, rely=0.03, anchor=customtkinter.CENTER)

    lab3 = customtkinter.CTkLabel(master=base_frame,
                                    text="Burst Time",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab3.place(relx=0.23, rely=0.03, anchor=customtkinter.CENTER)

    lab4 = customtkinter.CTkLabel(master=base_frame,
                                    text="Priority",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab4.place(relx=0.31, rely=0.03, anchor=customtkinter.CENTER)

    lab5 = customtkinter.CTkLabel(master=base_frame,
                                    text="Completion\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab5.place(relx=0.40, rely=0.03, anchor=customtkinter.CENTER)

    lab6 = customtkinter.CTkLabel(master=base_frame,
                                    text="Turnaround\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab6.place(relx=0.485, rely=0.03, anchor=customtkinter.CENTER)

    lab7 = customtkinter.CTkLabel(master=base_frame,
                                    text="Waiting\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab7.place(relx=0.565, rely=0.03, anchor=customtkinter.CENTER)

    text1 = 'Status(Quantum : '+str(quant)+')'

    lab8 = customtkinter.CTkLabel(master=base_frame,
                                    text=text1,
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab8.place(relx=0.75, rely=0.03, anchor=customtkinter.CENTER)

    lab9 = customtkinter.CTkLabel(master=base_frame,
                                    text="Remaining\nTime",
                                    font=("Consolas", 13),
                                    width=120,
                                    height=22)
    lab9.place(relx=0.94, rely=0.03, anchor=customtkinter.CENTER)

    top_frame = customtkinter.CTkScrollableFrame(master=base_frame)
    top_frame.pack(pady=(40,10), padx=(10,10), fill="both", expand=True)

    com = 0
    trnar = []
    wait = []
    get_status = []
    get_remtime = []
    status = []
    remtime = []
    readyq = []

    compl = calculate_completion_time(arriv, burst, quant)
    time = 0

    for i in range(num):
        trnar.append(compl[i] - arriv[i])
        wait.append(trnar[i] - burst[i])

    for i in range(num):

        for j in range(7):

            if j%7 == 0:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=pname[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 1:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=arriv[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 2:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=burst[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 3:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=prior[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 4:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=compl[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 5:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=trnar[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

            elif j%7 == 6:
                e = customtkinter.CTkLabel(master=top_frame,
                                    text=wait[order[i]],
                                    font=("Consolas", 15),
                                    width = 80)
                e.grid(row=i, column=j, padx=10, pady=10)

        progressbar = customtkinter.CTkProgressBar(master=top_frame, width=300, height=5)
        progressbar.set(0)
        progressbar.grid(row=i, column=j+1, padx=(20, 20), pady=10)
        get_status.append(progressbar)
        rem = customtkinter.CTkEntry(master=top_frame,width=80)
        rem.insert(0,burst[order[i]])
        rem.grid(row=i, column=j+2, padx=10, pady=10)
        rem.configure(state="disabled")
        get_remtime.append(rem)

    for i in range(num):
        remtime.append(int(get_remtime[i].get()))
        status.append(get_status[order[i]].get())
        readyq.append(pname[order[i]])

    base2_frame = customtkinter.CTkFrame(master=app4,height=100)
    base2_frame.grid(row=4, column=0, columnspan=3,rowspan=1, padx=10, pady=(5,10), sticky="nsew")


    qlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Ready Queue",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    qlab.place(relx=0.08, rely=0.20,anchor=customtkinter.CENTER)

    qint = customtkinter.CTkEntry(master=base2_frame,
                                    width=500)
    qint.insert(0,readyq)
    qint.place(relx=0.35, rely=0.20, anchor=customtkinter.CENTER)

    clab = customtkinter.CTkLabel(master=base2_frame,
                                    text="CPU",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    clab.place(relx=0.63, rely=0.20, anchor=customtkinter.CENTER)

    cint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    cint.insert(0,"IDLE")
    cint.place(relx=0.70, rely=0.20, anchor=customtkinter.CENTER)

    tlab = customtkinter.CTkLabel(master=base2_frame,
                                    text="Timer",
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tlab.place(relx=0.83, rely=0.20, anchor=customtkinter.CENTER)

    tint = customtkinter.CTkEntry(master=base2_frame,
                                    width=100)
    tint.insert(0,timer)
    tint.place(relx=0.90, rely=0.20, anchor=customtkinter.CENTER)

    at1 = "Throughput : "
    wavg = str(round((num/compl[num-1]),2))
    at1 = at1 + wavg
    
    awlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    awlab.place(relx=0.1, rely=0.48,anchor=customtkinter.CENTER)

    at1 = "Average Turnaround Time : "
    wavg = str(round((sum(trnar)/len(trnar)),2))
    at1 = at1 + wavg

    atlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    atlab.place(relx=0.15, rely=0.66,anchor=customtkinter.CENTER)

    at1 = "Average Waiting Time : "
    wavg = str(round((sum(wait)/len(wait)),2))
    at1 = at1 + wavg

    tptlab = customtkinter.CTkLabel(master=base2_frame,
                                    text=at1,
                                    font=("Consolas", 18),
                                    width=120,
                                    height=22)
    tptlab.place(relx=0.14, rely=0.85,anchor=customtkinter.CENTER)

    sim_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Simulation",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=sim)
    sim_btn.place(relx=0.66, rely=0.7, anchor=customtkinter.CENTER)

    vis_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Visualization",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=show_visual)
    vis_btn.place(relx=0.78, rely=0.7, anchor=customtkinter.CENTER)

    back_btn = customtkinter.CTkButton(master=base2_frame,
                                        text="Home",
                                        width=120,
                                        height=32,
                                        border_width=0,
                                        corner_radius=4,
                                        command=home)
    back_btn.place(relx=0.90, rely=0.7, anchor=customtkinter.CENTER)

    app4.mainloop() 
