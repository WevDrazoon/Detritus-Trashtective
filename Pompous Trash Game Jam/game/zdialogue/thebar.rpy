label bar_intro:
    play music "audio/Bar.mp3" fadein 3.0
    pause 3
    scene bar
    show raz:
        xalign -0.2
        yalign 0
    "There are evident signs of a bar fight here."
    "Indents on the wall, scratches on the tables, torn clothes everywhere, and markings of shoe soles on the wooden floors."
    if foot_prints == True:
        show footprints:
            xalign 0.5
            yalign 0.4
        "Wait a minute, shoe sole markings? As in tracked inside here with mud? Like from those tracks at Pu Belle's?"
        "That's pretty sus."
        hide footprints
    "Seems like a rough part of town...just the kind of place Cherry likes to hang out at."
    eyh "Ay rat."
    eyh "Psssst rat."
    eyh "Over here."
    r "Uhh...{w} hello?{w} Is someone there...{w} behind the wall?"
    show eyeguy:
        xalign 0.9
        yalign 0.5
    i "Why hello there! Fancy seeing you here, young'un!"
    r "Woah! Uhm... {w} hi. What are you doing back there exactly?"
    i "Not relevant, young'un, but what {i}is{/i} relevant is that some lil' birdie told me that you are looking for your girlfriend..."
    i "Cherry, was it?"
    i "Anyways, I might have seen her, but I require some food from the infamous Chez Pu Belle's to jog my memory a bit."
    r "Huh? What? I mean {w}yes; I am looking for her, but how do you even know? Where did you get this fro—"
    with Shake((0, 0, 0, 0), 1.0, dist=20)
    i "Hush"
    i "It's alright. Don't sweat the small stuff!"
    i "Could you get me that grubby food?"
    $ jy_1 = False
    menu:
        "Yea sure, why not":
            r "Uhm... {w} I mean sure?"
            r "If you have information on where she is, then...hell yeah! Food is on its way!"
            hide raz
            hide eyeguy
            jump junkyard_fetchquest

        "Um, no. Bye guy.":
            r "I'm fine. I think I can deal with this myself, but thanks for the offer and help!"
            "Yikes, what was that dude on about..."
            "Anyways, there's Erret at the bar, gotta go shake him down."
            $ jy_1 = False
            $ b_1 = True
            hide raz
            hide eyeguy
            call screen bar_erret

#the scene that brings you to the clickable things after fetching food for eye guy


label erret_talk_intro:
    scene bar
    show raz:
        xalign -0.2
        yalign 0

    show erret:
        xalign 1.5
        yalign 0
    e "Raz! What can I get you tonight?"
    r "Information.{w} I'm looking for Cherry."
    r "We were supposed to go out on a date tonight, but apparently some co-workers dragged her to work for a shift."
    r "So... {w} I was wondering if I'd be able to find her here?"

    default does_she_work_tonight = False
    default what_happened_here = False
    default locker_keys_convo = False
    default trash_gang = False
    default cherry_info = False

    jump erret_questions

label erret_questions:
#erret questions and actual dialogue hasnt been finalised yet
    scene bar
    show raz:
        xalign -0.2
        yalign 0

    show erret:
        xalign 1.5
        yalign 0
    menu:
        "Does she work tonight?" if does_she_work_tonight == False:
            e "Can't say I've seen 'er. Why not order a drink with a cherry instead?"
            r "I'm fine. I'm looking for {b}my{/b} Cherry."
            r "So... What happened here?"
            # interaction that leads to locker keys
            $ locker_keys = True
            $ does_she_work_tonight = True
            jump erret_questions

        "What happened here?" if what_happened_here == False:
            e "Local scum bringing unsavoury business to the bar, trash gang business."
            e "Heard they--"
            e "Whoop, said a bit too much there."
            r "Trash gang? Local scum is your default clientele, Erret."
            e "Pish posh{w}, the town itself is scum, and you're no better. {w} You might wanna keep your voice down, kid."
            e "The dumpsters' got ears."
            $ what_happened_here = True
            $ trash_gang = True
            jump erret_questions

        "Who is the trash gang?" if trash_gang:
            r "Who is the trash gang?"
            e "Just a new violent gang. Rumours've been circulating."
            r "It's not like Cherry to disappear like this. Where can I find the trash gang?"
            e "Go look for trash, and you'll be next in the heap."
            e "But... {w} I heard they move cargo through the alleys at night, and into the sewers."
            e "I even got myself one of them fancy laser pistols for protection."
            e "Y’know those things are battery powered now? All I gotta do is charge the damn thing before I turn in."
            $ erret_teach = True
            $ cherry_info = True
            $ trash_gang = False
            jump erret_questions

        "Got any more info about Cherry?" if cherry_info:
            e "Oh! Yea! Cherry's got a locker out back."
            e "Employee keys are kept under my watchful supervision."
            show key:
                xalign 0.5
                yalign 0.4
            e "Go check if it'll put the mind at ease. {w}A stiff drink will do the same."
            r "Thanks for the help, Erret!"
            hide key
            e "No prob kid, don’t stay in there too long."
            e "I got my own business to tend to later."
            r "Gotcha boss."
            #get keys
            #erret leaves
            "Pretty cool of Erret to hand those sweet sweet keys over. Time to check out that locker room."
            $ locker_key = True
            $ what_happened_here = True
            $ renpy.notify("New notebook entry!")
            hide raz
            hide erret
            jump locker_start

label eyeguy_notalk:
    scene bar
    show raz:
        xalign -0.2
        yalign 0

    "Seems like that guy, Eye Guy, doesn't want to talk to me cuz I said no."
    show raz alt:
        xalign -0.2
        yalign 0
    "Their loss, I'm super cool~"
    hide raz
    call screen bar_erret

label eyeguy_give_food:
    scene bar
    play music "audio/Bar.mp3" fadein 3.0
    show raz:
        xalign -0.2
        yalign 0

    show eyeguy:
        xalign 0.9
        yalign 0.5
    r "Here ya go!"
    i "Oh, why thank you for the amazing food!"
    i "Once I eat it, it should jog my memory.{w} Just gimme a minute."
    i "Om{w} nom {w} nom{w}.{w}.{w}.{w} Uhm, yeah! {w} I remember absolutely nothing."
    r "What?{w}.{w}.{w}."
    i "Thanks for the food! Farewell!"
    hide eyeguy
    r "What the hell?!{w} What was that for?!"
    r "Take this, stupid wall!"
    with Shake((0, 0, 0, 0), 1.5, dist=30)
    "{i}Clink{/i}"
    "Huh?{w} Did something fall?"
    $ jy_2 = False
    $ b_2 = True
    hide raz
    call screen bar_eyeguy


label eyeguy_had_taken_food: #getting item that eye guy has dropped
    show raz:
        xalign -0.2
        yalign 0

    "Ugh, whoever that Eye Guy was clearly isn't here anymore."
    "They did drop this, though."
    "Wait, what is this? Essential oils? They are more of a weirdo than I thought."
    $ eye_guy_healing = True
    hide raz
    call screen bar_eyeguy

label no_erret_key: #leave later sign, get keys and head to the locker
    show raz:
        xalign -0.2
        yalign 0
    "Huh, the bartender who's also Cherry's boss, Erret, doen't seem to be here rignt now."
    show key:
        xalign 0.5
        yalign 0.4
    "He did conveniently leave the locker keys on the bar table though..."
    hide key
    $ locker_key = True
    hide raz
    call screen bar_eyeguy

label bar_end:
    show raz:
        xalign -0.2
        yalign 0

    if locker_key and eye_guy_healing:
        "Nice, Ok, Let's go sneak in-- I mean, with total permission,-- go to the locker room..."
        $ renpy.notify("New notebook entry!")
        hide raz
        jump locker_start
    else:
        "Yikes, wait, I have a feeling we have stuff left to check out here..."
        hide raz
        call screen bar_eyeguy
