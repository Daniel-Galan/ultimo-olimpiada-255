let luminosidad_del_ambiente = 0
basic.forever(function () {
    luminosidad_del_ambiente = input.lightLevel()
    led.plotBarGraph(
    luminosidad_del_ambiente,
    255
    )
})
basic.forever(function () {
    luminosidad_del_ambiente = input.lightLevel()
    if (luminosidad_del_ambiente > 200) {
        music.playMelody("- A - - A - - A ", 120)
        servos.P0.setAngle(90)
        servos.P1.setAngle(90)
        basic.pause(10000000000)
    } else {
        servos.P0.setAngle(0)
        servos.P1.setAngle(0)
    }
})
