screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Raz" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value raz_ep
                    range raz_ep_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[raz_ep] / [raz_ep_max]" size 16


    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Cool Janitor Mole" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value jm_ep
                    range jm_ep_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "???? / ????" size 16


    text "Wild COOL JANITOR MOLE appeared!" xalign 0.5 yalign 0.05 size 30

    #### Some variables that describes the game state.
    # ep is exhaustion, pp is persuasion
label battle_mole_1:

    $ jm_ep_max = 30
    $ jm_ep = jm_ep_max

    $ raz_ep_max = 50
    $ raz_ep = raz_ep_max


    scene sewer
    play music "audio/Fightin_Time.mp3" fadein 3.0
    show janitor:
      xalign 0.9
      yalign 0


    show raz:
        xalign -0.2
        yalign 0
    jm "You don't know what you're messing with."
    jump janitor_mole_questions


label janitor_mole_questions:

    #### Let's show the game screen.
    #
    show screen simple_stats_screen
    $ raz_correct = 0

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    "Wild JANITOR MOLE appeared!"
    jump question1

label question1:

    menu:

        jm "How did you know that our hideout was located in the sewers?"

        "Newspaper Clippings" if newspaper_clippings:
            r "These newspaper clippin's right here show so!"
            jm "Ha! That's a bunch of bogus! The news don't know about this place."
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)
            jm "And even if they did, they wouldn't publish it."

            jump question2

        "Cherry's Conspiracy Board" if conspiracy_board:
            r "Right here on this conspiracy board! My girl has pieced together your tracks!"
            jm "Agh! How could you have found that! Stupid rat!"
            $ raz_correct += 1

            jump question2

        "Wanted Poster" if wanted_poster:
            r "Simple! With this wanted poster!"
            jm "That... {w}that literally says nothing about this place. Are you blind?"
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)

            jump question2

label question2:
    menu:
        jm "I think you're lying when you say that we have committed multiple mischievous crimes in the past. Prove it!"
        "Crowbar" if crow_bar:
            r "This crowbar is your primary criminal tool!"
            jm "That's just a crowbar. Nothing illegal. You can't even prove that that is ours."
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)
            jump question3

        "Footprints" if foot_prints:
            r "I've spotted your footprints all over the place!"
            jm "So what? Are we not allowed to go to public areas anymore?"
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)
            jump question3

        "Newspaper Clippings" if newspaper_clippings:
            r "The news have covered your crimes many many times!"
            jm "Ack! I knew we should've cleaned up the reporters' stories before they could be released!"
            $ raz_correct += 1
            jump question3

label question3:
    menu:
        jm "What made you think we were heading to the Musky Mug after capturing Cherry?"

        "Footprints" if foot_prints:
            r "Your footprints led me right where I needed to be!"
            jm "Ah! I forgot to sweep them away!"
            $ raz_correct += 1
            jump end_mole1

        "Ring Pop" if ring_pop:
            r "This very ring pop guided me!"
            jm "You sound crazy."
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)
            jump end_mole1

        "Wanted Poster" if wanted_poster:
            r "This wanted poster led me right to you!"
            jm "That says literally nothing about where we went!"
            $ jm_damage = renpy.random.randint(4, 6)
            $ raz_ep -= jm_damage
            with Shake((0, 0, 0, 0), 1.0, dist=30)
            jump end_mole1
    #
    ####
label end_mole1:
    hide screen simple_stats_screen


    if raz_correct == 3:
        jm "Yikes! You've got some true detective skills, I'll give you that."
        jm "And I dont give compliments out easy, don't count on it again, punk."

    if raz_correct == 2:
        jm "WHA- I, I CANT believe you've OUTSMARTED me this time."

    if raz_correct == 1:
        jm "By pure dumb luck, you've caught one of my questions{w}, but your luck won't last forever."

    if raz_correct == 0:
        jm "Are you even trying?"
        jm "You aren't worth spending time on, urgh."

    hide janitor
    jump battle_mole_2
