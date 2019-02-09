"""
    select() and iterate() both allow one to isolate items of a passage in iterable form for processing, 
    but in different forms.  select() renders the target as a Selection() (a sort of list or sequence), 
    while iterate() renders the target as a iterator (specifically, a generator).  That's really the heart of 
    the difference: lists vs generators.  Looking inside the definition of Selection() reveals many special methods 
    like __getitem__, __iter__, __add__, __contains__, __len__, __radd__ -- all of which allow the class 
    to behave like a list. Iteration() on the other hand has none of these but, in the main methods,  
    many, many yield statements instead. 

"""

"""
    Simple listcomp vs genexpr example to illustrate the difference. 

        >>> a = [9, 10, 2, 1, 5, 6]
        >>> b = [(0 - n) % 12 for n in a]
        >>> b
        [3, 2, 10, 11, 7, 6]
        >>> b[0]
        3
        >>> b[3]
        11
        >>> 

        >>> b = ((0 - n) % 12 for n in a)
        >>> b
        <generator object <genexpr> at 0x10075c990>
        >>>
        >>> b[0]
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: 'generator' object is not subscriptable
        >>>
        >>> b = [i for i in b]
        >>> b
        [3, 2, 10, 11, 7, 6]
        >>> b[0]
        3
        >>> b[3]
        11
        >>> 

"""

"""
    The difference can be seen when trying to view the representation of the class

        >>> chord = [i - 24 for i in mtools.unmod([9, 10, 2, 1, 5, 6, 0, 11, 7, 8, 4, 3])]
        >>> mapped_sets = mtools.map_sets(chord, [mtools.transpose([0, 1, 2, 4, 6, 7], n) for n in range(12)])
        >>>
        >>> sorted_sets = sorted(
        ...    mtools.noramlize_registers([mtools.reduce_chord(tset) for tset in mapped_sets]),
        ...    key=lambda x: (max(x) - min(x)),
        ...    reverse=True,
        ...    )
        >>>
        >>> voice_list = mtools.collect_horizontals(sorted_sets)
        >>> notes = [[abjad.Note(n, abjad.Duration(1, 1)) for n in lst] for lst in voice_list][-1::-1]
        >>>
        >>> group = mtools.make_staff_group(notes)
        >>> 
        >>> abjad.iterate(group).components(abjad.Staff)
        <generator object Iteration.components at 0x104c10888>
        >>>
        >>> format(abjad.select(group).components(abjad.Staff))
        abjad.Selection(
            [
                abjad.Staff(
                    "e''''1 af'''1 g'''1 ef'''1 ~ ef'''1 e'''1 ef'''1 ~ ef'''1 e'''1 ef'''1 ~ ef'''1 af''1",
                    lilypond_type='Staff',
                    ),
                abjad.Staff(
                    "g'''1 ~ g'''1 b''1 e''1 ~ e''1 af''1 ~ af''1 e''1 b''1 ~ b''1 af''1 g''1",
                    lilypond_type='Staff',
                    ),
                abjad.Staff(
                    "c'''1 b''1 c''1 af'1 g'1 b'1 c''1 b'1 c''1 ~ c''1 g''1 c''1",
                    lilypond_type='Staff',
                    ),
                abjad.Staff(
                    "fs''1 cs''1 fs'1 ~ fs'1 f'1 fs'1 d'1 cs'1 f'1 fs'1 f''1 fs'1",
                    lilypond_type='Staff',
                    ),
                abjad.Staff(
                    "cs''1 d'1 f'1 d'1 bf1 f'1 bf1 ~ bf1 d'1 f'1 cs''1 cs'1",
                    lilypond_type='Staff',
                    ),
                abjad.Staff(
                    "d'1 a1 ~ a1 ~ a1 ~ a1 bf1 a1 ~ a1 bf1 cs'1 d'1 bf1",
                    lilypond_type='Staff',
                    ),
                ]
            )
        >>>
"""

"""
    Here is an instance where select is more useful. Rather than iterating through the leaves, 
    I am accessing the the leaves in sequence via a range object and indexing, comparing them to 
    surrounding leaves.  (And of course, select has a built in method for doing this sort of 
    thing as well: select(notes).leaf(n) ).

        >>> for staff in group:
        ...     notes = abjad.select(staff).leaves()
        ...     for i in range(len(notes) - 1):
        ...         if all(isinstance(note, abjad.Note) for note in (notes[i], notes[i+1])) \
        ...         and notes[i+1].written_pitch == notes[i].written_pitch:
        ...             abjad.attach(abjad.TieIndicator(), notes[i])
        >>>


    Selections allow materials to be grouped into selection lists which can make them easier 
    to manage and also allow them to place nicely with containers and staves. It also allows multiple items 
    that fit the same criteria to be collected into a selection to which some transformation can be applied 
    to them at once -  something that would require loops and conditionals if using iterate().


"""