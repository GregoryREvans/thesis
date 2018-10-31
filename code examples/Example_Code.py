import abjad

# ###NOTE CREATION###
# note = abjad.Note()
# abjad.show(note)
#
# note = abjad.Note(11, abjad.Duration(1, 8))
# abjad.show(note)
#
# #Slow Note Creation
# note_1 = abjad.Note(0, abjad.Duration(1, 4))
# note_2 = abjad.Note(1, abjad.Duration(1, 4))
# note_3 = abjad.Note(2, abjad.Duration(1, 2))
# notes = [note_1, note_2, note_3]
# staff = abjad.Staff(notes)
# abjad.show(staff)
#
# #Faster Note Creation
# numerators = [1, 1, 1, ]
# denominators = [4, 4, 2, ]
# durations = [abjad.Duration(y, z) for y, z in zip(numerators, denominators)]
# pitches = [0, 1, 2, ]
# notes = [abjad.Note(x, y) for x, y in zip(pitches, durations)]
# note_staff = abjad.Staff(notes)
# abjad.show(note_staff)
#
# ###BOW STAFF OPTIONS###
# #Slow bow_staff
# bow_staff = abjad.Staff()
# bow_staff.extend(r"c'4 c'4 c'4 c'4")
# indicator_1 = abjad.BowContactPoint((3, 3))
# indicator_2 = abjad.BowContactPoint((2, 3))
# indicator_3 = abjad.BowContactPoint((1, 3))
# indicator_4 = abjad.BowContactPoint((0, 3))
# abjad.attach(indicator_1, bow_staff[0])
# abjad.attach(indicator_2, bow_staff[1])
# abjad.attach(indicator_3, bow_staff[2])
# abjad.attach(indicator_4, bow_staff[3])
# abjad.bow_contact_spanner(bow_staff, omit_bow_changes=True)
# abjad.show(bow_staff)
#
# #Faster bow_staff
# new_bow_staff = abjad.Staff()
# new_bow_staff.extend(r"c'4 c'4 c'4 c'4")
# indicator_1 = abjad.BowContactPoint((3, 3))
# indicator_2 = abjad.BowContactPoint((2, 3))
# indicator_3 = abjad.BowContactPoint((1, 3))
# indicator_4 = abjad.BowContactPoint((0, 3))
# indicators = [indicator_1, indicator_2, indicator_3, indicator_4, ]
# leaves = abjad.select(new_bow_staff).leaves()
# for leaf, indicator in zip(leaves, indicators):
#     abjad.attach(indicator, leaf)
# abjad.bow_contact_spanner(new_bow_staff, omit_bow_changes=True)
# abjad.show(new_bow_staff)
#
# #Alternative Faster bow_staff
# new_bow_staff = abjad.Staff()
# new_bow_staff.extend(r"c'4 c'4 c'4 c'4")
# numerators = [3, 2, 1, 0, ]
# indicators = [(abjad.BowContactPoint((numerator, 3))) for numerator in numerators]
# leaves = abjad.select(new_bow_staff).leaves()
# for leaf, indicator in zip(leaves, indicators):
#     abjad.attach(indicator, leaf)
# abjad.bow_contact_spanner(new_bow_staff, omit_bow_changes=True)
# abjad.show(new_bow_staff)
#
# #Even Faster bow_staff
# newer_bow_staff = abjad.Staff()
# newer_bow_staff.extend(r"c'4 c'4 c'4 c'4")
# leaves = abjad.select(newer_bow_staff).leaves()
# indicator_numerators = [3, 2, 1, 0, ]
# for leaf, numerator in zip(leaves, indicator_numerators):
#     abjad.attach(abjad.BowContactPoint((numerator, 3)), leaf)
# abjad.bow_contact_spanner(newer_bow_staff, omit_bow_changes=True)
# abjad.show(newer_bow_staff)
#
###DYNAMIC ATTACHMENT###
#Slow dynamics
dynamic_staff = abjad.Staff()
dynamic_staff.extend(r"c'4 cs'4 d'2")
piano = abjad.Dynamic('p')
mezzo_forte = abjad.Dynamic('mf')
forte = abjad.Dynamic('f')
abjad.attach(piano, dynamic_staff[0])
abjad.attach(mezzo_forte, dynamic_staff[1])
abjad.attach(forte, dynamic_staff[2])
abjad.show(dynamic_staff)

#Faster dynamics
new_staff = abjad.Staff()
new_staff.extend(r"c'4 cs'4 d'2")
dynamics = ['p', 'mf', 'f', ]
leaves = abjad.select(new_staff).leaves()
for leaf, dynamic in zip(leaves, dynamics):
    abjad.attach(abjad.Dynamic(dynamic), leaf)
abjad.show(new_staff)

#Behavioral Dynamics
music_staff = abjad.Staff()
music_staff.extend(r"c'4 cs'4 d'2 r4 ds'2. e'8 f'8 fs'8 g'8 gs'8 r4. a'1")
for run in abjad.select(music_staff).runs():
    if len(run) > 3:
        leaves = abjad.select(run).leaves()
        abjad.attach(abjad.Dynamic('mf'), run[0])
        for leaf in leaves:
            abjad.attach(abjad.Articulation('tenuto'), leaf)
    elif len(run) == 3:
        abjad.attach(abjad.Dynamic('f'), run[0])
        abjad.attach(abjad.StartHairpin('>'), run[0])
        abjad.attach(abjad.Dynamic('mp'), run[-1])
    elif len(run) == 1:
        abjad.attach(abjad.Dynamic('ppp'), run[0])
abjad.show(music_staff)
