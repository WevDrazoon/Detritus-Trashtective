# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    $ config.keymap['game_menu'].remove('K_ESCAPE')

define r = Character("Raz", callback=raz_voice, who_color="#20d8f3")
define w = Character("Cherry", callback=cherry_voice, who_color="#32eaa3")
define b = Character("Belle", callback=belle_voice, who_color="#847AC1")
define e = Character("Erret", callback=erret_voice, who_color="#a4246e")
define i = Character("Eye Guy", callback=eye_guy_voice, who_color="#D836A7")

#goons
define g = Character("Mr. Jab", callback=g_voice, who_color="#d6bcbf")
define jm = Character("Beaumont", callback=jm_voice, who_color="#ea9d32")
define nm = Character("Alfred", callback=nm_voice, who_color="#e9253c")
define dm = Character("Jarred", callback=dm_voice, who_color="#547960")

define mh = Character("????", callback=g_voice, who_color="#d6bcbf")
define ch = Character("????", callback=cherry_voice, who_color="#32eaa3")
define ih = Character("????", callback=jm_voice, who_color="#ea9d32")
define eyh = Character("????", callback=eye_guy_voice, who_color="#D836A7")

# music

$ ring_pop = True

transform midleft:
    xalign 0.05 yalign 0.10

transform midright:
    xalign 0.90 yalign 0.10


default jy_1 = False
default jy_2 = False
default b_1 = False
default b_2 = False
default lr_1 = False
default ba_1 = False
default s_1 = False

label good_ending:
    play music "audio/Sewer.mp3" fadein 3.0
    hide screen simple_stats_screen3
    nm "?????"
    nm "HOW COULD YOU SURVIVE OUR FURY?!"
    nm "Fellas! Reassemble!"
    hide incel
    show coat:
        xalign 1.2
        yalign 0
    g "Automoles, roll out!"
    hide coat
    #goons go out
    r "That'll teach you not to mess with me or my Cherry ever again!"
    show cherry:
        xalign 1.5
        yalign 0
    r "Cherry! Thank goodness, you're in one piece!"
    r "I was so worried about you!"
    w "Raz! I'm so glad to be reunited; this day has been a pain in the butt."
    w "They caught me by surprise at Chez Pu Belle's, and I didn't know how you would react about—"
    with Shake((0, 0, 0, 0), 0.5, dist=15)
    r "Shh... it's alright, Cherry...{w} now that you're safe and sound, I couldn't be happier..."
    r "Except for one thing."
    w "And what is that?"
    r "Well, ya see...{w} I kinda was planning on proposing to you tonight, but the ring pop I was gonna give you kinda busted so uhm..."
    r "I'm really sorry."
    w "Oh Raz. You don't need to be sad about that, because I was planning on doing the same thing, hehe~"
    r "Our great minds sure do think alike! It would be my pleasure to be engaged to you!"
    w "Likewise! Now, can we please get outta these sewers and head back for that dinner you promised me?"
    r "Right, let's do that!"

    call credits from _call_credits
    return

label bad_ending:
    play music "audio/Sewer.mp3" fadein 3.0
    hide screen simple_stats_screen3
    nm "HAHA! I knew you weren't capable of truly beating us!"
    nm "GOOD LUCK FINDING YOUR GIRLFRIEND NOW!"
    nm "Fellas! Assemble!"
    hide incel
    show coat:
        xalign 1.2
        yalign 0
    g "Automoles, roll out!"
    hide coat
    # goons go out
    r "That'll teach you not to mess with me or my Cherry ever again!"
    r "Wait...{w} where is she?"
    hide raz
    show raz horror:
        xalign -0.2
        yalign 0
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    r "Where is Cherry?!"
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    r "I swear I saw her here when we got here!"
    r "Where did they take her?!"
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    show bell:
        xalign 1.2
        yalign -0.5
    b "Raz...{w} I feel like you should see this{w}.{w}.{w}."
    r "What is it?!"
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    hide bell
    # show box and prosthetics
    "I... I dont understand, I just saw Cherry..."
    "Why are her prosthetics just... there...?"
    "Is- is that- blood?{w}?{w}?{w}?"
    r "Oh{w} no{w} no no{w} no no no{w} no no no no"
    r "NO!"
    r "CHERRY PLEASE!{w} Come back..."
    r "p{w}l{w}e{w}a{w}s{w}e"

    call credits from _call_credits_1
    return

label credits:
    play music "audio/Outro.mp3" fadein 3.0
    $ credits_speed = 25 #scrolling speed in seconds
    scene ratman #replace this with a fancy background
    with dissolve
    #show theend:
    #    yanchor 0.5 ypos 0.5
    #    xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(3)
    #hide theend
    show cred at Move((0.5, 2.5), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(21)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide thanks
    return

init python:
    credits = ('Story', 'Pleco & AtomicPsythe'), ('Programming', 'WevDrazoon, PlagueBabeZ & Allie'), ('Backgrounds', 'Allie'), ('Character Sprites', 'KedLead'), ('Item Sprites', 'AtomicPsythe'), ('Music', 'Marsh')
    credits_s = "{size=80}Made for the Pompous Trash GameJam\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\7.4.0.1167" #Don't forget to set this to your Ren'py version

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, font="ShareTechMono-Regular.ttf", text_align=0.5)
    #image theend = Text("{size=80}Made for the Pompous Trash GameJam", text_align=0.5)
    image thanks = Text("{size=80}Congrats, player! Could you have done things differently, though?", text_align=0.5)
