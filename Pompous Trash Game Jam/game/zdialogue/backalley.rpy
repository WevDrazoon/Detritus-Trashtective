label back_alley_start:
    scene back alley
    with dissolve
    show raz:
        xalign -0.2
        yalign 0

    "If the gang moves trash through the alleys, maybe they took Cherry closeby."
    "There’s only dingy dumpsters, and a sewer grate back here...I guess I should still look around, just in case."
    $ lrz_1 = False
    $ ba_1 = True
    if eye_guy_snack:
        hide raz
        call screen back_alley

    else:
        scene back alley
        "There are scuff marks around the sewer grate, maybe I can pry it open with the screwdriver?"
        "..."
        "Well, that didn't work. Maybe there's something else I can use around here."
        hide raz
        call screen back_alley


label back_alley_eyeguy_snack:
    show raz:
        xalign -0.2
        yalign 0
    if screw_driver:
        show screwdriver:
            xalign 0.5
            yalign 0.4
        "Why would I need a second screwdriver?"
        "I already have this one I stol- borrowed."
        "Plus, I'm not touching it, who knows what kind of stuff it's been through."
        hide screwdriver
        hide raz
        call screen back_alley

    else:
        show screwdriver:
            xalign 0.5
            yalign 0.4
        "A screwdriver? I guess the janitor must've dropped this on his way out."
        $ screw_driver = True
        $ renpy.notify("New notebook entry!")
        hide screwdriver
        "Wait...There are scuff marks on the sewer grate...maybe I can use that screwdriver to pry it open."

        "..."
        "Well, that didn't work. Maybe there's something else I can use around here."
        hide raz
        call screen back_alley

label back_alley_crowbar:
    show raz:
        xalign -0.2
        yalign 0
    show crowbar:
        xalign 0.5
        yalign 0.4
    "OH! A crowbar! These things are used to pry things open, aren't they?"
    $ crow_bar = True
    $ renpy.notify("New notebook entry!")
    hide crowbar
    hide raz
    call screen back_alley

label back_alley_sewer:
    scene back alley
    show raz:
        xalign -0.2
        yalign 0

    if crow_bar and screw_driver and revolver:
        "Aight, I think I have everything I need!"
        "These will be useful for opening that sewer lid! Let me try again..."
        "..."
        "It's open!"
        "Time to head inside, Cherry here I come!"
        jump combined_goon_interaction
    else:
        scene back alley
        "Dang, it wont budge with what I've got."
        "Maybe I can find something that could help me."
        hide raz
        call screen back_alley


label back_alley_revolver:
    show raz:
        xalign -0.2
        yalign 0
    "Huh, looks like someone dropped this."
    show gun:
        xalign 0.5
        yalign 0.4

    if erret_teach:
        "Good thing Erret taught me how to use a revolver!"
        "I still hope I won't need this, though. I'll keep it, just in case."
        hide gun
        hide raz
        $ revolver = True
        $ renpy.notify("New notebook entry!")
        call screen back_alley

    else:
        "I don't really know how to use this...hopefully I won't need to!"
        "I'll keep it, just in case."
        hide gun
        hide raz
        $ revolver = True
        $ renpy.notify("New notebook entry!")
        call screen back_alley
