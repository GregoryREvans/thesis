import abjad
import itertools
import os
import pathlib
import time
import abjadext.rmakers
from MusicMaker import MusicMaker
from AttachmentHandler import AttachmentHandler
from random import random
from random import seed

print('Interpreting file ...')

time_signatures = [
    abjad.TimeSignature(pair) for pair in [
        (5, 4), (2, 4), (4, 4), (3, 4), (4, 4), (4, 4),
        (4, 4), (4, 4), (5, 4), (5, 4), (3, 4), (3, 4),
        (4, 4), (4, 4), (5, 4), (5, 4), (3, 4), (3, 4),
        (2, 4), (3, 4), (4, 4), (3, 4), (4, 4), (3, 4),
        (5, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4),
        (4, 4), (5, 4), (4, 4), (3, 4), (5, 4), (5, 4),
        (5, 4), (5, 4), (4, 4), (4, 4), (5, 4), (5, 4),
        (4, 4), (4, 4), (3, 4), (4, 4), (4, 4), (3, 4),
        (5, 4),
    ]
]

bounds = abjad.mathtools.cumulative_sums([_.duration for _ in time_signatures])

def reduceMod3(rw):
    return [(x % 4) for x in rw]

def reduceMod5(rw):
    return [(x % 6) for x in rw]

def reduceMod7(rw):
    return [(x % 8) for x in rw]

def reduceMod9(rw):
    return [(x % 10) for x in rw]

def reduceMod11(rw):
    return [(x % 12) for x in rw]

def reduceMod13(rw):
    return [(x % 14) for x in rw]

def reduceMod15(rw):
    return [(x % 16) for x in rw]

seed(1)
flute_random_walk_one = []
flute_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = flute_random_walk_one[i-1] + movement
    flute_random_walk_one.append(value)
flute_random_walk_one = [abs(x) for x in flute_random_walk_one]
flute_chord_one = [8, 14, 23, 27, 28, 30, 37, 30, 28, 27, 23, 14, ]
flute_notes_one = [flute_chord_one[x] for x in reduceMod11(flute_random_walk_one)]

seed(2)
clarinet_random_walk_one = []
clarinet_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = clarinet_random_walk_one[i-1] + movement
    clarinet_random_walk_one.append(value)
clarinet_random_walk_one = [abs(x) for x in clarinet_random_walk_one]
clarinet_chord_one = [-3, 5, 8, 14, 23, 27, 23, 14, 8, 5, ]
clarinet_notes_one = [clarinet_chord_one[x] for x in reduceMod9(clarinet_random_walk_one)]

seed(3)
bassoon_random_walk_one = []
bassoon_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = bassoon_random_walk_one[i-1] + movement
    bassoon_random_walk_one.append(value)
bassoon_random_walk_one = [abs(x) for x in bassoon_random_walk_one]
bassoon_chord_one = [-24, -14, -3, 5, 8, 5, -3, -14, ]
bassoon_notes_one = [bassoon_chord_one[x] for x in reduceMod7(bassoon_random_walk_one)]

seed(4)
horn_random_walk_one = []
horn_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = horn_random_walk_one[i-1] + movement
    horn_random_walk_one.append(value)
horn_random_walk_one = [abs(x) for x in horn_random_walk_one]
horn_chord_one = [-24, -14, -3, 5, 8, 5, -3, -14, ]
horn_notes_one = [horn_chord_one[x] for x in reduceMod7(horn_random_walk_one)]

seed(5)
trumpet_random_walk_one = []
trumpet_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = trumpet_random_walk_one[i-1] + movement
    trumpet_random_walk_one.append(value)
trumpet_random_walk_one = [abs(x) for x in trumpet_random_walk_one]
trumpet_chord_one = [-3, 5, 8, 14, 23, 14, 8, 5, ]
trumpet_notes_one = [trumpet_chord_one[x] for x in reduceMod7(trumpet_random_walk_one)]

seed(6)
trombone_random_walk_one = []
trombone_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = trombone_random_walk_one[i-1] + movement
    trombone_random_walk_one.append(value)
trombone_random_walk_one = [abs(x) for x in trombone_random_walk_one]
trombone_chord_one = [-14, -3, 5, -3, ]
trombone_notes_one = [trombone_chord_one[x] for x in reduceMod3(trombone_random_walk_one)]

seed(7)
tuba_random_walk_one = []
tuba_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = tuba_random_walk_one[i-1] + movement
    tuba_random_walk_one.append(value)
tuba_random_walk_one = [abs(x) for x in tuba_random_walk_one]
tuba_chord_one = [-29, -24, -14, -3, 5, -3, -14, -24, ]
tuba_notes_one = [tuba_chord_one[x] for x in reduceMod7(tuba_random_walk_one)]

seed(8)
violin1_random_walk_one = []
violin1_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = violin1_random_walk_one[i-1] + movement
    violin1_random_walk_one.append(value)
violin1_random_walk_one = [abs(x) for x in violin1_random_walk_one]
violin1_chord_one = [-3, 5, 8, 14, 23, 27, 28, 30, 37, 30, 28, 27, 23, 14, 8, 5, ]
violin1_notes_one = [violin1_chord_one[x] for x in reduceMod15(violin1_random_walk_one)]

seed(9)
violin2_random_walk_one = []
violin2_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = violin2_random_walk_one[i-1] + movement
    violin2_random_walk_one.append(value)
violin2_random_walk_one = [abs(x) for x in violin2_random_walk_one]
violin2_chord_one = [-3, 5, 8, 14, 23, 27, 28, 27, 23, 14, 8, 5, ]
violin2_notes_one = [violin2_chord_one[x] for x in reduceMod11(violin2_random_walk_one)]

seed(10)
viola_random_walk_one = []
viola_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = viola_random_walk_one[i-1] + movement
    viola_random_walk_one.append(value)
viola_random_walk_one = [abs(x) for x in viola_random_walk_one]
viola_chord_one = [-3, 5, 8, 14, 23, 27, 28, 27, 23, 14, 8, 5, ]
viola_notes_one = [viola_chord_one[x] for x in reduceMod11(viola_random_walk_one)]

seed(11)
cello_random_walk_one = []
cello_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_one[i-1] + movement
    cello_random_walk_one.append(value)
cello_random_walk_one = [abs(x) for x in cello_random_walk_one]
cello_chord_one = [-24, -14, -3, 5, 8, 14, 8, 5, -3, -14]
cello_notes_one = [cello_chord_one[x] for x in reduceMod9(cello_random_walk_one)]

seed(12)
bass_random_walk_one = []
bass_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = bass_random_walk_one[i-1] + movement
    bass_random_walk_one.append(value)
bass_random_walk_one = [abs(x) for x in bass_random_walk_one]
bass_chord_one = [-29, -24, -14, -3, -14, -24, ]
bass_notes_one = [bass_chord_one[x] for x in reduceMod5(bass_random_walk_one)]

flute_scale = [30, 23, 5, 23, ]
clarinet_scale = [23, 5, ]
bassoon_scale = [-24, ]
horn_scale = [5, ]
trumpet_scale = [23, ]
trombone_scale = [5, ]
tuba_scale = [-24, ]
violin1_scale = [30, 29.5, 29, 28.5, 28, 27.5, 27, 26.5, 26, 25.5, 25, 24.5, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20.5, 20, 19.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, ]
violin2_scale = [19, 18.5, 18, 17.5, 17, 16.5, 16, 15.5, 15, 14.5, 14, 13.5, 13, 12.5, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, ]
viola_scale = [8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2, -2.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, ]
cello_scale = [-3, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10, -10.5, -11, -11.5, -12, -12.5 -13, -13.5 -14, -13.5, -13, -12.5, -12, -11.5, -11, -10.5, -10, -9.5, -9, -8.5, -8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, ]
bass_scale = [-14, -14.5, -15, -15.5, -16, -16.5, -17, -17.5, -18, -18.5, -19, -19.5, -20, -20.5, -21, -21.5, -22, -22.5, -23, -23.5, -24, -24.5, -25, -24.5, -24, -23.5, -23, -22.5, -22, -21.5, -21, -20.5, -20, -19.5, -19, -18.5, -18, -17.5, -17, -16.5, -16, -15.5, -15, -14.5, ]

seed(1)
flute_random_walk_two = []
flute_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = flute_random_walk_two[i-1] + movement
    flute_random_walk_two.append(value)
flute_random_walk_two = [abs(x) for x in flute_random_walk_two]
flute_chord_two = [10, 16, 23, 25, 26, 25, 23, 16, ]
flute_notes_two = [flute_chord_two[x] for x in reduceMod7(flute_random_walk_two)]

seed(2)
clarinet_random_walk_two = []
clarinet_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = clarinet_random_walk_two[i-1] + movement
    clarinet_random_walk_two.append(value)
clarinet_random_walk_two = [abs(x) for x in clarinet_random_walk_two]
clarinet_chord_two = [-5, 5, 10, 16, 23, 25, 26, 25, 23, 16, 10, 5, ]
clarinet_notes_two = [clarinet_chord_two[x] for x in reduceMod11(clarinet_random_walk_two)]

seed(3)
bassoon_random_walk_two = []
bassoon_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = bassoon_random_walk_two[i-1] + movement
    bassoon_random_walk_two.append(value)
bassoon_random_walk_two = [abs(x) for x in bassoon_random_walk_two]
bassoon_chord_two = [-24, -16, -5, 5, -5, -16, ]
bassoon_notes_two = [bassoon_chord_two[x] for x in reduceMod5(bassoon_random_walk_two)]

seed(4)
horn_random_walk_two = []
horn_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = horn_random_walk_two[i-1] + movement
    horn_random_walk_two.append(value)
horn_random_walk_two = [abs(x) for x in horn_random_walk_two]
horn_chord_two = [-16, -5, 5, 10, 5, -5, ]
horn_notes_two = [horn_chord_two[x] for x in reduceMod5(horn_random_walk_two)]

seed(5)
trumpet_random_walk_two = []
trumpet_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = trumpet_random_walk_two[i-1] + movement
    trumpet_random_walk_two.append(value)
trumpet_random_walk_two = [abs(x) for x in trumpet_random_walk_two]
trumpet_chord_two = [-5, 5, 10, 16, 23, 16, 10, 5, ]
trumpet_notes_two = [trumpet_chord_two[x] for x in reduceMod7(trumpet_random_walk_two)]

seed(6)
trombone_random_walk_two = []
trombone_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = trombone_random_walk_two[i-1] + movement
    trombone_random_walk_two.append(value)
trombone_random_walk_two = [abs(x) for x in trombone_random_walk_two]
trombone_chord_two = [-16, -5, 5, -5, ]
trombone_notes_two = [trombone_chord_two[x] for x in reduceMod3(trombone_random_walk_two)]

seed(7)
tuba_random_walk_two = []
tuba_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = tuba_random_walk_two[i-1] + movement
    tuba_random_walk_two.append(value)
tuba_random_walk_two = [abs(x) for x in tuba_random_walk_two]
tuba_chord_two = [-27, -24, -16, -5, -16, -24, ]
tuba_notes_two = [tuba_chord_two[x] for x in reduceMod5(tuba_random_walk_two)]

seed(8)
violin1_random_walk_two = []
violin1_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = violin1_random_walk_two[i-1] + movement
    violin1_random_walk_two.append(value)
violin1_random_walk_two = [abs(x) for x in violin1_random_walk_two]
violin1_chord_two = [-5, 5, 10, 16, 23, 25, 26, 30, 38, 30, 26, 25, 23, 16, 10, 5, ]
violin1_notes_two = [violin1_chord_two[x] for x in reduceMod15(violin1_random_walk_two)]

seed(9)
violin2_random_walk_two = []
violin2_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = violin2_random_walk_two[i-1] + movement
    violin2_random_walk_two.append(value)
violin2_random_walk_two = [abs(x) for x in violin2_random_walk_two]
violin2_chord_two = [-5, 5, 10, 16, 23, 25, 26, 25, 23, 16, 10, 5, ]
violin2_notes_two = [violin2_chord_two[x] for x in reduceMod11(violin2_random_walk_two)]

seed(10)
viola_random_walk_two = []
viola_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = viola_random_walk_two[i-1] + movement
    viola_random_walk_two.append(value)
viola_random_walk_two = [abs(x) for x in viola_random_walk_two]
viola_chord_two = [-5, 5, 10, 16, 23, 16, 10, 5, ]
viola_notes_two = [viola_chord_two[x] for x in reduceMod7(viola_random_walk_two)]

seed(11)
cello_random_walk_two = []
cello_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_two[i-1] + movement
    cello_random_walk_two.append(value)
cello_random_walk_two = [abs(x) for x in cello_random_walk_two]
cello_chord_two = [-24, -16, -5, 5, 10, 16, 23, 16, 10, 5, -5, -16]
cello_notes_two = [cello_chord_two[x] for x in reduceMod11(cello_random_walk_two)]

seed(12)
bass_random_walk_two = []
bass_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = bass_random_walk_two[i-1] + movement
    bass_random_walk_two.append(value)
bass_random_walk_two = [abs(x) for x in bass_random_walk_two]
bass_chord_two = [-27, -24, -16, -5, -16, -24, ]
bass_notes_two = [bass_chord_two[x] for x in reduceMod5(bass_random_walk_two)]

rmaker_one = abjadext.rmakers.NoteRhythmMaker()

rmaker_two = abjadext.rmakers.EvenDivisionRhythmMaker(
    denominators=[16, 16, 8, 16, 4, 16, 8],
    extra_counts_per_division=[0, 1, 0, 0, -1, 0, 1, -1],
    burnish_specifier=abjadext.rmakers.BurnishSpecifier(
        left_classes=[abjad.Rest],
        left_counts=[1],
        right_classes=[abjad.Rest],
        right_counts=[1],
        outer_divisions_only=True,
        ),
    tuplet_specifier=abjadext.rmakers.TupletSpecifier(
        trivialize=True,
        extract_trivial=True,
        rewrite_rest_filled=True,
        ),
    )

rmaker_three = abjadext.rmakers.TaleaRhythmMaker(
    talea=abjadext.rmakers.Talea(
        counts=[1, 1, 1, 2, 1, 3, 1, 4, 5],
        denominator=16,
        ),
    beam_specifier=abjadext.rmakers.BeamSpecifier(
        beam_divisions_together=True,
        beam_rests=False,
        ),
    extra_counts_per_division=[0, 1, 0, -1],
    burnish_specifier=abjadext.rmakers.BurnishSpecifier(
        left_classes=[abjad.Note, abjad.Rest],
        left_counts=[1, 0, 1],
        ),
    tuplet_specifier=abjadext.rmakers.TupletSpecifier(
        trivialize=True,
        extract_trivial=True,
        rewrite_rest_filled=True,
        ),
    )

attachment_handler_one = AttachmentHandler(
    starting_dynamic='p',
    ending_dynamic='mp',
    hairpin_indicator='--',
    articulation='accent',
)

attachment_handler_two = AttachmentHandler(
    starting_dynamic='fff',
    ending_dynamic='mf',
    hairpin_indicator='>',
    articulation='tenuto',
)

attachment_handler_three = AttachmentHandler(
    starting_dynamic='mp',
    ending_dynamic='ff',
    hairpin_indicator='<|',
    articulation='',
)

#####oboe#####
flutemusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=flute_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
flutemusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=flute_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
flutemusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=flute_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####violin1#####
violin1musicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=violin1_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
violin1musicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=violin1_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
violin1musicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=violin1_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####trumpet#####
trumpetmusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=trumpet_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
trumpetmusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=trumpet_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
trumpetmusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=trumpet_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####clarinet#####
clarinetmusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=clarinet_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
clarinetmusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=clarinet_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
clarinetmusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=clarinet_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####violin2#####
violin2musicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=violin2_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
violin2musicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=violin2_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
violin2musicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=violin2_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####viola#####
violamusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=viola_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
violamusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=viola_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
violamusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=viola_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####bassoon#####
bassoonmusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=bassoon_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
bassoonmusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=bassoon_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
bassoonmusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=bassoon_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####trombone#####
trombonemusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=trombone_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
trombonemusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=trombone_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
trombonemusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=trombone_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####cello#####
cellomusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=cello_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
cellomusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=cello_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
cellomusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=cello_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####horn#####
hornmusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=horn_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
hornmusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=horn_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
hornmusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=horn_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####tuba#####
tubamusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=tuba_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
tubamusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=tuba_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
tubamusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=tuba_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####bass#####
bassmusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=bass_scale,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
bassmusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=bass_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
bassmusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=bass_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_three,
)

silence_maker = abjadext.rmakers.NoteRhythmMaker(
    division_masks=[
        abjadext.rmakers.SilenceMask(
            pattern=abjad.index([0], 1),
            ),
        ],
    )

class MusicSpecifier:

    def __init__(self, music_maker, voice_name):
        self.music_maker = music_maker
        self.voice_name = voice_name

print('Collecting timespans and rmakers ...')
###group one###
voice_1_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 1',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(9, 4), (10, 4), flutemusicmaker_one],
        [(15, 4), (18, 4), flutemusicmaker_two],
        [(22, 4), (25, 4), flutemusicmaker_three],
        [(27, 4), (30, 4), flutemusicmaker_one],
        [(30, 4), (32, 4), flutemusicmaker_one],
        [(35, 4), (39, 4), flutemusicmaker_two],
        [(42, 4), (43, 4), flutemusicmaker_three],
        [(43, 4), (44, 4), flutemusicmaker_three],
        [(45, 4), (46, 4), flutemusicmaker_one],
        [(46, 4), (50, 4), flutemusicmaker_one],
        [(54, 4), (57, 4), flutemusicmaker_two],
        [(59, 4), (60, 4), flutemusicmaker_three],
        [(65, 4), (67, 4), flutemusicmaker_one],
        [(67, 4), (69, 4), flutemusicmaker_one],
        [(70, 4), (72, 4), flutemusicmaker_two],
        [(72, 4), (75, 4), flutemusicmaker_two],
        [(76, 4), (78, 4), flutemusicmaker_three],
        [(81, 4), (82, 4), flutemusicmaker_one],
        [(82, 4), (85, 4), flutemusicmaker_one],
        [(90, 4), (91, 4), flutemusicmaker_two],
        [(93, 4), (94, 4), flutemusicmaker_three],
        [(94, 4), (96, 4), flutemusicmaker_three],
        [(100, 4), (104, 4), flutemusicmaker_one],
        [(104, 4), (105, 4), flutemusicmaker_one],
        [(106, 4), (107, 4), flutemusicmaker_two],
        [(107, 4), (108, 4), flutemusicmaker_two],
        [(111, 4), (114, 4), flutemusicmaker_one],
        [(114, 4), (115, 4), flutemusicmaker_one],
        [(116, 4), (119, 4), flutemusicmaker_one],
        [(119, 4), (120, 4), flutemusicmaker_one],
        [(121, 4), (123, 4), flutemusicmaker_one],
        [(123, 4), (125, 4), flutemusicmaker_one],
        [(126, 4), (131, 4), flutemusicmaker_two],
        [(131, 4), (133, 4), flutemusicmaker_two],
        [(136, 4), (141, 4), flutemusicmaker_two],
        [(148, 4), (150, 4), flutemusicmaker_two],
        [(150, 4), (153, 4), flutemusicmaker_three],
        [(155, 4), (159, 4), flutemusicmaker_three],
        [(162, 4), (164, 4), flutemusicmaker_three],
        [(168, 4), (171, 4), flutemusicmaker_three],
        [(173, 4), (175, 4), flutemusicmaker_three],
        [(175, 4), (177, 4), flutemusicmaker_three],
        [(180, 4), (182, 4), flutemusicmaker_three],
        [(186, 4), (190, 4), flutemusicmaker_three],
        [(190, 4), (191, 4), silence_maker],
    ]
])

voice_5_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 5',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(9, 4), (10, 4), trumpetmusicmaker_one],
        [(14, 4), (18, 4), trumpetmusicmaker_two],
        [(23, 4), (25, 4), trumpetmusicmaker_three],
        [(27, 4), (30, 4), trumpetmusicmaker_one],
        [(30, 4), (32, 4), trumpetmusicmaker_one],
        [(35, 4), (39, 4), trumpetmusicmaker_two],
        [(42, 4), (43, 4), trumpetmusicmaker_three],
        [(43, 4), (44, 4), trumpetmusicmaker_three],
        [(45, 4), (46, 4), trumpetmusicmaker_one],
        [(46, 4), (50, 4), trumpetmusicmaker_one],
        [(54, 4), (57, 4), trumpetmusicmaker_two],
        [(59, 4), (60, 4), trumpetmusicmaker_three],
        [(65, 4), (67, 4), trumpetmusicmaker_one],
        [(67, 4), (69, 4), trumpetmusicmaker_one],
        [(70, 4), (72, 4), trumpetmusicmaker_two],
        [(72, 4), (75, 4), trumpetmusicmaker_two],
        [(76, 4), (78, 4), trumpetmusicmaker_three],
        [(81, 4), (82, 4), trumpetmusicmaker_one],
        [(82, 4), (85, 4), trumpetmusicmaker_one],
        [(90, 4), (91, 4), trumpetmusicmaker_two],
        [(93, 4), (94, 4), trumpetmusicmaker_three],
        [(94, 4), (96, 4), trumpetmusicmaker_three],
        [(100, 4), (104, 4), trumpetmusicmaker_one],
        [(104, 4), (105, 4), trumpetmusicmaker_one],
        [(106, 4), (107, 4), trumpetmusicmaker_two],
        [(107, 4), (108, 4), trumpetmusicmaker_two],
        [(111, 4), (114, 4), trumpetmusicmaker_one],
        [(114, 4), (115, 4), trumpetmusicmaker_one],
        [(116, 4), (119, 4), trumpetmusicmaker_one],
        [(119, 4), (120, 4), trumpetmusicmaker_one],
        [(121, 4), (123, 4), trumpetmusicmaker_one],
        [(123, 4), (125, 4), trumpetmusicmaker_one],
        [(126, 4), (131, 4), trumpetmusicmaker_two],
        [(131, 4), (133, 4), trumpetmusicmaker_two],
        [(136, 4), (141, 4), trumpetmusicmaker_two],
        [(148, 4), (150, 4), trumpetmusicmaker_two],
        [(150, 4), (154, 4), trumpetmusicmaker_three],
        [(157, 4), (159, 4), trumpetmusicmaker_three],
        [(163, 4), (164, 4), trumpetmusicmaker_three],
        [(164, 4), (166, 4), trumpetmusicmaker_three],
        [(168, 4), (172, 4), trumpetmusicmaker_three],
        [(175, 4), (177, 4), trumpetmusicmaker_three],
        [(181, 4), (183, 4), trumpetmusicmaker_three],
        [(183, 4), (184, 4), trumpetmusicmaker_three],
        [(186, 4), (190, 4), trumpetmusicmaker_three],
    ]
])

voice_8_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 8',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(9, 4), (10, 4), violin1musicmaker_one],
        [(14, 4), (18, 4), violin1musicmaker_two],
        [(22, 4), (25, 4), violin1musicmaker_three],
        [(27, 4), (30, 4), violin1musicmaker_one],
        [(35, 4), (39, 4), violin1musicmaker_two],
        [(42, 4), (43, 4), violin1musicmaker_three],
        [(43, 4), (44, 4), violin1musicmaker_three],
        [(45, 4), (46, 4), violin1musicmaker_one],
        [(46, 4), (50, 4), violin1musicmaker_one],
        [(54, 4), (57, 4), violin1musicmaker_two],
        [(59, 4), (60, 4), violin1musicmaker_three],
        [(65, 4), (67, 4), violin1musicmaker_one],
        [(67, 4), (69, 4), violin1musicmaker_one],
        [(70, 4), (72, 4), violin1musicmaker_two],
        [(72, 4), (75, 4), violin1musicmaker_two],
        [(76, 4), (78, 4), violin1musicmaker_three],
        [(81, 4), (82, 4), violin1musicmaker_one],
        [(82, 4), (85, 4), violin1musicmaker_one],
        [(90, 4), (91, 4), violin1musicmaker_two],
        [(93, 4), (94, 4), violin1musicmaker_three],
        [(94, 4), (96, 4), violin1musicmaker_three],
        [(100, 4), (104, 4), violin1musicmaker_one],
        [(104, 4), (105, 4), violin1musicmaker_one],
        [(106, 4), (107, 4), violin1musicmaker_two],
        [(107, 4), (108, 4), violin1musicmaker_two],
        [(111, 4), (114, 4), violin1musicmaker_one],
        [(114, 4), (115, 4), violin1musicmaker_one],
        [(116, 4), (119, 4), violin1musicmaker_one],
        [(119, 4), (120, 4), violin1musicmaker_one],
        [(121, 4), (123, 4), violin1musicmaker_one],
        [(123, 4), (125, 4), violin1musicmaker_one],
        [(126, 4), (131, 4), violin1musicmaker_two],
        [(131, 4), (133, 4), violin1musicmaker_two],
        [(136, 4), (141, 4), violin1musicmaker_two],
        [(148, 4), (150, 4), violin1musicmaker_two],
        [(150, 4), (152, 4), violin1musicmaker_three],
        [(156, 4), (159, 4), violin1musicmaker_three],
        [(161, 4), (164, 4), violin1musicmaker_three],
        [(164, 4), (165, 4), violin1musicmaker_three],
        [(168, 4), (170, 4), violin1musicmaker_three],
        [(174, 4), (175, 4), violin1musicmaker_three],
        [(175, 4), (177, 4), violin1musicmaker_three],
        [(179, 4), (183, 4), violin1musicmaker_three],
        [(186, 4), (190, 4), violin1musicmaker_three],
    ]
])

###group two###
voice_2_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 2',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(2, 4), (5, 4), clarinetmusicmaker_one],
        [(10, 4), (11, 4), clarinetmusicmaker_two],
        [(11, 4), (13, 4), clarinetmusicmaker_two],
        [(16, 4), (18, 4), clarinetmusicmaker_three],
        [(21, 4), (22, 4), clarinetmusicmaker_one],
        [(22, 4), (25, 4), clarinetmusicmaker_one],
        [(35, 4), (40, 4), clarinetmusicmaker_one],
        [(44, 4), (46, 4), clarinetmusicmaker_two],
        [(46, 4), (47, 4), clarinetmusicmaker_two],
        [(49, 4), (50, 4), clarinetmusicmaker_three],
        [(55, 4), (59, 4), clarinetmusicmaker_one],
        [(62, 4), (64, 4), clarinetmusicmaker_two],
        [(65, 4), (67, 4), clarinetmusicmaker_three],
        [(67, 4), (70, 4), clarinetmusicmaker_three],
        [(70, 4), (71, 4), clarinetmusicmaker_three],
        [(73, 4), (75, 4), clarinetmusicmaker_two],
        [(75, 4), (76, 4), clarinetmusicmaker_two],
        [(80, 4), (82, 4), clarinetmusicmaker_one],
        [(82, 4), (85, 4), clarinetmusicmaker_one],
        [(86, 4), (88, 4), clarinetmusicmaker_two],
        [(91, 4), (94, 4), clarinetmusicmaker_three],
        [(94, 4), (95, 4), clarinetmusicmaker_three],
        [(100, 4), (101, 4), clarinetmusicmaker_two],
        [(103, 4), (104, 4), clarinetmusicmaker_one],
        [(104, 4), (106, 4), clarinetmusicmaker_one],
        [(110, 4), (114, 4), clarinetmusicmaker_one],
        [(115, 4), (119, 4), clarinetmusicmaker_one],
        [(120, 4), (123, 4), clarinetmusicmaker_one],
        [(123, 4), (124, 4), clarinetmusicmaker_one],
        [(125, 4), (126, 4), clarinetmusicmaker_two],
        [(129, 4), (131, 4), clarinetmusicmaker_two],
        [(131, 4), (134, 4), clarinetmusicmaker_two],
        [(141, 4), (144, 4), clarinetmusicmaker_two],
        [(149, 4), (150, 4), clarinetmusicmaker_two],
        [(155, 4), (159, 4), clarinetmusicmaker_three],
        [(162, 4), (164, 4), clarinetmusicmaker_three],
        [(165, 4), (168, 4), clarinetmusicmaker_three],
        [(168, 4), (170, 4), clarinetmusicmaker_three],
        [(174, 4), (175, 4), clarinetmusicmaker_three],
        [(175, 4), (177, 4), clarinetmusicmaker_three],
        [(179, 4), (180, 4), clarinetmusicmaker_three],
        [(185, 4), (186, 4), clarinetmusicmaker_three],
        [(186, 4), (190, 4), clarinetmusicmaker_three],
    ]
])

voice_9_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 9',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(2, 4), (5, 4), violin2musicmaker_one],
        [(9, 4), (11, 4), violin2musicmaker_two],
        [(11, 4), (13, 4), violin2musicmaker_two],
        [(16, 4), (18, 4), violin2musicmaker_three],
        [(21, 4), (22, 4), violin2musicmaker_one],
        [(22, 4), (23, 4), violin2musicmaker_one],
        [(35, 4), (40, 4), violin2musicmaker_one],
        [(44, 4), (46, 4), violin2musicmaker_two],
        [(46, 4), (47, 4), violin2musicmaker_two],
        [(49, 4), (50, 4), violin2musicmaker_three],
        [(55, 4), (59, 4), violin2musicmaker_one],
        [(62, 4), (64, 4), violin2musicmaker_two],
        [(65, 4), (67, 4), violin2musicmaker_three],
        [(67, 4), (70, 4), violin2musicmaker_three],
        [(70, 4), (71, 4), violin2musicmaker_three],
        [(73, 4), (75, 4), violin2musicmaker_two],
        [(75, 4), (76, 4), violin2musicmaker_two],
        [(80, 4), (82, 4), violin2musicmaker_one],
        [(82, 4), (85, 4), violin2musicmaker_one],
        [(86, 4), (88, 4), violin2musicmaker_two],
        [(91, 4), (94, 4), violin2musicmaker_three],
        [(94, 4), (95, 4), violin2musicmaker_three],
        [(100, 4), (101, 4), violin2musicmaker_two],
        [(103, 4), (104, 4), violin2musicmaker_one],
        [(104, 4), (106, 4), violin2musicmaker_one],
        [(110, 4), (114, 4), violin2musicmaker_one],
        [(115, 4), (119, 4), violin2musicmaker_one],
        [(120, 4), (123, 4), violin2musicmaker_one],
        [(123, 4), (124, 4), violin2musicmaker_one],
        [(125, 4), (126, 4), violin2musicmaker_two],
        [(129, 4), (131, 4), violin2musicmaker_two],
        [(131, 4), (134, 4), violin2musicmaker_two],
        [(141, 4), (144, 4), violin2musicmaker_two],
        [(149, 4), (150, 4), violin2musicmaker_two],
        [(154, 4), (157, 4), violin2musicmaker_three],
        [(159, 4), (160, 4), violin2musicmaker_three],
        [(165, 4), (168, 4), violin2musicmaker_three],
        [(168, 4), (169, 4), violin2musicmaker_three],
        [(172, 4), (174, 4), violin2musicmaker_three],
        [(175, 4), (179, 4), violin2musicmaker_three],
        [(179, 4), (180, 4), violin2musicmaker_three],
        [(184, 4), (186, 4), violin2musicmaker_three],
        [(186, 4), (190, 4), violin2musicmaker_three],
    ]
])

voice_10_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 10',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(2, 4), (5, 4), violamusicmaker_one],
        [(9, 4), (11, 4), violamusicmaker_two],
        [(11, 4), (13, 4), violamusicmaker_two],
        [(17, 4), (18, 4), violamusicmaker_three],
        [(21, 4), (22, 4), violamusicmaker_one],
        [(22, 4), (25, 4), violamusicmaker_one],
        [(29, 4), (30, 4), violamusicmaker_two],
        [(30, 4), (32, 4), violamusicmaker_two],
        [(35, 4), (40, 4), violamusicmaker_one],
        [(44, 4), (46, 4), violamusicmaker_two],
        [(46, 4), (47, 4), violamusicmaker_two],
        [(49, 4), (50, 4), violamusicmaker_three],
        [(55, 4), (59, 4), violamusicmaker_one],
        [(62, 4), (64, 4), violamusicmaker_two],
        [(65, 4), (67, 4), violamusicmaker_three],
        [(67, 4), (70, 4), violamusicmaker_three],
        [(70, 4), (71, 4), violamusicmaker_three],
        [(73, 4), (75, 4), violamusicmaker_two],
        [(75, 4), (76, 4), violamusicmaker_two],
        [(80, 4), (82, 4), violamusicmaker_one],
        [(82, 4), (85, 4), violamusicmaker_one],
        [(86, 4), (88, 4), violamusicmaker_two],
        [(91, 4), (94, 4), violamusicmaker_three],
        [(94, 4), (95, 4), violamusicmaker_three],
        [(100, 4), (101, 4), violamusicmaker_two],
        [(103, 4), (104, 4), violamusicmaker_one],
        [(104, 4), (106, 4), violamusicmaker_one],
        [(110, 4), (114, 4), violamusicmaker_one],
        [(115, 4), (119, 4), violamusicmaker_one],
        [(120, 4), (123, 4), violamusicmaker_one],
        [(123, 4), (124, 4), violamusicmaker_one],
        [(125, 4), (126, 4), violamusicmaker_two],
        [(129, 4), (131, 4), violamusicmaker_two],
        [(131, 4), (134, 4), violamusicmaker_two],
        [(141, 4), (144, 4), violamusicmaker_two],
        [(149, 4), (150, 4), violamusicmaker_two],
        [(153, 4), (154, 4), violamusicmaker_three],
        [(154, 4), (155, 4), violamusicmaker_three],
        [(156, 4), (159, 4), violamusicmaker_three],
        [(159, 4), (161, 4), violamusicmaker_three],
        [(165, 4), (168, 4), violamusicmaker_three],
        [(170, 4), (171, 4), violamusicmaker_three],
        [(176, 4), (179, 4), violamusicmaker_three],
        [(179, 4), (180, 4), violamusicmaker_three],
        [(183, 4), (185, 4), violamusicmaker_three],
        [(186, 4), (190, 4), violamusicmaker_three],
    ]
])

###group three###
voice_3_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 3',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(7, 4), (11, 4), bassoonmusicmaker_one],
        [(15, 4), (16, 4), bassoonmusicmaker_two],
        [(19, 4), (22, 4), bassoonmusicmaker_three],
        [(22, 4), (23, 4), bassoonmusicmaker_three],
        [(27, 4), (30, 4), bassoonmusicmaker_one],
        [(32, 4), (35, 4), bassoonmusicmaker_two],
        [(35, 4), (36, 4), bassoonmusicmaker_three],
        [(37, 4), (40, 4), bassoonmusicmaker_two],
        [(40, 4), (42, 4), bassoonmusicmaker_two],
        [(46, 4), (49, 4), bassoonmusicmaker_one],
        [(51, 4), (52, 4), bassoonmusicmaker_three],
        [(57, 4), (59, 4), bassoonmusicmaker_two],
        [(59, 4), (61, 4), bassoonmusicmaker_two],
        [(64, 4), (66, 4), bassoonmusicmaker_one],
        [(67, 4), (70, 4), bassoonmusicmaker_three],
        [(70, 4), (72, 4), bassoonmusicmaker_one],
        [(72, 4), (73, 4), bassoonmusicmaker_one],
        [(77, 4), (79, 4), bassoonmusicmaker_two],
        [(79, 4), (82, 4), bassoonmusicmaker_two],
        [(83, 4), (85, 4), bassoonmusicmaker_three],
        [(88, 4), (89, 4), bassoonmusicmaker_two],
        [(89, 4), (92, 4), bassoonmusicmaker_two],
        [(97, 4), (98, 4), bassoonmusicmaker_one],
        [(100, 4), (103, 4), bassoonmusicmaker_two],
        [(107, 4), (110, 4), bassoonmusicmaker_three],
        [(110, 4), (112, 4), bassoonmusicmaker_one],
        [(113, 4), (114, 4), bassoonmusicmaker_one],
        [(114, 4), (117, 4), bassoonmusicmaker_one],
        [(118, 4), (119, 4), bassoonmusicmaker_one],
        [(119, 4), (122, 4), bassoonmusicmaker_one],
        [(123, 4), (125, 4), bassoonmusicmaker_one],
        [(126, 4), (131, 4), bassoonmusicmaker_two],
        [(138, 4), (141, 4), bassoonmusicmaker_two],
        [(146, 4), (150, 4), bassoonmusicmaker_two],
        [(150, 4), (154, 4), bassoonmusicmaker_three],
        [(154, 4), (155, 4), bassoonmusicmaker_three],
        [(159, 4), (162, 4), bassoonmusicmaker_three],
        [(164, 4), (165, 4), bassoonmusicmaker_three],
        [(170, 4), (172, 4), bassoonmusicmaker_three],
        [(172, 4), (174, 4), bassoonmusicmaker_three],
        [(177, 4), (179, 4), bassoonmusicmaker_three],
        [(180, 4), (183, 4), bassoonmusicmaker_three],
        [(183, 4), (185, 4), bassoonmusicmaker_three],
        [(186, 4), (190, 4), bassoonmusicmaker_three],
    ]
])

voice_6_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 6',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(7, 4), (11, 4), trombonemusicmaker_one],
        [(14, 4), (16, 4), trombonemusicmaker_two],
        [(19, 4), (22, 4), trombonemusicmaker_three],
        [(22, 4), (23, 4), trombonemusicmaker_three],
        [(27, 4), (29, 4), trombonemusicmaker_one],
        [(35, 4), (36, 4), trombonemusicmaker_three],
        [(37, 4), (40, 4), trombonemusicmaker_two],
        [(40, 4), (42, 4), trombonemusicmaker_two],
        [(46, 4), (49, 4), trombonemusicmaker_one],
        [(51, 4), (52, 4), trombonemusicmaker_three],
        [(57, 4), (59, 4), trombonemusicmaker_two],
        [(59, 4), (61, 4), trombonemusicmaker_two],
        [(64, 4), (66, 4), trombonemusicmaker_one],
        [(67, 4), (70, 4), trombonemusicmaker_three],
        [(70, 4), (72, 4), trombonemusicmaker_one],
        [(72, 4), (73, 4), trombonemusicmaker_one],
        [(77, 4), (79, 4), trombonemusicmaker_two],
        [(79, 4), (82, 4), trombonemusicmaker_two],
        [(83, 4), (85, 4), trombonemusicmaker_three],
        [(88, 4), (89, 4), trombonemusicmaker_two],
        [(89, 4), (92, 4), trombonemusicmaker_two],
        [(97, 4), (98, 4), trombonemusicmaker_one],
        [(100, 4), (103, 4), trombonemusicmaker_two],
        [(107, 4), (110, 4), trombonemusicmaker_three],
        [(110, 4), (112, 4), trombonemusicmaker_one],
        [(113, 4), (114, 4), trombonemusicmaker_one],
        [(114, 4), (117, 4), trombonemusicmaker_one],
        [(118, 4), (119, 4), trombonemusicmaker_one],
        [(119, 4), (122, 4), trombonemusicmaker_one],
        [(123, 4), (125, 4), trombonemusicmaker_one],
        [(126, 4), (131, 4), trombonemusicmaker_two],
        [(138, 4), (141, 4), trombonemusicmaker_two],
        [(146, 4), (150, 4), trombonemusicmaker_two],
        [(150, 4), (154, 4), trombonemusicmaker_three],
        [(157, 4), (159, 4), trombonemusicmaker_three],
        [(160, 4), (164, 4), trombonemusicmaker_three],
        [(164, 4), (165, 4), trombonemusicmaker_three],
        [(169, 4), (172, 4), trombonemusicmaker_three],
        [(174, 4), (175, 4), trombonemusicmaker_three],
        [(180, 4), (183, 4), trombonemusicmaker_three],
        [(183, 4), (184, 4), trombonemusicmaker_three],
        [(186, 4), (190, 4), trombonemusicmaker_three],
    ]
])

voice_11_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 11',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(7, 4), (11, 4), cellomusicmaker_one],
        [(14, 4), (16, 4), cellomusicmaker_two],
        [(21, 4), (22, 4), cellomusicmaker_three],
        [(22, 4), (23, 4), cellomusicmaker_three],
        [(27, 4), (30, 4), cellomusicmaker_one],
        [(35, 4), (36, 4), cellomusicmaker_three],
        [(37, 4), (40, 4), cellomusicmaker_two],
        [(40, 4), (42, 4), cellomusicmaker_two],
        [(46, 4), (49, 4), cellomusicmaker_one],
        [(51, 4), (52, 4), cellomusicmaker_three],
        [(57, 4), (59, 4), cellomusicmaker_two],
        [(59, 4), (61, 4), cellomusicmaker_two],
        [(64, 4), (66, 4), cellomusicmaker_one],
        [(67, 4), (70, 4), cellomusicmaker_three],
        [(70, 4), (72, 4), cellomusicmaker_one],
        [(72, 4), (73, 4), cellomusicmaker_one],
        [(77, 4), (79, 4), cellomusicmaker_two],
        [(79, 4), (82, 4), cellomusicmaker_two],
        [(83, 4), (85, 4), cellomusicmaker_three],
        [(88, 4), (89, 4), cellomusicmaker_two],
        [(89, 4), (92, 4), cellomusicmaker_two],
        [(97, 4), (98, 4), cellomusicmaker_one],
        [(100, 4), (103, 4), cellomusicmaker_two],
        [(107, 4), (110, 4), cellomusicmaker_three],
        [(110, 4), (112, 4), cellomusicmaker_one],
        [(113, 4), (114, 4), cellomusicmaker_one],
        [(114, 4), (117, 4), cellomusicmaker_one],
        [(118, 4), (119, 4), cellomusicmaker_one],
        [(119, 4), (122, 4), cellomusicmaker_one],
        [(123, 4), (125, 4), cellomusicmaker_one],
        [(126, 4), (131, 4), cellomusicmaker_two],
        [(138, 4), (141, 4), cellomusicmaker_two],
        [(146, 4), (150, 4), cellomusicmaker_two],
        [(150, 4), (153, 4), cellomusicmaker_three],
        [(155, 4), (156, 4), cellomusicmaker_three],
        [(161, 4), (164, 4), cellomusicmaker_three],
        [(164, 4), (165, 4), cellomusicmaker_three],
        [(168, 4), (170, 4), cellomusicmaker_three],
        [(171, 4), (172, 4), cellomusicmaker_three],
        [(172, 4), (175, 4), cellomusicmaker_three],
        [(175, 4), (176, 4), cellomusicmaker_three],
        [(180, 4), (183, 4), cellomusicmaker_three],
        [(185, 4), (186, 4), cellomusicmaker_three],
        [(186, 4), (190, 4), cellomusicmaker_three],
    ]
])

###group four###
voice_4_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 4',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(0, 4), (5, 4), hornmusicmaker_one],
        [(8, 4), (10, 4), hornmusicmaker_two],
        [(14, 4), (18, 4), hornmusicmaker_three],
        [(21, 4), (22, 4), hornmusicmaker_one],
        [(22, 4), (23, 4), hornmusicmaker_one],
        [(38, 4), (40, 4), hornmusicmaker_two],
        [(41, 4), (43, 4), hornmusicmaker_one],
        [(43, 4), (46, 4), hornmusicmaker_one],
        [(50, 4), (53, 4), hornmusicmaker_three],
        [(55, 4), (56, 4), hornmusicmaker_two],
        [(61, 4), (64, 4), hornmusicmaker_one],
        [(64, 4), (65, 4), hornmusicmaker_one],
        [(68, 4), (70, 4), hornmusicmaker_three],
        [(70, 4), (72, 4), hornmusicmaker_two],
        [(72, 4), (74, 4), hornmusicmaker_two],
        [(79, 4), (80, 4), hornmusicmaker_three],
        [(82, 4), (85, 4), hornmusicmaker_two],
        [(89, 4), (94, 4), hornmusicmaker_one],
        [(95, 4), (97, 4), hornmusicmaker_two],
        [(100, 4), (104, 4), hornmusicmaker_three],
        [(109, 4), (110, 4), hornmusicmaker_two],
        [(110, 4), (111, 4), hornmusicmaker_one],
        [(112, 4), (114, 4), hornmusicmaker_one],
        [(114, 4), (116, 4), hornmusicmaker_one],
        [(117, 4), (119, 4), hornmusicmaker_one],
        [(119, 4), (121, 4), hornmusicmaker_one],
        [(122, 4), (123, 4), hornmusicmaker_one],
        [(123, 4), (125, 4), hornmusicmaker_one],
        [(133, 4), (136, 4), hornmusicmaker_two],
        [(142, 4), (146, 4), hornmusicmaker_two],
        [(146, 4), (150, 4), hornmusicmaker_two],
        [(153, 4), (154, 4), hornmusicmaker_three],
        [(154, 4), (155, 4), hornmusicmaker_three],
        [(159, 4), (162, 4), hornmusicmaker_three],
        [(164, 4), (168, 4), hornmusicmaker_three],
        [(171, 4), (172, 4), hornmusicmaker_three],
        [(172, 4), (173, 4), hornmusicmaker_three],
        [(177, 4), (179, 4), hornmusicmaker_three],
        [(179, 4), (180, 4), hornmusicmaker_three],
        [(182, 4), (183, 4), hornmusicmaker_three],
        [(183, 4), (186, 4), hornmusicmaker_three],
        [(186, 4), (190, 4), hornmusicmaker_three],
    ]
])

voice_7_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 7',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(0, 4), (5, 4), tubamusicmaker_one],
        [(8, 4), (10, 4), tubamusicmaker_two],
        [(14, 4), (18, 4), tubamusicmaker_three],
        [(21, 4), (22, 4), tubamusicmaker_one],
        [(22, 4), (23, 4), tubamusicmaker_one],
        [(26, 4), (30, 4), tubamusicmaker_two],
        [(38, 4), (40, 4), tubamusicmaker_two],
        [(41, 4), (43, 4), tubamusicmaker_one],
        [(43, 4), (46, 4), tubamusicmaker_one],
        [(50, 4), (53, 4), tubamusicmaker_three],
        [(55, 4), (56, 4), tubamusicmaker_two],
        [(61, 4), (64, 4), tubamusicmaker_one],
        [(64, 4), (65, 4), tubamusicmaker_one],
        [(68, 4), (70, 4), tubamusicmaker_three],
        [(70, 4), (72, 4), tubamusicmaker_two],
        [(72, 4), (74, 4), tubamusicmaker_two],
        [(79, 4), (80, 4), tubamusicmaker_three],
        [(82, 4), (85, 4), tubamusicmaker_two],
        [(89, 4), (94, 4), tubamusicmaker_one],
        [(95, 4), (97, 4), tubamusicmaker_two],
        [(100, 4), (104, 4), tubamusicmaker_three],
        [(109, 4), (110, 4), tubamusicmaker_two],
        [(110, 4), (111, 4), tubamusicmaker_one],
        [(112, 4), (114, 4), tubamusicmaker_one],
        [(114, 4), (116, 4), tubamusicmaker_one],
        [(117, 4), (119, 4), tubamusicmaker_one],
        [(119, 4), (121, 4), tubamusicmaker_one],
        [(122, 4), (123, 4), tubamusicmaker_one],
        [(123, 4), (125, 4), tubamusicmaker_one],
        [(133, 4), (136, 4), tubamusicmaker_two],
        [(142, 4), (146, 4), tubamusicmaker_two],
        [(146, 4), (150, 4), tubamusicmaker_two],
        [(154, 4), (157, 4), tubamusicmaker_three],
        [(159, 4), (163, 4), tubamusicmaker_three],
        [(166, 4), (168, 4), tubamusicmaker_three],
        [(172, 4), (175, 4), tubamusicmaker_three],
        [(177, 4), (179, 4), tubamusicmaker_three],
        [(179, 4), (181, 4), tubamusicmaker_three],
        [(184, 4), (186, 4), tubamusicmaker_three],
        [(186, 4), (190, 4), tubamusicmaker_three],
    ]
])

voice_12_timespan_list = abjad.TimespanList([
    abjad.AnnotatedTimespan(
        start_offset=start_offset,
        stop_offset=stop_offset,
        annotation=MusicSpecifier(
            music_maker=music_maker,
            voice_name='Voice 12',
        ),
    )
    for start_offset, stop_offset, music_maker in [
        [(0, 4), (5, 4), bassmusicmaker_one],
        [(8, 4), (10, 4), bassmusicmaker_two],
        [(14, 4), (18, 4), bassmusicmaker_three],
        [(21, 4), (22, 4), bassmusicmaker_one],
        [(22, 4), (23, 4), bassmusicmaker_one],
        [(38, 4), (40, 4), bassmusicmaker_two],
        [(41, 4), (43, 4), bassmusicmaker_one],
        [(43, 4), (46, 4), bassmusicmaker_one],
        [(50, 4), (53, 4), bassmusicmaker_three],
        [(55, 4), (56, 4), bassmusicmaker_two],
        [(61, 4), (64, 4), bassmusicmaker_one],
        [(64, 4), (65, 4), bassmusicmaker_one],
        [(68, 4), (70, 4), bassmusicmaker_three],
        [(70, 4), (72, 4), bassmusicmaker_two],
        [(72, 4), (74, 4), bassmusicmaker_two],
        [(79, 4), (80, 4), bassmusicmaker_three],
        [(82, 4), (85, 4), bassmusicmaker_two],
        [(89, 4), (94, 4), bassmusicmaker_one],
        [(95, 4), (97, 4), bassmusicmaker_two],
        [(100, 4), (104, 4), bassmusicmaker_three],
        [(109, 4), (110, 4), bassmusicmaker_two],
        [(110, 4), (111, 4), bassmusicmaker_one],
        [(112, 4), (114, 4), bassmusicmaker_one],
        [(114, 4), (116, 4), bassmusicmaker_one],
        [(117, 4), (119, 4), bassmusicmaker_one],
        [(119, 4), (121, 4), bassmusicmaker_one],
        [(122, 4), (123, 4), bassmusicmaker_one],
        [(123, 4), (125, 4), bassmusicmaker_one],
        [(133, 4), (136, 4), bassmusicmaker_two],
        [(142, 4), (146, 4), bassmusicmaker_two],
        [(146, 4), (150, 4), bassmusicmaker_two],
        [(152, 4), (154, 4), bassmusicmaker_three],
        [(154, 4), (156, 4), bassmusicmaker_three],
        [(159, 4), (161, 4), bassmusicmaker_three],
        [(165, 4), (168, 4), bassmusicmaker_three],
        [(170, 4), (172, 4), bassmusicmaker_three],
        [(172, 4), (174, 4), bassmusicmaker_three],
        [(177, 4), (179, 4), bassmusicmaker_three],
        [(183, 4), (186, 4), bassmusicmaker_three],
        [(186, 4), (190, 4), bassmusicmaker_three],
    ]
])

all_timespan_lists = {
    'Voice 1': voice_1_timespan_list,
    'Voice 2': voice_2_timespan_list,
    'Voice 3': voice_3_timespan_list,
    'Voice 4': voice_4_timespan_list,
    'Voice 5': voice_5_timespan_list,
    'Voice 6': voice_6_timespan_list,
    'Voice 7': voice_7_timespan_list,
    'Voice 8': voice_8_timespan_list,
    'Voice 9': voice_9_timespan_list,
    'Voice 10': voice_10_timespan_list,
    'Voice 11': voice_11_timespan_list,
    'Voice 12': voice_12_timespan_list,
}

global_timespan = abjad.Timespan(
    start_offset=0,
    stop_offset=max(_.stop_offset for _ in all_timespan_lists.values())
)

for voice_name, timespan_list in all_timespan_lists.items():
    silences = abjad.TimespanList([global_timespan])
    silences.extend(timespan_list)
    silences.sort()
    silences.compute_logical_xor()
    for silence_timespan in silences:
        timespan_list.append(
            abjad.AnnotatedTimespan(
                start_offset=silence_timespan.start_offset,
                stop_offset=silence_timespan.stop_offset,
                annotation=MusicSpecifier(
                    music_maker=None,
                    voice_name=voice_name,
                ),
            )
        )
    timespan_list.sort()

for voice_name, timespan_list in all_timespan_lists.items():
    shards = timespan_list.split_at_offsets(bounds)
    split_timespan_list = abjad.TimespanList()
    for shard in shards:
        split_timespan_list.extend(shard)
    split_timespan_list.sort()
    all_timespan_lists[voice_name] = timespan_list

# score structure
score = abjad.Score([
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context 1'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 1')],name='Staff 1', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 2')],name='Staff 2', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 3')],name='Staff 3', lilypond_type='Staff',),
        ],
        name='Staff Group 1',
    ),
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context 2'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 4')],name='Staff 4', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 5')],name='Staff 5', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 6')],name='Staff 6', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 7')],name='Staff 7', lilypond_type='Staff',),
        ],
        name='Staff Group 2',
    ),
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context 3'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 8')],name='Staff 8', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 9')],name='Staff 9', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 10')],name='Staff 10', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 11')],name='Staff 11', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 12')],name='Staff 12', lilypond_type='Staff',),
        ],
        name='Staff Group 3',
    )
],
)

for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context 1'].append(skip)

for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context 2'].append(skip)

for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context 3'].append(skip)

print('Making containers ...')

def make_container(music_maker, durations):
    selections = music_maker(durations)
    container = abjad.Container([])
    container.extend(selections)
    return container

def key_function(timespan):
    """
    Get the timespan's annotation's rhythm-maker.
    If the annotation's rhythm-maker is None, return the silence maker.
    """
    return timespan.annotation.music_maker or silence_maker

for voice_name, timespan_list in all_timespan_lists.items():
    for music_maker, grouper in itertools.groupby(
        timespan_list,
        key=key_function,
    ):
        durations = [timespan.duration for timespan in grouper]
        container = make_container(music_maker, durations)
        voice = score[voice_name]
        voice.append(container)

print('Splitting and rewriting ...')

# split and rewite meters
for voice in abjad.iterate(score['Staff Group 1']).components(abjad.Voice):
    for i , shard in enumerate(abjad.mutate(voice[:]).split(time_signatures)):
        time_signature = time_signatures[i]
        abjad.mutate(shard).rewrite_meter(time_signature)

for voice in abjad.iterate(score['Staff Group 2']).components(abjad.Voice):
    for i , shard in enumerate(abjad.mutate(voice[:]).split(time_signatures)):
        time_signature = time_signatures[i]
        abjad.mutate(shard).rewrite_meter(time_signature)

for voice in abjad.iterate(score['Staff Group 3']).components(abjad.Voice):
    for i , shard in enumerate(abjad.mutate(voice[:]).split(time_signatures)):
        time_signature = time_signatures[i]
        abjad.mutate(shard).rewrite_meter(time_signature)

print('Beaming runs ...')

for voice in abjad.select(score).components(abjad.Voice):
    for run in abjad.select(voice).runs():
        if 1 < len(run):
            # use a beam_specifier to remove beam indicators from run
            specifier = abjadext.rmakers.BeamSpecifier(
                beam_each_division=False,
                )
            specifier(run)
            # then attach new indicators at the 0 and -1 of run
            abjad.attach(abjad.StartBeam(), run[0])
            abjad.attach(abjad.StopBeam(), run[-1])
            for leaf in run:
                # continue if leaf can't be beamed
                if abjad.Duration(1, 4) <= leaf.written_duration:
                    continue
                previous_leaf = abjad.inspect(leaf).leaf(-1)
                next_leaf = abjad.inspect(leaf).leaf(1)
                # if next leaf is quarter note (or greater) ...
                if (isinstance(next_leaf, (abjad.Chord, abjad.Note)) and
                    abjad.Duration(1, 4) <= next_leaf.written_duration):
                    left = previous_leaf.written_duration.flag_count
                    right = leaf.written_duration.flag_count # right-pointing nib
                    beam_count = abjad.BeamCount(
                        left=left,
                        right=right,
                        )
                    abjad.attach(beam_count, leaf)
                    continue
                # if previous leaf is quarter note (or greater) ...
                if (isinstance(previous_leaf, (abjad.Chord, abjad.Note)) and
                    abjad.Duration(1, 4) <= previous_leaf.written_duration):
                    left = leaf.written_duration.flag_count # left-pointing nib
                    right = next_leaf.written_duration.flag_count
                    beam_count = abjad.BeamCount(
                        left=left,
                        right=right,
                        )
                    abjad.attach(beam_count, leaf)

print('Beautifying score ...')
# cutaway score
for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    for selection in abjad.select(staff).components(abjad.Rest).group_by_contiguity():
        start_command = abjad.LilyPondLiteral(
            r'\stopStaff \once \override Staff.StaffSymbol.line-count = #1 \startStaff',
            format_slot='before',
            )
        stop_command = abjad.LilyPondLiteral(
            r'\stopStaff \startStaff',
            format_slot='after',
            )
        abjad.attach(start_command, selection[0])
        abjad.attach(stop_command, selection[-1])

for staff in abjad.iterate(score['Staff Group 2']).components(abjad.Staff):
    for selection in abjad.select(staff).components(abjad.Rest).group_by_contiguity():
        start_command = abjad.LilyPondLiteral(
            r'\stopStaff \once \override Staff.StaffSymbol.line-count = #1 \startStaff',
            format_slot='before',
            )
        stop_command = abjad.LilyPondLiteral(
            r'\stopStaff \startStaff',
            format_slot='after',
            )
        abjad.attach(start_command, selection[0])
        abjad.attach(stop_command, selection[-1])

for staff in abjad.iterate(score['Staff Group 3']).components(abjad.Staff):
    for selection in abjad.select(staff).components(abjad.Rest).group_by_contiguity():
        start_command = abjad.LilyPondLiteral(
            r'\stopStaff \once \override Staff.StaffSymbol.line-count = #1 \startStaff',
            format_slot='before',
            )
        stop_command = abjad.LilyPondLiteral(
            r'\stopStaff \startStaff',
            format_slot='after',
            )
        abjad.attach(start_command, selection[0])
        abjad.attach(stop_command, selection[-1])

print('Stopping Hairpins ...')
for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    for rest in abjad.iterate(staff).components(abjad.Rest):
        previous_leaf = abjad.inspect(rest).leaf(-1)
        if isinstance(previous_leaf, abjad.Note):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Chord):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Rest):
            pass

for staff in abjad.iterate(score['Staff Group 2']).components(abjad.Staff):
    for rest in abjad.iterate(staff).components(abjad.Rest):
        previous_leaf = abjad.inspect(rest).leaf(-1)
        if isinstance(previous_leaf, abjad.Note):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Chord):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Rest):
            pass

for staff in abjad.iterate(score['Staff Group 3']).components(abjad.Staff):
    for rest in abjad.iterate(staff).components(abjad.Rest):
        previous_leaf = abjad.inspect(rest).leaf(-1)
        if isinstance(previous_leaf, abjad.Note):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Chord):
            abjad.attach(abjad.StopHairpin(), rest)
        elif isinstance(previous_leaf, abjad.Rest):
            pass

# Make pitches
print('Adding pitch material ...')
def cyc(lst):
    count = 0
    while True:
        yield lst[count%len(lst)]
        count += 1

#attach instruments and clefs

print('Adding attachments ...')
bar_line = abjad.BarLine('||')
metro = abjad.MetronomeMark((1, 4), 108)
markup1 = abjad.Markup(r'\bold { A }')
markup2 = abjad.Markup(r'\bold { B }')
markup3 = abjad.Markup(r'\bold { C }')
markup4 = abjad.Markup(r'\bold { D }')
markup5 = abjad.Markup(r'\bold { E }')
markup6 = abjad.Markup(r'\bold { F }')
mark1 = abjad.RehearsalMark(markup=markup1)
mark2 = abjad.RehearsalMark(markup=markup2)
mark3 = abjad.RehearsalMark(markup=markup3)
mark4 = abjad.RehearsalMark(markup=markup4)
mark5 = abjad.RehearsalMark(markup=markup5)
mark6 = abjad.RehearsalMark(markup=markup6)

instruments1 = cyc([
    abjad.Flute(),
    abjad.ClarinetInBFlat(),
    abjad.Bassoon(),
])

instruments2 = cyc([
    abjad.FrenchHorn(),
    abjad.Trumpet(),
    abjad.TenorTrombone(),
    abjad.Tuba(),
])

instruments3 = cyc([
    abjad.Violin(),
    abjad.Violin(),
    abjad.Viola(),
    abjad.Cello(),
    abjad.Contrabass(),
])

clefs1 = cyc([
    abjad.Clef('treble'),
    abjad.Clef('treble'),
    abjad.Clef('bass'),
])

clefs2 = cyc([
    abjad.Clef('bass'),
    abjad.Clef('treble'),
    abjad.Clef('bass'),
    abjad.Clef('bass'),
])

clefs3 = cyc([
    abjad.Clef('treble'),
    abjad.Clef('treble'),
    abjad.Clef('alto'),
    abjad.Clef('bass'),
    abjad.Clef('bass'),
])

abbreviations1 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('fl.'),),
    abjad.MarginMarkup(markup=abjad.Markup('cl.'),),
    abjad.MarginMarkup(markup=abjad.Markup('bssn.'),),
])

abbreviations2 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('hr.'),),
    abjad.MarginMarkup(markup=abjad.Markup('trp.'),),
    abjad.MarginMarkup(markup=abjad.Markup('trmb.'),),
    abjad.MarginMarkup(markup=abjad.Markup('tb.'),),
])

abbreviations3 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('vln.I'),),
    abjad.MarginMarkup(markup=abjad.Markup('vln.II'),),
    abjad.MarginMarkup(markup=abjad.Markup('vla.'),),
    abjad.MarginMarkup(markup=abjad.Markup('vc.'),),
    abjad.MarginMarkup(markup=abjad.Markup('cb.'),),
])

names1 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Flute'),),
    abjad.StartMarkup(markup=abjad.Markup('Clarinet'),),
    abjad.StartMarkup(markup=abjad.Markup('Bassoon'),),
])

names2 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Horn'),),
    abjad.StartMarkup(markup=abjad.Markup('Trumpet'),),
    abjad.StartMarkup(markup=abjad.Markup('Trombone'),),
    abjad.StartMarkup(markup=abjad.Markup('Tuba'),),
])

names3 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Violin I'),),
    abjad.StartMarkup(markup=abjad.Markup('Violin II'),),
    abjad.StartMarkup(markup=abjad.Markup('Viola'),),
    abjad.StartMarkup(markup=abjad.Markup('Violoncello'),),
    abjad.StartMarkup(markup=abjad.Markup('Contrabass'),),
])

for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[0]
    abjad.attach(next(instruments1), leaf1)
    abjad.attach(next(abbreviations1), leaf1)
    abjad.attach(next(names1), leaf1)
    abjad.attach(next(clefs1), leaf1)

for staff in abjad.iterate(score['Staff Group 2']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[0]
    abjad.attach(next(instruments2), leaf1)
    abjad.attach(next(abbreviations2), leaf1)
    abjad.attach(next(names2), leaf1)
    abjad.attach(next(clefs2), leaf1)

for staff in abjad.iterate(score['Staff Group 3']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[0]
    abjad.attach(next(instruments3), leaf1)
    abjad.attach(next(abbreviations3), leaf1)
    abjad.attach(next(names3), leaf1)
    abjad.attach(next(clefs3), leaf1)

for staff in abjad.select(score['Staff Group 1']).components(abjad.Staff)[0]:
    leaf1 = abjad.select(staff).leaves()[0]
    last_leaf = abjad.select(staff).leaves()[-1]
    abjad.attach(metro, leaf1)
    abjad.attach(bar_line, last_leaf)

for staff in abjad.select(score['Staff Group 2']).components(abjad.Staff)[0]:
    leaf1 = abjad.select(staff).leaves()[0]
    last_leaf = abjad.select(staff).leaves()[-1]
    abjad.attach(metro, leaf1)
    abjad.attach(bar_line, last_leaf)

for staff in abjad.select(score['Staff Group 3']).components(abjad.Staff)[0]:
    leaf1 = abjad.select(staff).leaves()[0]
    last_leaf = abjad.select(staff).leaves()[-1]
    abjad.attach(metro, leaf1)
    abjad.attach(bar_line, last_leaf)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[7]
    abjad.attach(mark1, leaf1)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[7]
    abjad.attach(mark1, leaf1)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[7]
    abjad.attach(mark1, leaf1)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf2 = abjad.select(staff).leaves()[16]
    abjad.attach(mark2, leaf2)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf2 = abjad.select(staff).leaves()[16]
    abjad.attach(mark2, leaf2)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf2 = abjad.select(staff).leaves()[16]
    abjad.attach(mark2, leaf2)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf3 = abjad.select(staff).leaves()[22]
    abjad.attach(mark3, leaf3)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf3 = abjad.select(staff).leaves()[22]
    abjad.attach(mark3, leaf3)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf3 = abjad.select(staff).leaves()[22]
    abjad.attach(mark3, leaf3)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf4 = abjad.select(staff).leaves()[29]
    abjad.attach(mark4, leaf4)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf4 = abjad.select(staff).leaves()[29]
    abjad.attach(mark4, leaf4)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf4 = abjad.select(staff).leaves()[29]
    abjad.attach(mark4, leaf4)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf5 = abjad.select(staff).leaves()[34]
    abjad.attach(mark5, leaf5)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf5 = abjad.select(staff).leaves()[34]
    abjad.attach(mark5, leaf5)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf5 = abjad.select(staff).leaves()[34]
    abjad.attach(mark5, leaf5)

for staff in abjad.iterate(score['Global Context 1']).components(abjad.Staff):
    leaf6 = abjad.select(staff).leaves()[39]
    abjad.attach(mark6, leaf6)

for staff in abjad.iterate(score['Global Context 2']).components(abjad.Staff):
    leaf6 = abjad.select(staff).leaves()[39]
    abjad.attach(mark6, leaf6)

for staff in abjad.iterate(score['Global Context 3']).components(abjad.Staff):
    leaf6 = abjad.select(staff).leaves()[39]
    abjad.attach(mark6, leaf6)

for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    abjad.Instrument.transpose_from_sounding_pitch(staff)

for staff in abjad.iterate(score['Staff Group 2']).components(abjad.Staff):
    abjad.Instrument.transpose_from_sounding_pitch(staff)

for staff in abjad.iterate(score['Staff Group 3']).components(abjad.Staff):
    abjad.Instrument.transpose_from_sounding_pitch(staff)

score_file = abjad.LilyPondFile.new(
    score,
    includes=['first_stylesheet.ily', '/Users/evansdsg2/abjad/docs/source/_stylesheets/abjad.ily'],
    )

abjad.SegmentMaker.comment_measure_numbers(score)
###################

directory = '/Users/evansdsg2/Scores//tianshu/tianshu/Segments/Segment_I'
pdf_path = f'{directory}/Segment_I.pdf'
path = pathlib.Path('Segment_I.pdf')
if path.exists():
    print(f'Removing {pdf_path} ...')
    path.unlink()
time_1 = time.time()
print(f'Persisting {pdf_path} ...')
result = abjad.persist(score_file).as_pdf(pdf_path)
print(result[0])
print(result[1])
print(result[2])
success = result[3]
if success is False:
        print('LilyPond failed!')
time_2 = time.time()
total_time = time_2 - time_1
print(f'Total time: {total_time} seconds')
if path.exists():
    print(f'Opening {pdf_path} ...')
    os.system(f'open {pdf_path}')

# for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
#     abjad.show(staff)
#
# for staff in abjad.iterate(score['Staff Group 2']).components(abjad.Staff):
#     abjad.show(staff)
#
# for staff in abjad.iterate(score['Staff Group 3']).components(abjad.Staff):
#     abjad.show(staff)

# abjad.show(score)
# abjad.play(score)
