label locker_start:
    scene lockerroom
    show raz:
        xalign -0.2
        yalign 0

    play music "audio/Locker Room.mp3" fadein 3.0
    if janitor_talked == False:
        "So... this is the locker room, huh? Time to get  a-searchin'."
    else:
        "Alright, stepping away from the lockers now."

    $ b_1 = False
    $ b_2 = False
    $ lr_1 = True

    hide raz
    call screen locker_room

label locker_exit:
    scene lockerroom
    show raz:
        xalign -0.2
        yalign 0
    if screw_driver:
        "Okay, Erret said something about the back alley being used to smuggle in some stuff."
        "Time to go check that out."
        $ lr_1 = False
        $ ba_1 = True
        hide raz
        jump back_alley_start
    else:
        "Whoever left this room did a really bad job at concealing it."
        "Time to follow this convenient lead."
        $ lr_1 = False
        $ ba_1 = True
        hide raz
        jump back_alley_start

label lockers_grime:
    scene lockerroom

    if grime == False:
        show raz horror:
            xalign -0.2
            yalign 0
        "Yikes, looks like the lockers and benches are missing their layer of grime."
        "Whoever Erret hired as the janitor must not be doing a good job -- this place is way too clean!"
        $ grime = True
        hide raz horror
        call screen locker_room

    else:
        show raz:
            xalign -0.2
            yalign 0
        "Yeesh... alright, let's not spend more time looking at this filthless place..."
        hide raz
        call screen locker_room


label lockers_next_zoom:
    scene lockerroom_zoom
    show raz:
        xalign -0.2
        yalign 0
    if janitor_locker_open == False:
        "Alright, seems like her locker is among one of these..."
    else:
        "Aight, let's check this area one more time then."
    hide raz
    call screen lockers_zoom

label lockers_cherry:
    $ cherry_locker_open = True
    scene lockerroom_zoom
    show raz:
        xalign -0.2
        yalign 0
    "Let's hope this key works."
    "Nice! Yea! Cherry's locker~"
    "Dang, my girl's such a packrat, what is all of this mess?"
    hide raz
    call screen lockers_zoom

label lockers_janitor:
    $ janitor_locker_open = True
    scene lockerroom_zoom
    show raz:
        xalign -0.2
        yalign 0
    "Let's hope this key works."
    "Huh, the key didn't take, but... the door to this one wasn't locked?"
    #shit falls OUT
    if grime == True:
        "Ah. Figures. It's that incompetent janitor's closet."
    else:
        "Ah. Figures. It's the janitor's closet."

    "Huh? What was that? Did something fall?"
    hide raz
    call screen lockers_zoom


label lockers_screw_driver:
    scene lockerroom_zoom
    show raz:
        xalign -0.2
        yalign 0
    if eye_guy_snack == False:
        "Wait, what's that noise? Is somebody coming in the locker room?"
        jm "Why hello there sweets, what are you doing back here?"
        "Ah, it's the janitor."
        show janitor:
            xalign 0.9
            yalign 0
        r "Oh, hi! I’m just getting something for my girlfriend. Don't mean no trouble!"

        jm "Hmmph, I see, I thought you were here to take some of my goods, since it’s {b}me{\b} of course!"

        r "I'm not here for that! No need to worry, I don’t need your um, goods."

        jm "Oh yeah? You wish you can have all of this, don't you?"
        jm "I’m so much better compared to you haha!"
        "What's this guy on??"

        r "Okay, mole dude...thanks, but I’m a little busy here."

        jm "You don’t deserve my valiant knowledge. I’ll go find someone worthy of my time."
        hide janitor
        #mole leaves
        "Yikes, let's get back to what I was doing."
        show screwdriver:
            xalign 0.5
            yalign 0.4
        "Rightttt, the screwdriver."
        hide screwdriver
        $ screw_driver = True
        $ janitor_talked = True
        hide raz
        call screen lockers_zoom
        #screwdriver gained

    else:
        show raz:
            xalign -0.2
            yalign 0
        "Oh? What's this? A screwdriver, huh."
        #noises from the back
        "Oh snap, what was that? Somebody's coming in?"
        "Quick quick! Gotta hideeeee in this locker. Best detective idea yet!"
        "RATS! I dropped the screwdriver!"
        "Welp, too late now!! Into the locker I go!"
        hide raz
        scene blank_textre
    #a black screen as they hide in the locker

        ih "hmm hmm, I'm the best, yea I'm the greatest! Bestest janitor in the area~"
        "Urgh, sounds like some kind of idiot is out there singing."
        "I'll just wait them out."
        "..."
        "..."
        ih "... I d-{w} what I w-{w}, make so muc-{w} th-{w} not so le-{w} th-{w} oh ye-~..."
        "... Wait, I think they are leaving?"
        "I think I just heard a big door creaking noise."
        "Ah yep, yeah they're gone."
        #steps out of the locker
        show raz:
            xalign -0.2
            yalign 0
        "Aw dang, whoever that was took the screwdriver before I could nab it."
        "Wait though, it looks like the exit door hasn't been closed properly."
        "Maybe it'd be smart to follow them out once I'm done here."
        hide raz
        $ janitor_talked = True
        scene lockerroom_zoom
        call screen lockers_zoom

label locker_room_conspiracy_board:
    show board:
        xalign 0.5
        yalign 0.4
    show raz alt:
        xalign -0.2
        yalign 0
    "Woah...Cherry was deep into this gang information gathering. Looks like she put a lot of effort into this."
    show raz:
        xalign -0.2
        yalign 0
    "It says here they're rumored to operate in the sewers beneath Placeholder Avenue. Wait--that's the road this bar is on!"
    hide board
    hide raz
    $ conspiracy_board = True
    call screen lockers_zoom

label locker_room_wanted_poster:
    show poster:
        xalign 0.5
        yalign 0.4
    show raz:
        xalign -0.2
        yalign 0
    "A wanted poster...for a trenchcoat? Made, uh, by Snek? Doesn't he love that coat to death?"
    "And how is this related to the whole gang thing? None of this makes sense..."
    hide raz
    hide poster
    $ wanted_poster = True
    call screen lockers_zoom
