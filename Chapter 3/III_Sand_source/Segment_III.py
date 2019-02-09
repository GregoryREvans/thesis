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

# Define the time signatures we would like to apply against the timespan structure.

time_signatures = [
    abjad.TimeSignature(pair) for pair in [
        (9, 8), (6, 8), (5, 4), (4, 4), (6, 8),
        (3, 8), (4, 4), (3, 4), (5, 8), (4, 4),
        (11, 8),
    ]
]

bounds = abjad.mathtools.cumulative_sums([_.duration for _ in time_signatures])

#Define Pitch Material

def reduceMod1(rw):
    return [(x % 2) for x in rw]

def reduceMod3(rw):
    return [(x % 4) for x in rw]

def reduceMod5(rw):
    return [(x % 6) for x in rw]

def reduceMod7(rw):
    return [(x % 8) for x in rw]

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
flute_random_walk_one = []
flute_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = flute_random_walk_one[i-1] + movement
    flute_random_walk_one.append(value)
flute_random_walk_one = [abs(x) for x in flute_random_walk_one]
flute_chord_one = [2, 11, 12, 20, 31, 20, 12, 11, ]
flute_notes_one = [flute_chord_one[x] for x in reduceMod7(flute_random_walk_one)]

seed(4)
saxophone_random_walk_one = []
saxophone_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = saxophone_random_walk_one[i-1] + movement
    saxophone_random_walk_one.append(value)
saxophone_random_walk_one = [abs(x) for x in saxophone_random_walk_one]
saxophone_chord_one = [-10, 2, 11, 12, 1, 2, ]
saxophone_notes_one = [saxophone_chord_one[x] for x in reduceMod5(saxophone_random_walk_one)]

seed(8)
cello_random_walk_one = []
cello_random_walk_one.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_one[i-1] + movement
    cello_random_walk_one.append(value)
cello_random_walk_one = [abs(x) for x in cello_random_walk_one]
cello_chord_one = [-18, -10, 2, -10, ]
cello_notes_one = [cello_chord_one[x] for x in reduceMod3(cello_random_walk_one)]

seed(1)
flute_random_walk_two = []
flute_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = flute_random_walk_two[i-1] + movement
    flute_random_walk_two.append(value)
flute_random_walk_two = [abs(x) for x in flute_random_walk_two]
flute_chord_two = [2, 12, 31, 12, ]
flute_notes_two = [flute_chord_two[x] for x in reduceMod3(flute_random_walk_two)]

seed(4)
saxophone_random_walk_two = []
saxophone_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = saxophone_random_walk_two[i-1] + movement
    saxophone_random_walk_two.append(value)
saxophone_random_walk_two = [abs(x) for x in saxophone_random_walk_two]
saxophone_chord_two = [11, 20, ]
saxophone_notes_two = [saxophone_chord_two[x] for x in reduceMod1(saxophone_random_walk_two)]

seed(8)
cello_random_walk_two = []
cello_random_walk_two.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_two[i-1] + movement
    cello_random_walk_two.append(value)
cello_random_walk_two = [abs(x) for x in cello_random_walk_two]
cello_chord_two = [-18, 2, ]
cello_notes_two = [cello_chord_two[x] for x in reduceMod1(cello_random_walk_two)]

seed(1)
flute_random_walk_three = []
flute_random_walk_three.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = flute_random_walk_three[i-1] + movement
    flute_random_walk_three.append(value)
flute_random_walk_three = [abs(x) for x in flute_random_walk_three]
flute_chord_three = [11, 20, ]
flute_notes_three = [flute_chord_three[x] for x in reduceMod1(flute_random_walk_three)]

seed(4)
saxophone_random_walk_three = []
saxophone_random_walk_three.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = saxophone_random_walk_three[i-1] + movement
    saxophone_random_walk_three.append(value)
saxophone_random_walk_three = [abs(x) for x in saxophone_random_walk_three]
saxophone_chord_three = [2, 12, ]
saxophone_notes_three = [saxophone_chord_three[x] for x in reduceMod1(saxophone_random_walk_three)]

seed(8)
cello_random_walk_three = []
cello_random_walk_three.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = cello_random_walk_three[i-1] + movement
    cello_random_walk_three.append(value)
cello_random_walk_three = [abs(x) for x in cello_random_walk_three]
cello_notes_three = [-10, ]

# Define rhythm-makers: two to be sued by the MusicMaker, one for silence.

rmaker_one = abjadext.rmakers.TaleaRhythmMaker(
    talea=abjadext.rmakers.Talea(
        counts=[2, 1, 3, 2, 2, 3, 1, ],
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

rmaker_two = abjadext.rmakers.TaleaRhythmMaker(
    talea=abjadext.rmakers.Talea(
        counts=[1, 2, 2, 3, 3, 3, 2, 2, 1, ],
        denominator=16,
        ),
    beam_specifier=abjadext.rmakers.BeamSpecifier(
        beam_divisions_together=True,
        beam_rests=False,
        ),
    extra_counts_per_division=[1, 0, -1, 0],
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

rmaker_three = abjadext.rmakers.EvenDivisionRhythmMaker(
    denominators=[16, 16, 8, 16, 16, 8],
    extra_counts_per_division=[1, 0, 0, -1, 0, 1, -1, 0],
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

# Initialize AttachmentHandler

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

# Initialize MusicMakers with the rhythm-makers.
#####oboe#####
flutemusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=flute_notes_one,
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
    pitches=flute_notes_three,
    continuous=True,
    attachment_handler=attachment_handler_three,
)
#####saxophone#####
saxophonemusicmaker_one = MusicMaker(
    rmaker=rmaker_one,
    pitches=saxophone_notes_one,
    continuous=True,
    attachment_handler=attachment_handler_one,
)
saxophonemusicmaker_two = MusicMaker(
    rmaker=rmaker_two,
    pitches=saxophone_notes_two,
    continuous=True,
    attachment_handler=attachment_handler_two,
)
saxophonemusicmaker_three = MusicMaker(
    rmaker=rmaker_three,
    pitches=saxophone_notes_three,
    continuous=True,
    attachment_handler=attachment_handler_three,
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

silence_maker = abjadext.rmakers.NoteRhythmMaker(
    division_masks=[
        abjadext.rmakers.SilenceMask(
            pattern=abjad.index([0], 1),
            ),
        ],
    )

# Define a small class so that we can annotate timespans with additional
# information:


class MusicSpecifier:

    def __init__(self, music_maker, voice_name):
        self.music_maker = music_maker
        self.voice_name = voice_name

# Define an initial timespan structure, annotated with music specifiers. This
# structure has not been split along meter boundaries. This structure does not
# contain timespans explicitly representing silence. Here I make four, one
# for each voice, using Python's list comprehension syntax to save some
# space.

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
    [(9, 8), (12, 8), flutemusicmaker_one],
    [(20, 8), (24, 8), flutemusicmaker_two],
    [(31, 8), (33, 8), flutemusicmaker_three],
    [(33, 8), (36, 8), flutemusicmaker_one],
    [(42, 8), (48, 8), flutemusicmaker_two],
    [(53, 8), (56, 8), flutemusicmaker_three],
    [(56, 8), (60, 8), flutemusicmaker_one],
    [(64, 8), (69, 8), flutemusicmaker_two],
    [(69, 8), (72, 8), flutemusicmaker_three],
    [(75, 8), (79, 8), flutemusicmaker_one],
    ]
])

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
    [(15, 8), (18, 8), saxophonemusicmaker_one],
    [(18, 8), (22, 8), saxophonemusicmaker_two],
    [(25, 8), (29, 8), saxophonemusicmaker_three],
    [(29, 8), (32, 8), saxophonemusicmaker_one],
    [(35, 8), (39, 8), saxophonemusicmaker_two],
    [(39, 8), (42, 8), saxophonemusicmaker_three],
    [(45, 8), (50, 8), saxophonemusicmaker_one],
    [(50, 8), (52, 8), saxophonemusicmaker_two],
    [(55, 8), (56, 8), saxophonemusicmaker_three],
    [(56, 8), (61, 8), saxophonemusicmaker_one],
    [(61, 8), (62, 8), saxophonemusicmaker_two],
    [(65, 8), (69, 8), saxophonemusicmaker_three],
    [(69, 8), (72, 8), saxophonemusicmaker_one],
    [(75, 8), (79, 8), saxophonemusicmaker_two],
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
    [(0, 8), (3, 8), cellomusicmaker_one],
    [(4, 8), (8, 8), cellomusicmaker_two],
    [(10, 8), (12, 8), cellomusicmaker_three],
    [(12, 8), (15, 8), cellomusicmaker_one],
    [(18, 8), (24, 8), cellomusicmaker_two],
    [(28, 8), (33, 8), cellomusicmaker_three],
    [(33, 8), (35, 8), cellomusicmaker_one],
    [(40, 8), (42, 8), cellomusicmaker_two],
    [(42, 8), (44, 8), cellomusicmaker_three],
    [(44, 8), (48, 8), cellomusicmaker_one],
    [(54, 8), (55, 8), cellomusicmaker_two],
    [(62, 8), (64, 8), cellomusicmaker_three],
    [(72, 8), (75, 8), cellomusicmaker_one],
    [(76, 8), (79, 8), cellomusicmaker_two],
    [(79, 8), (80, 8), silence_maker],
    ]
])

# Create a dictionary mapping voice names to timespan lists so we can
# maintain the association in later operations:

all_timespan_lists = {
    'Voice 1': voice_1_timespan_list,
    'Voice 3': voice_3_timespan_list,
    'Voice 8': voice_8_timespan_list,
}

# Determine the "global" timespan of all voices combined:

global_timespan = abjad.Timespan(
    start_offset=0,
    stop_offset=max(_.stop_offset for _ in all_timespan_lists.values())
)

# Using the global timespan, create silence timespans for each timespan list.
# We don't need to create any silences by-hand if we now the global start and
# stop offsets of all voices combined:

for voice_name, timespan_list in all_timespan_lists.items():
    # Here is another technique for finding where the silence timespans are. We
    # create a new timespan list consisting of the global timespan and all the
    # timespans from our current per-voice timespan list. Then we compute an
    # in-place logical XOR. The XOR will replace the contents of the "silences"
    # timespan list with a set of timespans representing those periods of time
    # where only one timespan from the original was present. This has the
    # effect of cutting out holes from the global timespan wherever a per-voice
    # timespan was found, but also preserves any silence before the first
    # per-voice timespan or after the last per-voice timespan. Then we merge
    # the newly-created silences back into the per-voice timespan list.
    silences = abjad.TimespanList([global_timespan])
    silences.extend(timespan_list)
    silences.sort()
    silences.compute_logical_xor()
    # Add the silences into the voice timespan list. We create new *annotated*
    # timespans so we can maintain the voice name information:
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

# Split the timespan list via the time signatures and collect the shards into a
# new timespan list

for voice_name, timespan_list in all_timespan_lists.items():
    shards = timespan_list.split_at_offsets(bounds)
    split_timespan_list = abjad.TimespanList()
    for shard in shards:
        split_timespan_list.extend(shard)
    split_timespan_list.sort()
    # We can replace the original timespan list in the dictionary of
    # timespan lists because we know the key it was stored at (its voice
    # name):
    all_timespan_lists[voice_name] = timespan_list

# Create a score structure

score = abjad.Score([
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name='Voice 1')],name='Staff 1', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 3')],name='Staff 3', lilypond_type='Staff',),
            abjad.Staff([abjad.Voice(name='Voice 8')],name='Staff 8', lilypond_type='Staff',),
        ],
        name='Staff Group 1',
    ),
],
)

# Teach each of the staves how to draw analysis brackets

# for staff in score['Staff Group']:
#     staff.consists_commands.append('Horizontal_bracket_engraver')

# Add skips and time signatures to the global context

for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context'].append(skip)

# Define a helper function that takes a rhythm maker and some durations and
# outputs a container. This helper function also adds LilyPond analysis
# brackets to make it clearer where the phrase and sub-phrase boundaries are.

print('Making containers ...')

def make_container(music_maker, durations):
    selections = music_maker(durations)
    container = abjad.Container([])
    container.extend(selections)
    # # Add analysis brackets so we can see the phrasing graphically
    # start_indicator = abjad.LilyPondLiteral('\startGroup', format_slot='after')
    # stop_indicator = abjad.LilyPondLiteral('\stopGroup', format_slot='after')
    # for cell in selections:
    #     cell_first_leaf = abjad.select(cell).leaves()[0]
    #     cell_last_leaf = abjad.select(cell).leaves()[-1]
    #     abjad.attach(start_indicator, cell_first_leaf)
    #     abjad.attach(stop_indicator, cell_last_leaf)
    # # The extra space in the literals is a hack around a check for whether an
    # # identical object has already been attached
    # start_indicator = abjad.LilyPondLiteral('\startGroup ', format_slot='after')
    # stop_indicator = abjad.LilyPondLiteral('\stopGroup ', format_slot='after')
    # phrase_first_leaf = abjad.select(container).leaves()[0]
    # phrase_last_leaf = abjad.select(container).leaves()[-1]
    # abjad.attach(start_indicator, phrase_first_leaf)
    # abjad.attach(stop_indicator, phrase_last_leaf)
    return container

# Loop over the timespan list dictionaries, spitting out pairs of voice
# names and per-voice timespan lists. Group timespans into phrases, with
# all timespans in each phrase having an identical rhythm maker. Run the
# rhythm maker against the durations of the timespans in the phrase and
# add the output to the voice with the timespan lists's voice name.

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
        # We know the voice name of each timespan because a) the timespan
        # list is in a dictionary, associated with that voice name and b)
        # each timespan's annotation is a MusicSpecifier instance which
        # knows the name of the voice the timespan should be used for.
        # This double-reference to the voice is redundant here, but in a
        # different implementation we could put *all* the timespans into
        # one timespan list, split them, whatever, and still know which
        # voice they belong to because their annotation records that
        # information.
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

#attach instruments and clefs

print('Adding attachments ...')
bar_line = abjad.BarLine('||')
metro = abjad.MetronomeMark((1, 4), 60)
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

instruments1 = cyc([
    abjad.Flute(),
    abjad.AltoSaxophone(),
    abjad.Cello(),
])

clefs1 = cyc([
    abjad.Clef('treble'),
    abjad.Clef('treble'),
    abjad.Clef('bass'),
])

abbreviations1 = cyc([
    abjad.MarginMarkup(markup=abjad.Markup('fl.'),),
    abjad.MarginMarkup(markup=abjad.Markup('sx.'),),
    abjad.MarginMarkup(markup=abjad.Markup('vc.'),),
])

names1 = cyc([
    abjad.StartMarkup(markup=abjad.Markup('Flute'),),
    abjad.StartMarkup(markup=abjad.Markup('Saxophone'),),
    abjad.StartMarkup(markup=abjad.Markup('Violoncello'),),
])

for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    leaf1 = abjad.select(staff).leaves()[0]
    abjad.attach(next(instruments1), leaf1)
    abjad.attach(next(abbreviations1), leaf1)
    abjad.attach(next(names1), leaf1)
    abjad.attach(next(clefs1), leaf1)

for staff in abjad.select(score['Staff Group 1']).components(abjad.Staff)[0]:
    leaf1 = abjad.select(staff).leaves()[0]
    last_leaf = abjad.select(staff).leaves()[-1]
    #abjad.attach(metro, leaf1)
    abjad.attach(bar_line, last_leaf)

# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf1 = abjad.select(staff).leaves()[7]
#     abjad.attach(mark1, leaf1)
#
# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf2 = abjad.select(staff).leaves()[16]
#     abjad.attach(mark2, leaf2)
#
# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf3 = abjad.select(staff).leaves()[22]
#     abjad.attach(mark3, leaf3)
#
# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf4 = abjad.select(staff).leaves()[29]
#     abjad.attach(mark4, leaf4)
#
# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf5 = abjad.select(staff).leaves()[34]
#     abjad.attach(mark5, leaf5)
#
# for staff in abjad.iterate(score['Global Context']).components(abjad.Staff):
#     leaf6 = abjad.select(staff).leaves()[39]
#     abjad.attach(mark6, leaf6)

for staff in abjad.iterate(score['Staff Group 1']).components(abjad.Staff):
    abjad.Instrument.transpose_from_sounding_pitch(staff)

# Make a lilypond file and show it:

score_file = abjad.LilyPondFile.new(
    score,
    includes=['first_stylesheet.ily', '/Users/evansdsg2/abjad/docs/source/_stylesheets/abjad.ily'],
    )

abjad.SegmentMaker.comment_measure_numbers(score)
###################

directory = '/Users/evansdsg2/Scores/four_ages_of_sand/four_ages_of_sand/Segments/Segment_III'
pdf_path = f'{directory}/Segment_III.pdf'
path = pathlib.Path('Segment_III.pdf')
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
