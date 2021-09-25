# CHARACTERS
define c = Character("Celeste")
define l = Character("Levi")
define e = Character("Sir Elijah")
define n = Character("Noah")
define f = Character("Father")
define em = Character("Empress Mirelle")
define el = Character("Emperor Lucius")

# SPRITE IMAGES
$ celesteOutfit = 'normal'
$ celesteMood = 'neutral'
image celeste = "images/sprites/celeste"
image levi = "images/sprites/levi"
image elijah = "images/sprites/elijah"
image noah = "image/sprites/noah"

# BACKGROUND IMAGES
image chapel = "images/backgrounds/chapel day.png"
image white = "#fff"

#SPRITE POSITIONS
transform left:
    xalign 0.05
    xzoom 1
transform right:
    xalign 0.95
    xzoom -1
transform flipLeft:
    xalign 0.05
    xzoom -1
transform flipRight:
    xalign 0.95
    xzoom 1
transform flipCenter:
    xzoom -1.0
    xalign 0.5
transform offscreenleft:
    xalign -0.5
transform offscreenleftFlip:
    xzoom -1
    xalign -0.5
transform offscreenright:
    xalign 1.5
transform offscreenrightFlip:
    xzoom -1
    xalign 1.5

init python:
    config.searchpath.extend(["game/audio", "game/images/backgrounds"])

    # SHAKE EFFECT : Shake(position, duration, max distance)
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [self.anchors.get(i,i) for i in start] # central position
            self.dist = dist                                    # max distance from start in pixels
            self.child = child
        def __call__(self, t, sizes):
            # turns float to int
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [fti(a,b) for a,b in zip(self.start, sizes)]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)
    Shake = renpy.curry(_Shake)

    # FLASH EFFECTS
    sshake = Shake((0, 0, 0, 0), 0.5, dist=15)      # for getting hit
    flash = Fade(0.1, 0.0, 0.25, color="#fff")      # flashes white
    pain = ComposeTransition(sshake, after=flash)    # pain flash
    fade = Fade(0.25, 0.5, 0.25, color="000")

    # STORY TRACKERS
    hideWithElijah = True;      # false if you stay put in ch1 s10



label start:
    jump ch1_s1
