\version "2.19.82"  %! LilyPondFile
\language "english" %! LilyPondFile
\include "first_stylesheet.ily"
\header { %! LilyPondFile
    tagline = ##f
} %! LilyPondFile

\layout {}

\paper {}

\score { %! LilyPondFile
    \new Score
    <<
        \context TimeSignatureContext = "Global Context"
        {
            \time 4/4
            s1 * 1
            \time 5/4
            s1 * 5/4
        }
        \context Staff = "Staff 1"
        {
            \context Voice = "Voice 1"
            {
                {
                    c'16
                    [
                    cs'16
                    ~
                    cs'16
                    d'16
                    ~
                    d'8
                    ef'8
                    ~
                    \times 4/5 {
                        ef'8
                        e'16
                        c'8
                    }
                    cs'8.
                    d'16
                    ]
                }
                {
                    r2
                }
                {
                    e'8
                    [
                    ef'8
                    d'8
                    cs'8
                    ]
                }
                {
                    r4
                }
            }
        }
    >>
} %! LilyPondFile