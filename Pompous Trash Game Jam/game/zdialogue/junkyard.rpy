label start:
    #jump bar_intro
    #jump battle_mole_1
    #jump notebook_page_one
    #jump combined_goon_interaction
    #jump bar_intro
    #jump credits


    #show coat:
    #    xalign 1.2
    #    yalign 0

    #show dirty:
    #    xalign 0.9
    #    yalign 0

    #show erret:
    #    xalign 1.5
    #    yalign 0

    #show cherry:
    #    xalign 1.5
    #    yalign 0

    #show incel:
    #    xalign 0.9
    #    yalign 0
    #show incel alt:
    #    xalign 0.9
    #    yalign 0
    #show janitor:
      # xalign 0.9
       #yalign 0

    play music "audio/Prologue.mp3"
    ch "Let me go, you filthy vermin!"
    mh "We want you to tell us everything you know."
    mh "NOW!"
    ch "What are you talking about? I don’t even know who you are!"
    mh "Let me spell it out for you: Either you give up your little charade and start talking, or we’ll have to do this the hard way."
    mh "And we don’t want that, do we?"
    with Shake((0, 0, 0, 0), 1, dist=30)


    jump junkyard_intro

label junkyard_intro:
    play music "audio/Pu Belle.mp3" fadein 3.0
    pause 3
    scene junkyard
    show raz:
        xalign -0.2
        yalign 0

    "Cherry said she had somethin’ important to tell me last night on the phone. She is gonna propose to me, I know it!"
    "I mean come on! Inviting me to our favorite restaurant at sunset? Obvious much?"
    show ring:
        xalign 0.5
        yalign 0.4
    show raz alt:
        xalign -0.2
        yalign 0
    $ ring_pop = True
    "So...I bought her this dope candy ring as a counter proposal. She’ll never see it comin’! hehe~"
    hide ring

    show raz:
        xalign -0.2
        yalign 0
    "Huh...looks like Cherry isn't here yet. She does like being fashionably late...I'm not worried!"

    "This place is pretty nice, though."
    "I guess I'll take a look around while I wait, maybe find a place to sit..."
    hide raz
    call screen junkyard_table_intro

label junkyard_closeup:
    scene junkyard
    show raz:
        xalign -0.2
        yalign 0
    "That table over there looks like the one she reserved, but it's empty... She'll be here soon, I'm sure!"
    "I mean usually she is late to our dates but this is kinda stretching it."
    "Wait, is that what I think it is by the table..."
    hide raz
    call screen table_clippings

label junkyard_clippings:
    scene junkyard
    $ newspaper_clippings = True
    show clippings:
        xalign 0.5
        yalign 0.4
    show raz:
        xalign -0.2
        yalign 0
    "Cherry’s newspaper clippin’s? She’s always carryin’ em around...this means she was here, and then…"
    # show raz horrified
    show raz horror:
        xalign -0.2
        yalign 0
    "She abandoned me?"

    #Newspaper Clippings

    "These clippin's are all speculations about some gang, supposedly operating in this town...these sound like conspiracy theories to me!"
    "Why would Cherry have these?"
    show raz:
        xalign -0.2
        yalign 0
    hide clippings
    "This is gettin' a little fishy...why isn't she here yet?"
    show raz alt:
        xalign -0.2
        yalign 0
    "Well then, it's time to get some damn answers."
    hide raz
    $ jy_1 = True
    call screen junkyard


label Bell_talk_intro:
    scene junkyard
    if talk_bell == False:
        scene junkyard
        show bell:
            xalign 1.2
            yalign -0.5
        show raz:
            xalign -0.2
            yalign 0
        b "Hello there, Sweets! Can I get you anything?"
        r "Hiya! Uh, actually, I was wondering... have you seen a gorgeous rat with blade prosthetics around?"
        r "I found her newspaper clippin's at our table, but she ain’t back yet so I’m gettin’ hella nervous!"
        b "Now that you mention it, I did see someone like that head in here."
        b "She didn’t stay long, though."
        b "Some of her co-workers from the Musky Mug came to find her and she left with them."
        b "They told me not to say anything, but you seem worried."
        "The Musky Mug? Did Cherry forget something at work, or... is she needed for a late shift?"
        r "That seems a little strange, but at least she's alright..."
        r "Anyways....thanks for the info!"

        "I don't know...something feels off about this. I should go check the bar."
        $ talk_bell = True
        hide raz
        hide bell
        call screen junkyard
    else:
        show raz:
            xalign -0.2
            yalign 0
        "I highly doubt Belle has any more info to give me."
        "Best to leave them be."
        "But hey! Maybe I should go rummage through some of those fine trash bins!"
        call screen junkyard

label junkyard_notepad:
    scene junkyard
    if notebook == False:
        $ notebook = True
        $ renpy.notify("New notebook entry!")
        show raz:
            xalign -0.2
            yalign 0
        "I wonder what I'd get if I stuck my hand in it..."
        show notepad:
            xalign 0.5
            yalign 0.4
        "Haha! Great detectiving work done right here, got this um... Notebook?"
        "Maybe I can keep track of the clues I find in it."
        hide raz
        hide notepad
        call screen junkyard
    else:
        show raz:
            xalign -0.2
            yalign 0
        "Seems like there is nothing left here."
        hide raz
        call screen junkyard


label junkyard_tracks:
    scene junkyard
    show raz:
        xalign -0.2
        yalign 0
    show tracks:
        xalign 0.5
        yalign 0.4
    "Just some average worker boot tracks..."
    "They're pretty interesting, but I don't have time to stare at the ground right now."
    $ foot_prints = True
    hide raz
    hide tracks
    call screen junkyard

label leaving_junkyard:
    scene junkyard
    if talk_bell == True and notebook == True:
        show raz:
            xalign -0.2
            yalign 0
        "Cherry's workplace, here I come!"
        hide raz
        jump bar_intro
    else:
        show raz:
            xalign -0.2
            yalign 0
        "Hmm, I feel like I missed out on something..."
        hide raz
        call screen junkyard

label junkyard_fetchquest:
    scene junkyard
    play music "audio/Pu Belle.mp3" fadein 3.0
    show raz:
        xalign -0.2
        yalign 0
    "Alright, time to find some grub for that weirdo."
    $ jy_1 = False
    $ jy_2 = True
    hide scrollbar_size
    call screen junkyard_eyeguy


label fetchquest_belle:
    scene junkyard
    if eye_guy_snack == False:
        show raz:
            xalign -0.2
            yalign 0
        show bell alt:
            xalign 1.2
            yalign -0.5
        b "Oh Raz! You are just on time I was about to close up cuz I have to head to a meeting."
        show bell:
            xalign 1.2
            yalign -0.5
        r "Oh, perfect timing! I just came by to get some food for uh… a friend."
        r "Whatcha got?"
        b "Oh, I dont have much left, but...{w}I can give you some scraps?"
        r "Yea, that will do, thanks."
        show fetch:
            xalign 0.5
            yalign 0.4
    #*gives garbage burrito*
        show bell alt:
            xalign 1.2
            yalign -0.5
        r "Perfect. Belle, you are a lifesaver!"
        b "My pleasure, hope they enjoy it!"
        hide fetch
        show bell:
            xalign 1.2
            yalign -0.5
        b "Oh! But before you go, here, take this."
    #hands code for note code
        b "The coworkers who picked up Cherry dropped this on their way out."
        b "I had just forgotten to give it to ya."
        r "Whoa! Thanks again Belle!"
        show bell alt:
            xalign 1.2
            yalign -0.5
        b "Have a good night now!"
        hide bell
    #bell leaves
        "Well, I got what I came for, time to head on back"
        $ eye_guy_snack = True
        $ goon_password = True
        $ renpy.notify("New notebook entry!")
        hide raz
        call screen junkyard_eyeguy
    else:
        show raz:
            xalign -0.2
            yalign 0
        "Huh, looks like thats one important meeting huh."
        "They left so fast... Might be a sign to leave as well hah."
        hide raz
        call screen junkyard_eyeguy

label fetchquest_tracks:
    scene junkyard
    show raz:
        xalign -0.2
        yalign 0
    "Here are those tracks again. Now that I look at em, they kinda look really small... and there seems to be more this time."
    hide raz
    call screen junkyard_eyeguy
        # enter right food wrong food scene at pu belle. Accepted fetch quest.

label fetchquest_leave:
    scene junkyard
    if eye_guy_snack:
        show raz:
            xalign -0.2
            yalign 0
        "Aight, time to bounce."
        show incel:
            xalign 0.9
            yalign 0
        nm "Wait! M'lady! Please, one moment of your time!"
        r "???"
        nm "Hello there, gorgeous. Excuse me for a moment."
        #mole takes a moment to get on a table, making himself taller
        nm "I’m here for the eye candy that are the beautiful women such as yourself."
        r "Oh, uhm that certainly is some kind of compliment..but it's weird my dude…"
        nm "Whatchu talkin bout?? It’s free eye candy! I can’t pass this up."
        nm "Plus if I can take one of ya with me it’ll be a bonus for me hehe..."
        r "Okay... you are creepy and I am walking away now. I have places to be."
        hide incel
        show incel alt:
            xalign 0.9
            yalign 0
        nm "Gotcha hot stuff, I’ll be waiting for ya when you come back for me"
        hide incel alt
        r "Ya... no."

        "Now it's {b}REALLY{/b} time to go, yeesh."
        hide raz
        jump eyeguy_give_food

    else:
        show raz alt:
            xalign -0.2
            yalign 0
        "I can't just leave here without that weirdo's snack."
        hide raz
        call screen junkyard_eyeguy
