    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play ambient lsys13
    n "Машина остановилась."
    nvl clear
    n "Ничего больше понять ему не удалось."
    n "Потому что, не удовольствуясь завязанными глазами, его ещё и закрыли в багажнике."
    n "{nw}"
    n "Он впервые понял, как же бессильны незрячие..."
    extend " Лишь на собственном опыте удалось ему проникнуться по-настоящему."
    nvl clear
    n "С первых же секунд он понял, что не стоит и пытаться освободиться. В тесноте багажника у него кружилась голова,"
    extend " и ему оставалось лишь ждать, пока от этой медленной пытки не помутится сознание."
    n "{nw}"
    n "Так что, когда машина затормозила и противная мелкая дрожь от движка прекратилась,"
    extend " его затуманенный разум охотно поверил в освобождение, хотя положение, в общем-то, нисколько не изменилось."
    nvl clear
    n "Само собой, он тут же очнулся от грёз."
    n "Услышав разговор своего похитителя с каким-то незнакомым пожилым человеком, он как мог напряг уши..."
    nvl clear
    n "\"......Здравствуйте."
    extend " Пацан в багажнике."
    extend " Он долго вырывался, так что сейчас, наверное, ослабел; но, как и приказывали, ни синяка, ни царапинки.\""
    n "\"...Да-да, блаадарствую за труды.\""
    nvl clear
    scene white with fade_010
    scene black with Dissolve(3.0)
    n "Багажник открыли. Поток свежего, прохладного воздуха обдал его."
    nvl clear
    n "Всего пару минут назад он только и думал о том, чтобы отсюда выбраться, но, как только багажник открыли, его сразу же охватила тревога."
    n "Он едва не пожелал, чтобы крышка ненавистной темницы снова закрылась, лишь бы хоть что-то его защищало от тех, кто снаружи."
    nvl clear
    n "Неожиданно голову погладила чья-то рука."
    n "Естественно, из-за повязки он не мог разглядеть, с ласкою ли его гладят или оценивают кожу, прежде чем снять скальп."
    extend " Ничего не понимая, он напрягся, готовясь к самому худшему..."
    nvl clear
    n "\"......У ты, мой хоремычный..."
    extend " Дрожишь весь..."
    extend " Ты полежи покамест без дрыгу...\""
    n "Ласковым голосом обратился к нему пожилой, поглаживая по голове."
    nvl clear
    n "\"Небось, круто тебе пришлось..."
    extend " Ничаго, дедка у тя славный."
    extend " Он тя скоро спасёт...\""
    n "Его, слышавшего раньше лишь столичную речь, мягкий деревенский говорок здорово удивил."
    n "{nw}"
    n "Вот только непонятно было, про что разговор."
    nvl clear
    n "Наконец, несколько раз повторив в уме: «Дедка у тя», он понял: тот говорит про его дедушку..."
    nvl clear
    n "Ладонь, гладившая голову, коснулась закрывающей глаза повязки."
    nvl clear
    n "\"......Лучше не трогайте..."
    extend " Нехорошо получится, если он нас запомнит.\""
    n "\"Хм... да, то так."
    extend " Тады хучь кляп, шо ли, вытащим..."
    extend " Вишь, едва дышит...\""
    n "\"......Он может закричать..."
    extend " Уж позвольте, мы с ним как-нибудь сами...\""
    nvl clear
    n "\"Тьфу, люди вы али хто?!!"
    extend " ...Главный дом запретил ево обижать."
    extend " Зарубите се на носу...\""
    n "\"Хорошо."
    extend " Пальцем его не тронем..."
    extend " Ну, если не вздумает рыпаться.\""
    n "Кто-то постучал по голове."
    nvl clear
    n "Его рука была груба и совсем не похожа на ту, что только что с жалостью гладила."
    n "{nw}"
    n "{i}Если не вздумает рыпаться.{/i}"
    n "{nw}"
    n "{i}«А если попробуешь пикнуть, то тут уж извини — как получится»{/i},"
    extend " — очень убедительно сообщало ему постукивание."
    nvl clear
    $ renpy.pause(1.0)
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return
