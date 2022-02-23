screen simple_stats_screen2:
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
            text "Dirty Mole" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value dm_ep
                    range dm_ep_max
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[dm_ep] / [dm_ep_max]" size 16


    text "Wild DIRTY MOLE appeared!" xalign 0.5 yalign 0.05 size 30

    #### Some variables that describes the game state.
    # ep is exhaustion, pp is persuasion
label battle_mole_2:
    $ dm_ep_max = 30
    $ dm_ep = dm_ep_max

    scene sewer
    show dirty:
        xalign 0.9
        yalign 0
    show raz:
        xalign -0.2
        yalign 0
    dm "You should have quit while you were ahead. You found us, and now we have to kill you!"
    jump battle_2_loop


label battle_2_loop:

    $ dm_ep = 30
    #### Let's show the game screen.
    #
    show screen simple_stats_screen2

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (dm_ep > 0) and (raz_ep > 0):

        menu:
            "Use an Object":
                menu:
                 # enter witty oneliners when writers make it
                    "Ring Pop" if ring_pop:
                        $ dm_ep -= 3
                        r "Ring Pop"
                        dm "A proposal to moi?"
                        $ ring_pop = False
                    "Newspaper Clippings" if newspaper_clippings:
                        $ dm_ep -= 2
                        r "Newspaper Clippings"
                        dm "Really? Paper? Are you serious right now?"
                        $ newspaper_clippings = False
                    "Locker Key" if locker_key:
                        $ dm_ep -= 5
                        r "Locker Key"
                        dm "Ow! That was tiny, but OW!"
                        $ locker_key = False
                    "Conspiracy Board" if conspiracy_board:
                        $ dm_ep -= 8
                        r "Conspiracy Board"
                        dm "WHERE DID YOU PULL THAT OUT FROM?!"
                        $ conspiracy_board = False
                    "Wanted Poster" if wanted_poster:
                        $ dm_ep -= 2
                        r "Wanted Poster"
                        dm "Really? Paper? Are you serious right now?"
                        $ wanted_poster = False
                    "Screwdriver" if screw_driver:
                        $ dm_ep -= 12
                        r "Screwdriver"
                        dm "WHAT THE- AHH!"
                        $ screw_driver = False
                    "Crowbar" if crow_bar:
                        $ dm_ep -= 10
                        r "Crowbar"
                        dm "THAT'S FOR CROWS, NOT MOLES!"
                        $ crow_bar = False
                    "Revolver" if revolver:
                        r "Should I really use this? I might not know how to use a {b}hot shit rusty laser revolver with one cartridge{/b}."
                        menu:
                            "Shoot":
                                if erret_teach:
                                    $ dm_ep -= 25
                                    r "Nice! Whatever rant Errent went into about guns helped me out!"
                                    dm "Wait, that's illegal! Also... ARRRGHHHH!!!"
                                    $ revolver = False

                                    #"ahh wait, right...I dont acctually know use this thing... OWW"
                                else:
                                    $ raz_ep -= 10
                                    r "Oww... {w} maybe I should've learnt how to shoot before using it."
                                    dm "Firstly, did ya just try to shoot me? Secondly, that was hilarious!"
                                    $ revolver = False
                            "Don't Shoot":
                                $ dm_ep -= 5
                                r "Eh, whatever, let's just throw the thing."
                                dm "Ack! Tetanus!"
                                $ revolver = False

            "Drink Essential Oils" if eye_guy_snack and raz_ep < raz_ep_max:
            # eye guy healy heals
                $ raz_ep = min(raz_ep+10, raz_ep_max)
                $ eye_guy_snack = False
                r "This Placebo Effect or whatever sure works wonders."

        $ dm_damage = renpy.random.randint(4,6)
        $ raz_ep -= dm_damage
        dm "I slap thee!"
        with Shake((0, 0, 0, 0), 1.0, dist=30)


    #
    ####

    hide screen simple_stats_screen2

    if dm_ep <= 0:
        dm "AHHHH! You stupid rat! You will never get your girlfriend back{w}, and we'll ensure that!"
        dm "Boss, finish 'em off!"
        dm "Heck yea~ I delivered that line just like boss made me memorize~"
        hide dirty
        jump battle_mole_3

    if raz_ep<= 0:
        dm "Hah! I got the rat down, boss! Let's dip!"
        hide dirty
        jump bad_ending
