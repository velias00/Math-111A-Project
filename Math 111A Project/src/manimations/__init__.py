from manim import *

class demo(Scene):
    def construct(self):
        t = Text("Hello")
        self.play(Write(t))
        self.wait(3)

from manim import *
from manimusic import *

class ManiMusicStaffExample(Scene):
    def construct(self):
        # Creates a default treble (G-clef) staff
        treble_staff = Staff()
        
        # Optional: specify clef ("G", "F", or "C") and size
        bass_staff = Staff(clef="F")
        
        staves = VGroup(treble_staff, bass_staff).arrange(DOWN, buff=1.5)
        self.play(Create(staves))
        self.wait()