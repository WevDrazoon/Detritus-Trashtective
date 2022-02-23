label notebook_ringpop:
    show ring:
        xalign 0.5
        yalign 0.4
    "I can't wait to give Cherry this ring. It's top-notch! Only the best for her~"
    #hide items
    hide ring
    jump notebook_page_one

label notebook_clippings:
    show clippings:
        xalign 0.5
        yalign 0.4
    "Cherry's always carrying newspaper clippings...I had no idea she was collecting information about a gang. Is she serious about this?"
    #hide items
    hide clippings
    jump notebook_page_one

label notebook_foot_prints:
    show footprints:
        xalign 0.5
        yalign 0.4
    "These footprints were strange...it's a good thing I remembered to immortalize their intricate shape in this notebook! These are the footprints of a coward."
    #hide items
    hide footprints
    jump notebook_page_two

label notebook_notebook:
    show notepad:
        xalign 0.5
        yalign 0.4
    "I found this amazing notebook in the trash. how convenient!"
    #hide items
    hide notepad
    jump notebook_page_two

label notebook_goon_password:
    #show item
    "Belle said the password the goons use is \"AVOGADRO\". Special avocado?"
    #hide items
    jump notebook_page_three

label notebook_erret_teach:
    #show item
    "Cherry wasn't at the bar...but I spoke to Erret and he taught me how to use a revolver."
    "I hope I won't need this information - killing is too lowly for detectives~"
    #hide items
    jump notebook_page_three

label notebook_eye_guy_healing:
    #show item
    "A bottle of essential oils dropped from eye guy's hole— NOT THAT KINDA HOLE!"
    #
    #hide items
    jump notebook_page_three

label notebook_eye_guy_snack:
    show fetch:
        xalign 0.5
        yalign 0.4
    "An apple-banana burrito? Belle is one heck of a gourmet chef."
    #hide items
    hide fetch
    jump notebook_page_three

label notebook_locker_key:
    show key:
        xalign 0.5
        yalign 0.4
    "I got the key to Cherry's locker at the bar. I guess she must have forgotten it here?"
    #hide items
    hide key
    jump notebook_page_four

label notebook_wanted_poster:
    show poster:
        xalign 0.5
        yalign 0.5
    "Looks like an old wanted poster about some kind of trench coat theif?"
    "This must have to do with the gang activity the clippings mentioned."
    "More information is always welcomed. "
    #hide items
    hide poster
    jump notebook_page_four

label notebook_conspiracy_board:
    show board:
        xalign 0.5
        yalign 0.4
    "A board of a bunch of information about the gang collected by cherry."
    "Looks like she put a lot of effort into this."
    "Huh wait, there seems to be something scribbled in the sides?"
    "What is that... Avocado?"
    "Avogado? Avogadro? Something to do with... thats some really scribbled writing... moles?"
    #if u already have the code, it will just reaffirm it
    #hide items
    hide board
    jump notebook_page_five

label notebook_screw_driver:
    show screwdriver:
        xalign 0.5
        yalign 0.4
    "I found this screwdriver in the locker room. Detectives keep tools like this all the time, right? I guess it could be useful somewhere..."
    #hide items
    hide screwdriver
    jump notebook_page_five

label notebook_crow_bar:
    show crowbar:
        xalign 0.5
        yalign 0.4
    "I raided the trash behind the bar and found a crowbar. I think it can be used to force things open? I don't think I'd need this... but who knows!!"
    #hide items
    hide crowbar
    jump notebook_page_six

label notebook_revolver:
    #show item
    show gun:
        xalign 0.5
        yalign 0.4
    if erret_teach:
        "Wow, a real working revolver! Never thought I'd hold one. I still feel a little in over my head, but at least Erret ~kinda~ taught me how to use this!"
    else:
        "Wow, a real working revolver! Never thought I'd hold one. I don't really know how to handle this, but...I'll figure it out if I have to!"
    #hide items
    hide gun
    jump notebook_page_six
