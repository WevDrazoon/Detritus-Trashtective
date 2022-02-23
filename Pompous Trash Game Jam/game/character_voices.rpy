
init python:
    def raz_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Raz Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def cherry_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Cherry Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def belle_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Belle Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def erret_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Erret Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def eye_guy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Eye Guy Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def g_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/3 Moles Voices.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def jm_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Mole 1 Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def nm_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Mole 2 Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def dm_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Mole 3 Voice.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
