scene black
scene bg 011
n "\"Да, слушаю."
extend " Желаете вызвать скорую помощь или пожарную службу?\""
n "\"Э-э... пожарных!\""
nvl clear
n "\"У вас пожар или поджог по неосторожности?"
extend " Говорите спокойней, пожалуйста.\""
n "\"К-кажется, пожар..."
extend " Я звоню с придорожного комплекса XX на трассе XX... Из-за гор почему-то поднимается дым, и огонь видно."
extend " Не знаю, почему, туда никто никогда не ходит..."
extend " В общем, подумал, надо позвонить!"
extend " А то ещё начнётся лесной пожар!\""
nvl clear
n "\"Ясно."
extend " Мы немедленно вышлем людей. Не могли бы вы сообщить ваше имя и телефонный номер, по которому с вами можно будет связаться, а также где именно вы наблюдаете возгорание?\""
nvl clear
scene black
n "\"Говорит диспетчерская пожарной службы."
extend " Поступил звонок о подозрительном возгорании на склоне горы XX."
extend " От трассы далеко — возможно, что какая-то парочка развела костёр или кто-то незаконно сжигает мусор."
extend " Горит глубоко в лесу."
extend " Домов рядом нет, но возможно расползание огня."
extend " Немедленно отправляйтесь и проверьте, что там.\""
nvl clear
n "\"Диспетчерская, слышите нас?"
extend " На связи пожарная команда района XX."
extend " Мы на месте возгорания."
extend " Видим горящую бочку, рядом никого нет."
extend " Огонь тушится, угрозы пожара более нет."
extend " .........И{w=1.0}...... это...{w=0.8}...... там, похоже... внутри человек."
extend " Словно бы кого-то полили чем-то вроде керосина... и подожгли......"
extend " Знаете...... наверное, стоит вызвать полицию...\""
n "\"{b}Ох... ОХ!!{/b}"
extend " {b}Т-то-точно, там тру-уп!!{/b}"
extend " {b}Ч-человеческий!!{/b}"
extend " {b}Аааааааа!!......{/b}\""
nvl clear
scene black
call screen tips_tata
return
