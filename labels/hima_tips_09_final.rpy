    $ persistent.hima_asobi = 3
    n "......Сейчас вы думаете про себя: «Че-е-го-о?»"
    nvl clear
    n "Именно так. В красной коробке лежала карамелька, в синей — жевательная резинка."
    n "Вы, наверное, тогда думали, что выбрали не ту; но, как можете видеть теперь, трудно сказать, какая же лучше, да?"
    n "{nw}"
    n "Ну, впрочем, у каждого свои вкусы."
    n "Кому нравится карамель, кому жевачка."
    n "...Не сомневаюсь, вам захочется выбрать то, что вам больше нравится."
    nvl clear
    n "Таков же и тот выбор, которого вы хотите в жизни."
    n "Вы, заботясь лишь о себе, хотите сначала посмотреть, что внутри обеих коробок, сравнить, а затем и сделать выбор."
    nvl clear
    n "Но знаете что?"
    extend " Действительность ничем не отличается от нашей игры."
    n "Когда выбираете одно, другой вариант навсегда уходит."
    extend " И вы так никогда и не узнаете, что же лучше."
    nvl clear
    n "Вы никогда не узнаете,"
    extend " стало бы вам лучше (или хуже),"
    extend " сделай вы тогда то-то"
    extend " или не сделай."
    n "В итоге вам остаётся лишь радоваться за себя или досадовать за сделанный выбор, и всё на том."
    nvl clear
    n "Но и ладно."
    n "По крайней мере, вам хоть понравился азарт выбора?"
    n "Знай вы, что внутри коробок,"
    extend " вы бы даже не стали терять время, выбирая между ними."
    n "Куда интереснее глядеть на изменчивое закатное небо и гадать, нагрянет ли нежданный летний дождь, чем играть в такую скучную игру в выбор коробки."
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return