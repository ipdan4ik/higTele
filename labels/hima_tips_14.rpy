    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
    play music msys06
    scene bg 093 with dissolve_04
    n "В школе день открытых дверей. День солнечный."
    n "{nw}"
    n "Урок готовки. Она уверенно готовит японское карри."
    n "В то время как дети её возраста обращались с кухонными ножами ещё стеснённо, на то, как она владела ножом, стоило посмотреть."
    nvl clear
    n "Учительница подошла вплотную ко мне и, улыбнувшись, сказала, что я замечательно учу свою дочь."
    n "Я обманула её, кивнув с неопределённой улыбкой."
    n "{nw}"
    stop music fadeout 1.0
    n "......Ведь я никогда не учила её готовить карри."
    n "{nw}"
    n "А она споро чистила овощи, которые кидала в кастрюльку строго в порядке варки."
    nvl clear
    scene black with dissolve_04
    play music days_of_children
    n "Любой прочий родитель завосторгался бы неожиданному таланту ребёнка."
    n "Но не в моём случае."
    n "{nw}"
    n "Это потому что кто-то, без сомнения, тайком от меня научил её готовить карри."
    n "Мне стало беспокойно, хоть я промолчала."
    nvl clear
    n "Спросив, я узнала, что дочь умеет и шить, и стирать бельё."
    n "Я никогда её тому не учила — да и не видела никогда, чтобы она этим занималась дома."
    nvl clear
    n "Готовка, шитьё, стирка..."
    n "Не сомневаюсь, старики ещё многому её учат у меня за спиной."
    n "{nw}"
    n "И мало им того — они забивают девочке голову дурацкими суеверьями, втолковывают, что она — воплощение Оясиро-сама."
    nvl clear
    scene bg 062 with left_03
    n "Я пожаловалась мужу, сказала, что нельзя позволять старикам её видеть."
    n "{nw}"
    n "Но, как смотритель храма Фурудэ, тот не может выступить против них — они всё-таки к тому же и прихожане."
    n "«...Да пускай балуют, что такого-то?» — равнодушно говорит он."
    nvl clear
    n "Я возразила."
    n "Она — дочь наша, и она не должна отличаться от остальных."
    n "И она вовсе не чёрт знает что, не какое-то там воплощение Оясиро-сама, как надеются старики."
    nvl clear
    scene bg 203 with dissolve_04
    n "Пожилые люди верят, что у неё есть божественная сила."
    n "{nw}"
    n "Они болтают, она может предсказать погоду на завтра, но сколько раз я видела, как она уходила без зонтика и возвращалась вымоченной до нитки."
    nvl clear
    scene black with dissolve_04
    scene bg 223 with dissolve_04
    n "Они говорят, она может видеть, что происходит в чужих странах, «внутренним оком», но всё её знание — от новостных программ, которые та постоянно смотрит."
    n "{nw}"
    n "Они говорят, она знает то, чего знать не должна, но это всё потому, что одни селяне втемяшивают ей тайком всякое, а другие поддакивают."
    nvl clear
    scene black with fastdown
    n "Вот только...... помню, однажды все думали, что погода будет хорошая, а она настояла на том, чтобы захватить зонт."
    n "Случился дождь, и зонтик нас защитил."
    n "{nw}"
    n "......По-моему, несколько раз Рика узнавала о крупных событиях в других странах до того, как их показывали в новостях."
    n "Я решала, та подслушала по радио срочное сообщение или что-нибудь в этом духе."
    nvl clear
    n "......«Она знает то, чего знать не должна»...{w=1.0} Вот это-то......{w=1.0} я сейчас и наблюдаю."
    n "{nw}"
    n "Она готовит японское карри, хотя никто не мог её научить."
    nvl clear
    n "Нет-нет... что это я."
    n "Кто-то её научил, точно."
    n "Кто-то чему-то учит Рику без моего ведома."
    nvl clear
    scene bg 093 with up
    n "\"Карри Фурудэ-сан просто великолепно."
    extend " Ставлю вам «особое отличие с плюсом»!\""
    show rika hima wa_a1 at central with dissolve_04
    n "\"......Нипа-а~{font=DejaVuSans.ttf}☆{/font}.\""
    n "\"У кого вы учились готовить?"
    extend " В семье, наверное?\""
    n "\"......Да."
    extend " В семье же.\""
    nvl clear
    n "Остальные родители восхитились."
    n "{nw}"
    n "{b}Ложь, ложь.{/b}"
    extend " {b}Я ничему её не учила.{/b}"
    n "{b}Кто, кто?{/b}"
    extend " {b}Кто забивает ей голову?{/b}"
    n "{b}Она никакое не воплощение Оясиро-сама — она всего лишь моя обыкновенная дочь!{/b}"
    nvl clear
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    call screen tips_hima
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
