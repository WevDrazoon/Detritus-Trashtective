#default pictures = False
#default diamond = False

#character settings
default talk_bell = False


# junkyard
default ring_pop = False
default newspaper_clippings = False
default notebook = False
default foot_prints = False

#eyeguy and erret items?
default eye_guy_snack = False
default eye_guy_healing = False
default goon_password = False
default erret_teach = False

# bar
default locker_key = False

# locker room + Janitor closet
default janitor_locker_open = False
default screw_driver = False
default grime = False
default janitor_talked = False

#Locker room + Cherry closet
default cherry_locker_open = False
default wanted_poster = False
default conspiracy_board = False

#back ally
default revolver = False
default crow_bar = False
default open_sewer = False



#Clues: ring pop, notepad, newspaper clippings, footprints,
# key to locker room, conspiracy board, wanted poster, screwdriver, crowbar.

#page one
label notebook_page_one:
    scene notepadbg
    play music "audio/Interrogation_Time.mp3" fadein 3.0

    if ring_pop == False and newspaper_clippings == False:
        "I haven't found any items to draw onto this page yet"

    "Seems like I'm on page 1."

    menu:

        "The Bestest Ring Pop Proposal Ring!" if ring_pop: #ring_pop
            jump notebook_ringpop

        "Cherry's Newspaper Clippings" if newspaper_clippings: # newspaper_clippings
            jump notebook_clippings

        "Flip to the next page": #this item
            jump notebook_page_two

        "Let's put the notebook down for now": #put book away
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                jump hideout


#page two
label notebook_page_two:

    if notebook == False and foot_prints == False:
        "I haven't found any items to draw onto this page yet"

    "Seems like I'm on page 2"
    menu:

        "The Great Trashtective Notebook" if notebook: #notebook
            jump notebook_notebook

        "Some Interesting Footprints" if foot_prints: #foot_prints
            jump notebook_foot_prints

        "Flip to the next page": #this item
            jump notebook_page_three

        "Let's put the notebook down for now": #put book away
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Sewers.mp3" fadein 3.0
                jump hideout


label notebook_page_three:

    if goon_password == False and erret_teach == False and eye_guy_snack == False:
        "I haven't found any items to draw onto this page yet"

    "Seems like I'm on page 3"
    menu:
        "Goon Code" if goon_password : #goon_password
            jump notebook_goon_password

        "Erret taught me something?" if erret_teach: #erret_teach
            jump notebook_erret_teach

        "Eye Guy's Gourmet Snack" if eye_guy_snack: #eye_guy_snack
            jump notebook_eye_guy_snack

        "The Essential Oils Eye Guy dropped..." if eye_guy_healing: #eye_guy_snack
            jump notebook_eye_guy_healing

        "Flip to the next page":
            jump notebook_page_four

        "Let's put the notebook down for now":
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Sewers.mp3" fadein 3.0
                jump hideout



label notebook_page_four:
    if locker_key == False and wanted_poster == False:
        "I haven't found any items to draw onto this page yet"

    "Seems like I'm on page 4"

    menu:

        "Locker keys~" if locker_key: #locker_key
            jump notebook_locker_key
        "Menacing Wanted Poster" if wanted_poster: # wanted_poster
            jump notebook_wanted_poster

        "Flip to the next page": #this item
            jump notebook_page_five

        "Let's put the notebook down for now": #put book away
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Sewers.mp3" fadein 3.0
                jump hideout


label notebook_page_five:

    if conspiracy_board == False and screw_driver == False:
        "I haven't found any items to draw onto this page yet"

    "Seems like I'm on page 5"
    menu:

        "Cherry's Conspiracy Board" if conspiracy_board: #conspiracy_board
            jump notebook_conspiracy_board

        "That Janitor's Screwdriver" if screw_driver: #screw_driver
            jump notebook_screw_driver

        "Flip to the next page": #this item
            jump notebook_page_six

        "Let's put the notebook down for now": #put book away
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Sewers.mp3" fadein 3.0
                jump hideout

label notebook_page_six:
    if crow_bar == False and revolver == False:
        "I haven't found any items to draw onto this page yet"
    "Seems like I'm on page 6"

    menu:
        "Random Crowbar" if crow_bar: #crowbar
            jump notebook_crow_bar
        "Hot Shit Rusty Laser Revolver With One Cartridge" if revolver: #revolver
            jump notebook_revolver

        "Flip to the next page": #this item
            jump notebook_page_one

        "Let's put the notebook down for now": #put book away
            if jy_1:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard
            if jy_2:
                play music "audio/Pu Belle.mp3" fadein 3.0
                call screen junkyard_eyeguy
            if b_1:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_erret
            if b_2:
                play music "audio/Bar.mp3" fadein 3.0
                call screen bar_eyeguy
            if lr_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen locker_room
            if lrz_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen lockers_zoom
            if ba_1:
                play music "audio/Locker Room.mp3" fadein 3.0
                call screen back_alley
            if s_1:
                play music "audio/Sewers.mp3" fadein 3.0
                jump hideout

    #if  == True:
    #if  == True:


    #scene notebookpages
    #hbox:


    #hbox:


    #if pictures == True:
        #show pictures.png
            #xpos ypos


#    if something == True
    #    call screen junkyard

#\n{image=images/dia.png}
