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
        (4, 4), (5, 4), (3, 4), (3, 4), (5, 4), (3, 4),
        (4, 4), (4, 4), (5, 4), (4, 4), (4, 4), (4, 4),
        (3, 4), (5, 4), (4, 4), (4, 4), (4, 4), (4, 4),
        (4, 4), (5, 4), (3, 4), (4, 4), (3, 4), (3, 4),
        (5, 4), (4, 4), (3, 4), (4, 4), (4, 4), (5, 4),
        (3, 4), (5, 4), (5, 4), (4, 4), (3, 4), (3, 4),
        (4, 4), (4, 4), (4, 4), (4, 4), (5, 4), (4, 4),
        (5, 4), (4, 4), (4, 4), (5, 4), (5, 4),
    ]
]

bounds = abjad.mathtools.cumulative_sums([_.duration for _ in time_signatures])

def reduceMod7(rw):
    return [(x % 8) for x in rw]

def reduceMod9(rw):
    return [(x % 10) for x in rw]

def reduceMod17(rw):
    return [(x % 18) for x in rw]

def reduceMod21(rw):
    return [(x % 22) for x in rw]

def reduceMod47(rw):
    return [(x % 48) for x in rw]

def cyc(lst):
    count = 0
    while True:
        yield lst[count%len(lst)]
        count += 1

def grouper(lst1, lst2):
    def cyc(lst):
        c = 0
        while True:
            yield lst[c%len(lst)]
            c += 1
    lst1 = cyc(lst1)
    return [next(lst1) if i == 1 else [next(lst1) for _ in range(i)] for i in lst2]

seed(1)
cello_random_walk_one = []
cello_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_one[i-1] + movement
    cello_random_walk_one.append(value)
cello_random_walk_one = [abs(x) for x in cello_random_walk_one]
cello_chord_one = [-12, -11.5, -11, -10.5, -10, -9.5, -9, -8.5, -8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, -0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10, -10.5, -11, -11.5, ]
cello_notes_one = [cello_chord_one[x] for x in reduceMod47(cello_random_walk_one)]

seed(2)
cello_random_walk_two = []
cello_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_two[i-1] + movement
    cello_random_walk_two.append(value)
cello_random_walk_two = [abs(x) for x in cello_random_walk_two]
cello_chord_two = [-24, -11, -20, -6, -12, -6, 0, -11, -6, 4, 0, 6, 0, -11, -6, -24, -8, 0, ]
cello_notes_two_walk = [cello_chord_two[x] for x in reduceMod17(cello_random_walk_two)]
map_1 = [1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, ]
cello_notes_two = grouper(cello_notes_two_walk, map_1)

seed(3)
cello_random_walk_three = []
cello_random_walk_three.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_three[i-1] + movement
    cello_random_walk_three.append(value)
cello_random_walk_three = [abs(x) for x in cello_random_walk_three]
cello_chord_three = [-24, -20, -15, -14, -4, 5, 11, 19, 26, 37, 39, 42, 39, 37, 26, 19, 11, 5, -4, -14, -15, -20, ]
cello_notes_three = [cello_chord_three[x] for x in reduceMod21(cello_random_walk_three)]

seed(4)
cello_random_walk_four = []
cello_random_walk_four.append(-1 if random() < 0.5 else 1)
for i in range(1, 2000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_four[i-1] + movement
    cello_random_walk_four.append(value)
cello_random_walk_four = [abs(x) for x in cello_random_walk_four]
cello_chord_four = [-17, -8, -13, -5, 5, -5, -13, -8, ]
map_2 = [2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, ]
cello_notes_four_walk = [cello_chord_four[x] for x in reduceMod7(cello_random_walk_four)]
cello_notes_four = grouper(cello_notes_four_walk, map_2)

rmaker_one = abjadext.rmakers.TaleaRhythmMaker(
    talea=abjadext.rmakers.Talea(
        counts=[7, 4, 6, 3, 5, 3, 5, 3, 6, 4],
        denominator=32,
        ),
    beam_specifier=abjadext.rmakers.BeamSpecifier(
        beam_divisions_together=True,
        beam_rests=False,
        ),
    extra_counts_per_division=[0, 1, 0, -1],
    tuplet_specifier=abjadext.rmakers.TupletSpecifier(
        trivialize=True,
        extract_trivial=True,
        rewrite_rest_filled=True,
        ),
    )

rmaker_two = abjadext.rmakers.TaleaRhythmMaker(
    talea=abjadext.rmakers.Talea(
        counts=[1, 1, 1, 2, 1, 3, 1, 2, 3],
        denominator=16,
        ),
    beam_specifier=abjadext.rmakers.BeamSpecifier(
        beam_divisions_together=True,
        beam_rests=False,
        ),
    extra_counts_per_division=[1, 0, -1, 0, 1],
    tuplet_specifier=abjadext.rmakers.TupletSpecifier(
        trivialize=True,
        extract_trivial=True,
        rewrite_rest_filled=True,
        ),
    )

rmaker_three = abjadext.rmakers.EvenDivisionRhythmMaker(
    denominators=[8, 8, 16, 8, 8, 16],
    extra_counts_per_division=[0, 1, 0, 0, -1, 0, 1, -1],
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

#####cello#####
cellomusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=cello_notes_one,
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
    pitches=cello_notes_three,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
cellomusicmaker_four = MusicMaker(
    rmaker=rmaker_two,
    pitches=cello_notes_four,
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

bowmaker = MusicMaker(
    pitches=[33, ],
    rmaker=rmaker_two,
    continuous=True,
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
        [(0, 4), (4, 4), bowmaker],
        [(4, 4), (7, 4), bowmaker],
        [(12, 4), (15, 4), bowmaker],
        [(15, 4), (17, 4), bowmaker],
        [(17, 4), (20, 4), bowmaker],
        [(23, 4), (25, 4), bowmaker],
        [(25, 4), (27, 4), bowmaker],
        [(27, 4), (30, 4), bowmaker],
        [(32, 4), (36, 4), bowmaker],
        [(43, 4), (44, 4), bowmaker],
        [(44, 4), (48, 4), bowmaker],
        [(48, 4), (51, 4), bowmaker],
        [(52, 4), (56, 4), bowmaker],
        [(56, 4), (58, 4), bowmaker],
        [(62, 4), (64, 4), bowmaker],
        [(68, 4), (72, 4), bowmaker],
        [(72, 4), (76, 4), bowmaker],
        [(76, 4), (78, 4), bowmaker],
        [(78, 4), (81, 4), bowmaker],
        [(82, 4), (84, 4), bowmaker],
        [(84, 4), (87, 4), bowmaker],
        [(88, 4), (91, 4), bowmaker],
        [(91, 4), (93, 4), bowmaker],
        [(94, 4), (99, 4), bowmaker],
        [(100, 4), (103, 4), bowmaker],
        [(103, 4), (105, 4), bowmaker],
        [(106, 4), (110, 4), bowmaker],
        [(110, 4), (111, 4), bowmaker],
        [(112, 4), (114, 4), bowmaker],
        [(114, 4), (119, 4), bowmaker],
        [(122, 4), (126, 4), bowmaker],
        [(128, 4), (131, 4), bowmaker],
        [(132, 4), (134, 4), bowmaker],
        [(139, 4), (140, 4), bowmaker],
        [(144, 4), (146, 4), bowmaker],
        [(146, 4), (149, 4), bowmaker],
        [(150, 4), (153, 4), bowmaker],
        [(157, 4), (158, 4), bowmaker],
        [(158, 4), (162, 4), bowmaker],
        [(165, 4), (167, 4), bowmaker],
        [(167, 4), (169, 4), bowmaker],
        [(174, 4), (176, 4), bowmaker],
        [(176, 4), (177, 4), bowmaker],
        [(181, 4), (185, 4), bowmaker],
        [(185, 4), (186, 4), bowmaker],

    ]
])

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
        [(0, 4), (4, 4), cellomusicmaker_two],
        [(4, 4), (7, 4), cellomusicmaker_one],
        [(12, 4), (15, 4), cellomusicmaker_two],
        [(15, 4), (17, 4), cellomusicmaker_one],
        [(17, 4), (20, 4), cellomusicmaker_two],
        [(23, 4), (25, 4), cellomusicmaker_two],
        [(25, 4), (27, 4), cellomusicmaker_one],
        [(27, 4), (30, 4), cellomusicmaker_two],
        [(32, 4), (36, 4), cellomusicmaker_three],
        [(43, 4), (44, 4), cellomusicmaker_two],
        [(44, 4), (48, 4), cellomusicmaker_two],
        [(48, 4), (51, 4), cellomusicmaker_one],
        [(52, 4), (56, 4), cellomusicmaker_one],
        [(56, 4), (58, 4), cellomusicmaker_two],
        [(62, 4), (64, 4), cellomusicmaker_two],
        [(68, 4), (72, 4), cellomusicmaker_three],
        [(72, 4), (76, 4), cellomusicmaker_two],
        [(76, 4), (78, 4), cellomusicmaker_three],
        [(78, 4), (81, 4), cellomusicmaker_two],
        [(82, 4), (84, 4), cellomusicmaker_two],
        [(84, 4), (87, 4), cellomusicmaker_four],#
        [(88, 4), (91, 4), cellomusicmaker_four],
        [(91, 4), (93, 4), cellomusicmaker_one],
        [(94, 4), (99, 4), cellomusicmaker_three],
        [(100, 4), (103, 4), cellomusicmaker_one],
        [(103, 4), (105, 4), cellomusicmaker_one],
        [(106, 4), (110, 4), cellomusicmaker_four],
        [(110, 4), (111, 4), cellomusicmaker_four],
        [(112, 4), (114, 4), cellomusicmaker_three],
        [(114, 4), (119, 4), cellomusicmaker_three],
        [(122, 4), (126, 4), cellomusicmaker_one],
        [(128, 4), (131, 4), cellomusicmaker_three],
        [(132, 4), (134, 4), cellomusicmaker_four],
        [(139, 4), (140, 4), cellomusicmaker_four],
        [(144, 4), (146, 4), cellomusicmaker_four],
        [(146, 4), (149, 4), cellomusicmaker_four],
        [(150, 4), (153, 4), cellomusicmaker_four],#
        [(157, 4), (158, 4), cellomusicmaker_two],
        [(158, 4), (162, 4), cellomusicmaker_three],
        [(165, 4), (167, 4), cellomusicmaker_two],
        [(167, 4), (169, 4), cellomusicmaker_two],
        [(174, 4), (176, 4), cellomusicmaker_three],
        [(176, 4), (177, 4), cellomusicmaker_one],
        [(181, 4), (185, 4), cellomusicmaker_two],
        [(185, 4), (186, 4), cellomusicmaker_three],
    ]
])

###group two###
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
        [(0, 4), (3, 4), bowmaker],
        [(3, 4), (4, 4), bowmaker],
        [(4, 4), (5, 4), bowmaker],
        [(8, 4), (9, 4), bowmaker],
        [(9, 4), (12, 4), bowmaker],
        [(12, 4), (15, 4), bowmaker],
        [(20, 4), (23, 4), bowmaker],
        [(25, 4), (27, 4), bowmaker],
        [(27, 4), (29, 4), bowmaker],
        [(34, 4), (36, 4), bowmaker],
        [(36, 4), (40, 4), bowmaker],
        [(40, 4), (43, 4), bowmaker],
        [(48, 4), (51, 4), bowmaker],
        [(52, 4), (56, 4), bowmaker],
        [(58, 4), (60, 4), bowmaker],
        [(60, 4), (64, 4), bowmaker],
        [(64, 4), (66, 4), bowmaker],
        [(72, 4), (76, 4), bowmaker],
        [(76, 4), (79, 4), bowmaker],
        [(79, 4), (81, 4), bowmaker],
        [(81, 4), (82, 4), bowmaker],
        [(83, 4), (84, 4), bowmaker],
        [(84, 4), (88, 4), bowmaker],
        [(88, 4), (89, 4), bowmaker],
        [(90, 4), (91, 4), bowmaker],
        [(91, 4), (94, 4), bowmaker],
        [(94, 4), (96, 4), bowmaker],
        [(97, 4), (99, 4), bowmaker],
        [(99, 4), (103, 4), bowmaker],
        [(104, 4), (106, 4), bowmaker],
        [(106, 4), (110, 4), bowmaker],
        [(111, 4), (114, 4), bowmaker],
        [(115, 4), (117, 4), bowmaker],
        [(119, 4), (122, 4), bowmaker],
        [(125, 4), (127, 4), bowmaker],
        [(127, 4), (129, 4), bowmaker],
        [(133, 4), (136, 4), bowmaker],
        [(136, 4), (138, 4), bowmaker],
        [(143, 4), (146, 4), bowmaker],
        [(146, 4), (150, 4), bowmaker],
        [(150, 4), (154, 4), bowmaker],
        [(154, 4), (155, 4), bowmaker],
        [(157, 4), (158, 4), bowmaker],
        [(158, 4), (160, 4), bowmaker],
        [(164, 4), (167, 4), bowmaker],
        [(167, 4), (169, 4), bowmaker],
        [(171, 4), (172, 4), bowmaker],
        [(172, 4), (174, 4), bowmaker],
        [(178, 4), (180, 4), bowmaker],
        [(180, 4), (183, 4), bowmaker],
        [(185, 4), (189, 4), bowmaker],

    ]
])

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
        [(0, 4), (3, 4), cellomusicmaker_one],
        [(3, 4), (4, 4), cellomusicmaker_two],
        [(4, 4), (5, 4), cellomusicmaker_one],
        [(8, 4), (9, 4), cellomusicmaker_one],
        [(9, 4), (12, 4), cellomusicmaker_three],
        [(12, 4), (15, 4), cellomusicmaker_one],
        [(20, 4), (23, 4), cellomusicmaker_two],
        [(25, 4), (27, 4), cellomusicmaker_one],
        [(27, 4), (29, 4), cellomusicmaker_one],
        [(34, 4), (36, 4), cellomusicmaker_two],
        [(36, 4), (40, 4), cellomusicmaker_one],
        [(40, 4), (43, 4), cellomusicmaker_two],
        [(48, 4), (51, 4), cellomusicmaker_two],
        [(52, 4), (56, 4), cellomusicmaker_two],
        [(58, 4), (60, 4), cellomusicmaker_one],
        [(60, 4), (64, 4), cellomusicmaker_one],
        [(64, 4), (66, 4), cellomusicmaker_three],
        [(72, 4), (76, 4), cellomusicmaker_two],
        [(76, 4), (79, 4), cellomusicmaker_one],
        [(79, 4), (81, 4), cellomusicmaker_one],
        [(81, 4), (82, 4), cellomusicmaker_three],
        [(83, 4), (84, 4), cellomusicmaker_two],
        [(84, 4), (88, 4), cellomusicmaker_two],
        [(88, 4), (89, 4), cellomusicmaker_one],
        [(90, 4), (91, 4), cellomusicmaker_one],
        [(91, 4), (94, 4), cellomusicmaker_three],
        [(94, 4), (96, 4), cellomusicmaker_two],
        [(97, 4), (99, 4), cellomusicmaker_two],
        [(99, 4), (103, 4), cellomusicmaker_one],
        [(104, 4), (106, 4), cellomusicmaker_one],
        [(106, 4), (110, 4), cellomusicmaker_three],
        [(111, 4), (114, 4), cellomusicmaker_two],
        [(115, 4), (117, 4), cellomusicmaker_four],#
        [(119, 4), (122, 4), cellomusicmaker_four],
        [(125, 4), (127, 4), cellomusicmaker_four],
        [(127, 4), (129, 4), cellomusicmaker_four],
        [(133, 4), (136, 4), cellomusicmaker_four],
        [(136, 4), (138, 4), cellomusicmaker_four],
        [(143, 4), (146, 4), cellomusicmaker_four],
        [(146, 4), (150, 4), cellomusicmaker_four],
        [(150, 4), (154, 4), cellomusicmaker_four],#
        [(154, 4), (155, 4), cellomusicmaker_one],
        [(157, 4), (158, 4), cellomusicmaker_three],
        [(158, 4), (160, 4), cellomusicmaker_three],
        [(164, 4), (167, 4), cellomusicmaker_two],
        [(167, 4), (169, 4), cellomusicmaker_two],
        [(171, 4), (172, 4), cellomusicmaker_three],
        [(172, 4), (174, 4), cellomusicmaker_one],
        [(178, 4), (180, 4), cellomusicmaker_one],
        [(180, 4), (183, 4), cellomusicmaker_two],
        [(185, 4), (189, 4), cellomusicmaker_two],
        [(189, 4), (190, 4), silence_maker],
    ]
])

all_timespan_lists = {
    'Voice 1': voice_1_timespan_list,
    'Voice 2': voice_2_timespan_list,
    'Voice 3': voice_3_timespan_list,
    'Voice 4': voice_4_timespan_list,
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

score = abjad.Score([
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 1')],name='Staff 1', lilypond_type='BowStaff',),
            abjad.Staff([abjad.Voice(name='Voice 5')],name='Staff 5', lilypond_type='BeamStaff',),
            abjad.Staff([abjad.Voice(name='Voice 2')],name='Staff 2', lilypond_type='Staff',),
        ],
        name='Staff Group 1',
    ),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 3')],name='Staff 3', lilypond_type='BowStaff',),
            abjad.Staff([abjad.Voice(name='Voice 6')],name='Staff 6', lilypond_type='BeamStaff',),
            abjad.Staff([abjad.Voice(name='Voice 4')],name='Staff 4', lilypond_type='Staff',),
        ],
        name='Staff Group 2',
    )
],
)

for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context'].append(skip)

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

print('Adding Beam Staff ...')
voice_1_copy = abjad.mutate(score['Voice 1']).copy()
score['Voice 5'].extend([voice_1_copy[:]])

voice_3_copy = abjad.mutate(score['Voice 3']).copy()
score['Voice 6'].extend([voice_3_copy[:]])

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

print('Beaming runs ...')

for voice in abjad.select(score).components(abjad.Voice):
    for run in abjad.select(voice).runs():
        if 1 < len(run):
            specifier = abjadext.rmakers.BeamSpecifier(
                beam_each_division=True,
                )
            specifier(abjad.select(run))
            abjad.attach(abjad.StartBeam(), run[0])
            abjad.attach(abjad.StopBeam(), run[-1])

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

#attach instruments and clefs

print('Adding attachments ...')
bar_line = abjad.BarLine('|.')
section_bar_line = abjad.BarLine('||')
metro = abjad.MetronomeMark((1, 8), 60)
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

def _apply_numerators_and_tech(staff, nums, tech):
    numerators = cyc(nums)
    techs = cyc(tech)
    for logical_tie in abjad.select(staff).logical_ties(pitched=True):
        tech = next(techs)
        numerator = next(numerators)
        bcp = abjad.BowContactPoint((numerator, 5))
        technis = abjad.BowMotionTechnique(tech)
        for note in logical_tie:
            abjad.attach(bcp, note)
            abjad.attach(technis, note)
    for run in abjad.select(staff).runs():
        abjad.bow_contact_spanner(run, omit_bow_changes=False)

for voice in abjad.select(score['Voice 1']).components(abjad.Voice):
    seed(4)
    nums_random_walk = []
    nums_random_walk.append(-1 if random() < 0.5 else 1)
    for i in range(1, 1000):
        movement = -1 if random() < 0.5 else 1
        value = nums_random_walk[i-1] + movement
        nums_random_walk.append(value)
    nums_random_walk = [abs(x) for x in nums_random_walk]
    nums_chord = [0, 5, 3, 1, 4, 2, 5, 4, 3, 2]
    num_list = [nums_chord[x] for x in reduceMod9(nums_random_walk)]
    tech_list = ['ordinario', 'ordinario', 'ordinario', 'ordinario', 'circular', 'circular', 'ordinario', 'ordinario', 'ordinario', 'jete',  'ordinario', 'ordinario', 'ordinario', 'ordinario', 'ordinario', 'jete', 'jete', 'jete', 'jete',]
    _apply_numerators_and_tech(staff=voice, nums=num_list, tech=tech_list)

for voice in abjad.select(score['Voice 3']).components(abjad.Voice):
    seed(5)
    nums_random_walk = []
    nums_random_walk.append(-1 if random() < 0.5 else 1)
    for i in range(1, 1000):
        movement = -1 if random() < 0.5 else 1
        value = nums_random_walk[i-1] + movement
        nums_random_walk.append(value)
    nums_random_walk = [abs(x) for x in nums_random_walk]
    nums_chord = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
    num_list = [nums_chord[x] for x in reduceMod9(nums_random_walk)]
    tech_list = ['ordinario', 'ordinario', 'ordinario', 'ordinario', 'circular', 'circular', 'ordinario', 'ordinario', 'ordinario', 'jete',  'ordinario', 'ordinario', 'ordinario', 'ordinario', 'ordinario', 'jete', 'jete', 'jete', 'jete',]
    _apply_numerators_and_tech(staff=voice, nums=num_list, tech=tech_list)

def _apply_position_and_span(staff, poses):
    positions = cyc(poses)
    for run in abjad.select(staff).runs():
        span = abjad.StartTextSpan(
            left_text=abjad.Markup(next(positions)).upright(),
            right_text=abjad.Markup(next(positions)).upright(),
            style='dashed-line-with-arrow',
            )
        abjad.attach(span, run[0])
        abjad.attach(abjad.StopTextSpan(), run[-1])
        abjad.override(staff).text_spanner.staff_padding = 0

for voice in abjad.select(score['Voice 5']).components(abjad.Voice):
    pos_list_1 = ['st.', 'ord.', 'sp.', 'msp.', 'ord.',]
    _apply_position_and_span(staff=voice, poses=pos_list_1)

for voice in abjad.select(score['Voice 6']).components(abjad.Voice):
    pos_list_2 = ['sp.', 'msp.', 'ord.', 'st.', 'ord.',]
    _apply_position_and_span(staff=voice, poses=pos_list_2)

for voice in abjad.select(score['Voice 1']).components(abjad.Voice):
    for run in abjad.select(voice).runs():
        specifier = abjadext.rmakers.BeamSpecifier(
            beam_each_division=False,
            )
        specifier(run)

for voice in abjad.select(score['Voice 3']).components(abjad.Voice):
    for run in abjad.select(voice).runs():
        specifier = abjadext.rmakers.BeamSpecifier(
            beam_each_division=False,
            )
        specifier(run)

instruments1 = cyc([
    abjad.Cello(),
])

instruments2 = cyc([
    abjad.Cello(),
])

clefs1 = cyc([
    abjad.Clef('percussion'),
    abjad.Clef('percussion'),
    abjad.Clef('bass'),
])

clefs2 = cyc([
    abjad.Clef('percussion'),
    abjad.Clef('percussion'),
    abjad.Clef('bass'),
])

abbreviations1 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('B.H.'),),
    abjad.MarginMarkup(markup=abjad.Markup('vc.I'),),
    abjad.MarginMarkup(markup=abjad.Markup('L.H.'),),
])

abbreviations2 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('B.H.'),),
    abjad.MarginMarkup(markup=abjad.Markup('vc.II'),),
    abjad.MarginMarkup(markup=abjad.Markup('L.H.'),),
])

names1 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Bow Hand'),),
    abjad.StartMarkup(markup=abjad.Markup('Violoncello I'),),
    abjad.StartMarkup(markup=abjad.Markup('Left Hand'),),
])

names2 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Bow Hand'),),
    abjad.StartMarkup(markup=abjad.Markup('Violoncello II'),),
    abjad.StartMarkup(markup=abjad.Markup('Left Hand'),),
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

for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
    leaf1_start = abjad.select(staff).leaves()[7]
    leaf1 = abjad.select(staff).leaves()[8]
    abjad.attach(mark1, leaf1)
    abjad.attach(section_bar_line, leaf1_start)

for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
    leaf2_start = abjad.select(staff).leaves()[15]
    leaf2 = abjad.select(staff).leaves()[16]
    abjad.attach(mark2, leaf2)
    abjad.attach(section_bar_line, leaf2_start)

for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
    leaf3_start = abjad.select(staff).leaves()[23]
    leaf3 = abjad.select(staff).leaves()[24]
    abjad.attach(mark3, leaf3)
    abjad.attach(section_bar_line, leaf3_start)

for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
    leaf4_start = abjad.select(staff).leaves()[31]
    leaf4 = abjad.select(staff).leaves()[32]
    abjad.attach(mark4, leaf4)
    abjad.attach(section_bar_line, leaf4_start)

for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
    leaf5_start = abjad.select(staff).leaves()[38]
    leaf5 = abjad.select(staff).leaves()[39]
    abjad.attach(mark5, leaf5)
    abjad.attach(section_bar_line, leaf5_start)

score_file = abjad.LilyPondFile.new(
    score,
    includes=['first_stylesheet.ily', '/Users/evansdsg2/abjad/docs/source/_stylesheets/abjad.ily'],
    )

abjad.SegmentMaker.comment_measure_numbers(score)
###################

directory = '/Users/evansdsg2/Scores/cthar/cthar/Segments/Segment_I'
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

# for staff in abjad.iterate(score['Staff Group']).components(abjad.Staff):
#     abjad.show(staff)
# abjad.show(score)
# abjad.play(score)
