luminosidad_del_ambiente = 0

def on_forever():
    global luminosidad_del_ambiente
    luminosidad_del_ambiente = input.light_level()
    led.plot_bar_graph(luminosidad_del_ambiente, 255)
basic.forever(on_forever)

def on_forever2():
    global luminosidad_del_ambiente
    luminosidad_del_ambiente = input.light_level()
    if luminosidad_del_ambiente > 200:
        servos.P0.set_pulse(2500)
        servos.P0.set_angle(120)
        servos.P1.set_angle(120)
    else:
        servos.P0.set_pulse(2500)
        servos.P0.set_angle(0)
        servos.P1.set_angle(0)
basic.forever(on_forever2)
