init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
#notebooks screen

#Junkyard screens

screen junkyard_table_intro:
    add "junkyard.png"
    imagebutton: #done
        xpos 1254
        ypos 681
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("junkyard_closeup")

screen table_clippings:
    add "Item BG/junk_item.PNG"
    imagebutton:
        xpos 1392
        ypos 746
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("junkyard_clippings")

screen junkyard:#1
    add "Item BG/junk_item.PNG"
    imagebutton:#bell converstion
        xpos 1035
        ypos 300
        auto "Items/stick_figure_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("Bell_talk_intro")

    imagebutton: #notepad done
        xpos 551
        ypos 162
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("junkyard_notepad")

    imagebutton: #tracks on the floor done
        xpos 1800
        ypos 700
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("junkyard_tracks")

    imagebutton: #leave Ches Pou belle
        xpos 1550
        ypos 800
        auto "Items/next_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("leaving_junkyard")


    showif notebook: #menu sound
        imagebutton:
            xpos 1
            ypos 0
            auto "Items/notepad_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("notebook_page_one")


screen junkyard_eyeguy:
    add "Item BG/junk_item.PNG"
    imagebutton: #bell again
        xpos 1035
        ypos 300
        auto"Items/stick_figure_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("fetchquest_belle")
    imagebutton: #tracks on the floor again
        xpos 1800
        ypos 700
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("fetchquest_tracks")

    imagebutton: #leaving #menu sound
        xpos 1550
        ypos 800
        auto "Items/next_%s.png"
        hover_sound "audio/Menu Option.mp3"
        action Jump("fetchquest_leave")

    showif notebook: #menu sound
        imagebutton:
            xpos 1
            ypos 0
            auto "Items/notepad_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("notebook_page_one")


#bar screens

screen bar_erret:
    add "Item BG/bar_item.PNG"
    imagebutton: #Erret
        xpos 750
        ypos 170
        auto "Items/erret_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("erret_talk_intro")

    imagebutton: #eyeguy wont talk to u anymore
        xpos 1705
        ypos 254
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("eyeguy_notalk")

    imagebutton:
        xpos 1
        ypos 0
        auto "Items/notepad_%s.png"
        hover_sound "audio/Menu Option.mp3"
        action Jump("notebook_page_one")


screen bar_eyeguy:
    add "Item BG/bar_item.PNG"
    showif locker_key == False:
        imagebutton: #Erret is not there anymore, pick up keys
            xpos 507
            ypos 428
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("no_erret_key")
    showif eye_guy_healing == False:
        imagebutton: #eyeguy click on him but nobody is there anymore
            xpos 1705
            ypos 254
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("eyeguy_had_taken_food")

    imagebutton:
        xpos 1
        ypos 0
        auto "Items/notepad_%s.png"
        hover_sound "audio/Menu Option.mp3"
        action Jump("notebook_page_one")
    showif locker_key: #menu sound
        imagebutton:
            xpos 1550
            ypos 800
            auto "Items/next_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("bar_end")
    #imagebutton anything extra we want to add

#lockeroom scene

screen locker_room:
    add "lockerroom.png"
    imagebutton: # click to go to lockers zoom
        xpos 1193
        ypos 374
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("lockers_next_zoom")

    imagebutton: #comment about arrea, perhaps an item on the bench
        xpos 1120
        ypos 747
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("lockers_grime")

    showif janitor_talked:#menu sound
        imagebutton: #exit
            xpos 442
            ypos 325
            auto "eye_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("locker_exit")

    showif notebook:#menu sound
        imagebutton:
            xpos 1
            ypos 0
            auto "Items/notepad_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("notebook_page_one")

screen lockers_zoom:
    add "lockerroom_zoom.png"

    #lockers that can be opened
    showif cherry_locker_open == False:
        imagebutton: #gf locker, it opens
            xpos 467
            ypos 492
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("lockers_cherry")
    showif janitor_locker_open == False:
        imagebutton: #janitor locker_room
            xpos 1251
            ypos 492
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("lockers_janitor")

    showif janitor_talked: #menu sound
        imagebutton: # click to go back to the lockers
            xpos 1550
            ypos 800
            auto "Items/next_%s.png"
            hover_sound "audio/Menu Option.mp3"
            action Jump("locker_start")

    showif cherry_locker_open:
        add "lockerroom_cherry.png"
        showif conspiracy_board == False:
            imagebutton: #conspiracy_board
                xpos 492
                ypos 691
                auto "eye_%s.png"
                hover_sound "audio/NoSusSong.mp3"
                action Jump("locker_room_conspiracy_board")
        showif wanted_poster == False:
            imagebutton: #wanted_poster
                xpos 461
                ypos 267
                auto "eye_%s.png"
                hover_sound "audio/NoSusSong.mp3"
                action Jump("locker_room_wanted_poster")

    showif janitor_locker_open:
        add "lockerroom_janitor.png"
        showif screw_driver == False:
            imagebutton: #screwdriver
                xpos 1216
                ypos 850
                auto "eye_%s.png"
                hover_sound "audio/NoSusSong.mp3"
                action Jump("lockers_screw_driver")

screen back_alley:
    add "Item BG/alley_item.PNG"

    imagebutton: #screwdriver
        xpos 379
        ypos 630
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("back_alley_eyeguy_snack")
    showif crow_bar == False:
        imagebutton: #crowbar
            xpos 553
            ypos 690
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("back_alley_crowbar")
    showif revolver == False:
        imagebutton: #revolver
            xpos 1317
            ypos 660
            auto "eye_%s.png"
            hover_sound "audio/NoSusSong.mp3"
            action Jump("back_alley_revolver")

    imagebutton: #sewer grate
        xpos 799
        ypos 930
        auto "eye_%s.png"
        hover_sound "audio/NoSusSong.mp3"
        action Jump("back_alley_sewer")

    imagebutton: #menu sound
        xpos 1
        ypos 0
        auto "Items/notepad_%s.png"
        hover_sound "audio/Menu Option.mp3"
        action Jump("notebook_page_one")
