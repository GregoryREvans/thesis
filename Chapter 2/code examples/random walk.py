import abjad
from random import seed
from random import random
seed(3)
random_walk = list()
random_walk.append(-1 if random() < 0.5 else 1)
for i in range(1, 64):
	movement = -1 if random() < 0.5 else 1
	value = random_walk[i-1] + movement
	random_walk.append(value)
notes = [abjad.Note(x / 2.0, (1, 8)) for x in random_walk]
staff = abjad.Staff(notes)
abjad.show(staff)

# lilypond_file = abjad.LilyPondFile.new(
# music=staff,
# default_paper_size=('a5', 'portrait'),
# includes=['ekmel.ily', ],
# global_staff_size=16,
# )
#
# abjad.show(lilypond_file)
