# intro sequence not yet written

label combined_goon_interaction:
    scene sewer dull
    play music "audio/Sewer.mp3" fadein 3.0
    default new_recruit = False
    show raz:
        xalign -0.2
        yalign 0
    "Huh, pretty snazzy place down here."
    show raz alt:
        xalign -0.2
        yalign 0
    "Time to sneak around, detective style~"

    show dirty:
        xalign 0.9
        yalign 0
    dm "Halt! Who goes there?"
    show raz:
        xalign -0.2
        yalign 0
    "Rats, I got caught..."
    dm "Wait, do you even know the secret password?"
    menu:
        "Avogadro, was it?" if goon_password:
            $ new_recruit = True

            r "I'm a new recruit. I was hired for my impeccable skill. The code is... {i}Avogadro{/i}."
            dm "Are you sure? You'll be committed to the gang{w}; once in, there's no going back."
            dm "The gang becomes your family, your life...{w} but the night shift sucks!"
            r "Whew, same here friend. What's the latest score?"
            dm "Big shiny bottles, boss says we can score enough to build a castle."
            dm "We were almost ratted out by the barmaid, but we took care of her."
            dm "Anywho, you should go see the boss. Follow me."
            jump hideout

        "(Yikes, I'll just make something up)":
            $ your_try = renpy.input("Uh, is it...")
            if your_try == "Avogadro":
                jump password_guessed
            if your_try == "avogadro":
                jump password_guessed
            if your_try == "AVOGADRO":
                jump password_guessed
            if your_try == "Password":
                jump password_guessed_maybe
            if your_try == "password":
                jump password_guessed_maybe
            if your_try == "PASSWORD":
                jump password_guessed_maybe
            else:
                jump guess_failed

        "No one can stop me from finding Cherry!":

            r "I'm here to save my girlfriend, and I will not let anyone stand in my way!"
            dm "Woah woah woah, slow down there. What makes you think she is even here?"
            "I'm pulling out the revolver."
            r "I {b}know{/b} she's here! Now, you better bring me to her or things will get dirty!"
            dm "OKAY OKAY! Fine, you psycho! I knew I smelled a rat! Follow me..."
            hide dirty
            hide raz
            jump final_notebook_check

label password_guessed:
    $ new_recruit = True
    scene sewer dull
    show raz:
        xalign -0.2
        yalign 0
    show dirty:
        xalign 0.9
        yalign 0
    dm "Ah, yeah that sounds about right."
    dm "You must be some kinda new recruit huh?"
    dm "Let me tell ya, the gang becomes your family, your life... but the night shifts suck!"
    "What!? I can't believe that worked!"
    r "Whew, yeah{w}, or so I have heard!"
    r " Hey friend, do tell. What's the latest score?"
    dm "Big shiny bottles. Boss says we can score enough to build a castle."
    dm "We were almost ratted out by the barmaid, but we took care of her."
    dm "Aw snap! Wait a minute. We are late for some important meeting."
    dm "Let’s go see the boss, you're gonna love us!"
    dm "Before we go in though, you better pull up any weapons to show the boss."
    dm "He kinda likes it when his goons have guns~"
    hide raz
    hide dirty
    jump final_notebook_check

label password_guessed_maybe:
    $ new_recruit = True
    scene sewer dull
    show raz:
        xalign -0.2
        yalign 0
    show dirty:
        xalign 0.9
        yalign 0
    dm "I feeeeeeeeel like that's wrong, but eh, sure yeah, it's right."
    dm "You must be some kinda new recruit huh?"
    dm "Let me tell ya, the gang becomes your family, your life... but the night shifts suck!"
    "What, is this guy an idiot? I can't believe that worked."
    r " Hey um... friend, do tell. What's the latest score?"
    dm "Big shiny bottles, boss says we can score enough to build a castle."
    dm "We were almost ratted out by the barmaid, but we took care of her."
    dm "Aw snap! Wait a minute. We are late for some important meeting."
    dm "Let’s go see the boss, you're gonna love us!"
    dm "Before we go in though, you better pull up any weapons to show the boss."
    dm "He kinda likes it when his goons have guns~"
    hide raz
    hide dirty
    jump final_notebook_check

label guess_failed:
    scene sewer dull
    show raz:
        xalign -0.2
        yalign 0
    show dirty:
        xalign 0.9
        yalign 0
    dm "Who do you take me for? I know our top notch secret codes, and that ain't it."
    "Guess the rat's out of the bag."
    #pull out gun
    "HECK YEAH LET'S PULL OUT THE GUN TOO."
    r "I'm here to save my girlfriend, and I will not let anyone stand in my way!"
    dm "Woah woah, slow down there. What makes you think she is here?"
    r "I {b}know{/b} she's here! Now, you better bring me to her or things will get dirty!"
    dm "OKAY OKAY! Fine, you psycho! I knew I smelled a rat! Follow me..."
    hide raz
    hide dirty
    jump final_notebook_check

label final_notebook_check:
    scene sewer dull
    show raz:
        xalign -0.2
        yalign 0
    show dirty:
        xalign 0.9
        yalign 0
    "Huh, before I follow this goon, maybe it'd be best to check my notebook one more time."
    "Ya know, just in case I'd need it."
    hide dirty
    menu:
        "Check notebook?"
        "Yea, that sounds good, I'll check the notebook.":
            $ ba_1 = False
            $ s_1 = True
            hide raz
            jump notebook_page_one
        "Nah, you know what, I don't need to check it.":
            hide raz
            jump hideout

label hideout:
    scene sewer dull
    play music "audio/Sewer.mp3" fadein 3.0
    show raz:
        xalign -0.2
        yalign 0
    show dirty:
        xalign 0.9
        yalign 0
    if new_recruit:
        dm "Ey boss, a new recruit is here to see you."
    else:
        dm "Ey boss, some rando wants to see you."

    hide dirty

    show erret:
        xalign 1.5
        yalign 0

    show bell:
        xalign 1.8
        yalign -0.5
    r "Belle?"

    # belle shows on screen

    if erret_teach:
        r "Erret?"
        r "What are you two doing here with them?"
    else:

        r "What are you two doing here with them?"
    r "Belle, they're the ones who took Cherry at your place, not her co-workers."
    b "What? I was fooled by some gangsters? How dare you trick me like that?! What despicable fiends!"

    hide bell
    if erret_teach:
        r "Erret, these are the gang members we were talking about back at the bar."
    else:
        r "Erret? Aren't you Cherry's boss? What are you doing here?"
    e "Eh? What? This is the manager who takes care of our establishment's upkeep."
    r "Erret, they are the ones who took Cherry!"
    e "Whoops, honest mistake~"
    e "But... ya know, it makes sense this imposter isn't the regular manager."
    e "They kept trying to increase the trash fee we both pay..."
    hide erret
    show coat:
        xalign 1.2
        yalign 0
    g "Ugh! Stop this dilly dally, you plebians."
    with Shake((0, 0, 0, 0), 0.5, dist=15)
    g "Pay attention to ME"
    with Shake((0, 0, 0, 0), 0.8, dist=20)
    g "When was the last time you followed your dreams?"
    g "Probably when you decided to date her."

    "Cherry!!"
    show cherry:
        xalign 0.5
        yalign 0
    pause 3
    hide cherry
    g "I have never been able to do such a thing until now."
    g "On the surface, both Belle and Erret preside over the junkyard in opulence."
    g "Producing waste by simply existing...{w} while my underlings exist without so much as a scrap!"
    g "But now, gaining power over a portion of the junkyard will change everything!"
    g "We'll be multi-{b}mole{/b}ionaires!"
    g "Mu{w}ha{w}ha{w}ha!"
    r "I can't believe you would do or even think such a thing, you vermin!"
    r "In the presence of the Trashtective, I will take you down and retrieve my Cherry back!"
    hide coat

    jump battle_mole_1
