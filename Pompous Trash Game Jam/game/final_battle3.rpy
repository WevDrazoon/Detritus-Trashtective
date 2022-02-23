screen simple_stats_screen3:
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

label battle_mole_3:
    play music "audio/Intense Fightin Time.mp3" fadein 3.0
    scene sewer
    show incel:
        xalign 0.9
        yalign 0
    show raz:
        xalign -0.2
        yalign 0
    nm "Alright, big mouth, show me what you can do.{w} I think you can do absolutely nothing."
    nm "If you truly believe that we're to blame for all of the ruckus goin' on up there,"
    nm "Then lay out all the facts for us, before we destroy you."
    show screen simple_stats_screen3
    $ x = 10
    menu:
        "Cherry got kidnapped at..."
        "The Musky Mug":
            r "She was kidnapped at umm...{w} her workplace, the Musky Mug."
            r "I think..."
            r "Well, anyways, it was somewhere."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Chez Pu Belle":
            r "After Cherry had arrived at Chez Pu Belle for our date,"
            r "She was caught off guard and the culprits took her hostage when no one was looking."
        "Placeholder Avenue":
            r "She was kidnapped at umm...{w} Placeholder Avenue."
            r "I think..."
            r "Well, anyways, it was somewhere."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "The Kidnapping Zone":
            r "She was kidnapped at umm...{w} where she was kidnapped."
            nm "Are you serious?"
            r "Well, it was worth a shot."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending

    if raz_ep <= 0:
        nm "I see we're wasting our time here."
        jump bad_ending

    r "I arrived at the restaurant where we were supposed to have our date."
    r "I assumed that she was late,{w} or that I came early, but I was very wrong."
    r "After a while, I got impatient and started looking and asking around to see if she had been there before I came."
    menu:
        "Cherry had definitely been there, because of the..."
        "Newspaper Clippings":
            r "I had found her newspaper clippin's on the seat opposite to mine, showin' that she was in fact there recently."
        "Footprints":
            r "The bare footprints I saw at the restaurant."
            nm "Doesn't your girlfriend dearest have prosthetics?"
            r "Ack-{w} I{w} I was just testing you! Yea! That's it!"
            nm "SHE IS LITERALLY RIGHT HERE."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Reserved Table":
            r "Well, we took the time to reserve a table and all."
            r "She should've been there, for sure!"
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Burrito":
            r "The burritos look so good."
            r "She totally wouldn't just miss the date!"
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending



    r "Turns out, her \"co-workers\" had dragged her out of the restaurant."
    menu:
        "This was witnessed by..."
        "Belle":
            r "Belle being the owner of the restaurant, would never miss a thing."
        "Cherry":
            r "Uhh...{w} Cherry herself would know for certain."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Erret":
            r "Erret knows! Well, I'm not sure how he would've known."
            r "But he's a smart guy..."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Queen Trashabeth XIV":
            r "The Queen Trashabeth XIV herself told me in a dream!"
            nm "You betas really do have a screw loose."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending


    r "The next evident step was to find these so-called \"co-workers\" at The Musky Mug."

    if eye_guy_snack:
        r "Once there, I had to go get some food for a strange person who promised information, and returned to Chez Pu Belle."
        r "In fact, I had even met {b}you{/b}, acting all creepy and gross."
        r "When I returned, the Eye Guy turned out to be completely useless."
        r "However, I did find locker keys on the counter."

    else:
        r "There, I met Cherry's boss, Erret."
        r "He didn't have a clue about the \"surprise shift\" or the \"co-workers\""
        r "In fact, he had no clue about the whole thing."
        r "He gave me the keys to the locker room, and so I went and investigated further."

    r "It was there that I figured out where you were hiding."
    menu:
        "The hideout was well-marked in the..."
        "Wanted Poster":
            r "The wanted poster for a missing coat had the information right there. Wait, no... that doesn't make sense."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Menu":
            r "The menu had the information right there. Wait, no... that doesn't make sense."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Conspiracy Board":
            r "It was all thanks to Cherry's conspiracy board and excellent sleuthing skills."
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending
        "Flashing Red Neon Arrows That Say \"Sus Hideout Here\"":
            r "I think I saw arrows pointing here."
            r "Maybe..."
            $ raz_ep -= x
            if raz_ep <= 0:
                nm "I see we're wasting our time here."
                jump bad_ending

    r "That's how I made my way here."
    r "All the clues left behind a trail. I needed only to follow it, and it led me straight to you."
    r "You three devious moles are the culprits behind Cherry's abduction!"
    jump good_ending
