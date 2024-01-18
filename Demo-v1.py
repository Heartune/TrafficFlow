import PySimpleGUI as gui


def showtime():
    window['-AOUT-'].update(ATime)
    window['-BOUT-'].update(BTime)
    window['plus-S1'].update('s')
    window['plus-S2'].update('s')


ATime = BTime = 50
gui.set_options(font=("Consolas", 16))
layout = [
    [gui.Text('A Rd. Traffic Flow'), gui.Input(key='-ATF-', size=(5, 1)), gui.Text('vehicles/s')],
    [gui.Text('B Rd. Traffic Flow'), gui.Input(key='-BTF-', size=(5, 1)), gui.Text('vehicles/s')],
    [gui.Text('A Rd. Incident Rate'), gui.Input(key='-AIR-', size=(3, 1)), gui.Text('%')],
    [gui.Text('B Rd. Incident Rate'), gui.Input(key='-BIR-', size=(3, 1)), gui.Text('%')],
    [gui.Text('A Rd. Emergency'), gui.Radio('Give Way', 'AE', key='-AGT-'), gui.Radio('Block Way', 'AE', key='-ABW-'),
     gui.Radio('None', 'AE', key='-ANONE-')],
    [gui.Text('B Rd. Emergency'), gui.Radio('Give Way', 'BE', key='-BGT-'), gui.Radio('Block Way', 'BE', key='-BBW-'),
     gui.Radio('None', 'BE', key='-BNONE-')],
    [gui.OK()],
    [gui.Text('A Rd. Time: '), gui.Text(key="-AOUT-"), gui.Text(key='plus-S1')],
    [gui.Text('B Rd. Time: '), gui.Text(key="-BOUT-"), gui.Text(key='plus-S2')],
]
window = gui.Window("Real-time Signal Timing System", layout, size=(1200, 740))
while True:
    event, values = window.read()
    print(event, values)

    if values['-ABW-']:
        ATime = 0
        BTime = 100
    elif values['-BBW-']:
        BTime = 0
        ATime = 100
    else:
        ATime = 100 * int(values['-ATF-']) / (int(values['-ATF-']) + int(values['-BTF-']))  # 暂定配时只考虑车流量
        BTime = 100 * int(values['-BTF-']) / (int(values['-ATF-']) + int(values['-BTF-']))
        ATime += 5 * int(values['-AIR-']) / 100  # 暂定罚时=事故发生率*5s
        BTime += 5 * int(values['-BIR-']) / 100
    showtime()  # 展示配时结果
    if event == gui.WIN_CLOSED or event == "Exit":
        break
window.close()
