from tkinter import *
import datetime
import urllib.request
import json
req = urllib.request.Request(
    url=
    'https://api.spacexdata.com/v4/launches/next'
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    launchtimeunix = data['date_unix']
    timestamp = datetime.datetime.fromtimestamp(launchtimeunix)
    launchtime = timestamp.strftime('%Y-%m-%d / %H:%M:%S  (Y-M-D H-M-S)')
    details = data['details']
    media = data['links']
    stream = media['webcast']
    missionname = data['name']
    flightid = data['id']
    fnum = data['flight_number']

requ = urllib.request.Request(
    url=
    'https://api.spacexdata.com/v4/launches/upcoming'
)

with urllib.request.urlopen(requ) as respp:
    apistuff = json.loads(respp.read().decode("utf-8"))
    dataa = apistuff[1]
    slaunchtimeunix = dataa['date_unix']
    stimestamp = datetime.datetime.fromtimestamp(slaunchtimeunix)
    slaunchtime = stimestamp.strftime('%Y-%m-%d / %H:%M:%S  (Y-M-D H-M-S)')
    sdetails = dataa['details']
    smedia = dataa['links']
    sstream = smedia['webcast']
    smissionname = dataa['name']
    sflightid = dataa['id']
    sfnum = dataa['flight_number']

		
def gotopg2():
    window.title(f"SpaceX Departure Board ({smissionname})")
    name.pack_forget()
    departure.pack_forget()
    pg1button.pack_forget()
    link.pack_forget()
    fid.pack_forget()
    names.pack()
    departures.pack()
    links.pack()
    fids.pack()
    pg2button.pack()
def gotopg1():
    window.title(f"SpaceX Departure Board ({missionname})")
    names.pack_forget()
    departures.pack_forget()
    links.pack_forget()
    fids.pack_forget()
    pg2button.pack_forget()
    name.pack()
    departure.pack()
    link.pack()
    fid.pack()
    pg1button.pack()
        
window = Tk()
window.title(f"SpaceX Departure Board ({missionname})")
window.geometry("375x125")

names = Label(window, text=f'Mission Name: {smissionname}')
name = Label(window, text=f'Mission Name: {missionname}')
name.pack()

departures = Label(window, text=f'Departure Time (UTC): {slaunchtime}')
departure = Label(window, text=f'Departure Time (UTC): {launchtime}')
departure.pack()

links = Label(window, text=f'Link to Live Launch: {sstream}')
link = Label(window, text=f'Link to Live Launch: {stream}')
link.pack()

fids = Label(window, text=f'Flight ID: {sflightid} - Flight number: {sfnum}')
fid = Label(window, text=f'Flight ID: {flightid} - Flight number: {fnum}')
fid.pack()

pg2button = Button(window, text='Previous flight', command=gotopg1)
pg1button = Button(window, text='Next flight', command=gotopg2)
pg1button.pack()

window.mainloop()
