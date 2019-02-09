% 2018-07-17 19:54

\version "2.19.82"
\language "english"
#(set-default-paper-size "letter")
#(set-global-staff-size 20)
\include "ekmel.ily"
\ekmelicStyle evans
%{
\header {
	tagline = ##f
	breakbefore = ##t
	dedication = \markup \override #'(font-name . "Didot") \fontsize #12 \center-column {"H   a   m   o   n   s   h   ū"}
	title =  \markup { \epsfile #Y #34 #"/Users/evansdsg2/Scores/hamon_shu/Segments/Test/title2.eps" }
	subtitle = \markup \override #'(font-name . "Didot") \fontsize #7 \center-column {"s  t  r  i  n  g    q  u  a  r  t  e  t    n  o.   1"}
	subsubtitle = \markup \override #'(font-name . "Didot") \fontsize #2 \center-column {";       o  r       t  h  e       m  a  n  y       w  a  y  s       o  f       d  r  a  w  i  n  g       w  a  t  e  r"}
	arranger = \markup \override #'(font-name . "Didot") \fontsize #5 {"Gregory Rowland Evans"}
} %}

\layout {
    \accidentalStyle forget
	%\accidentalStyle modern
	%\accidentalStyle modern-cautionary
	%\accidentalStyle neo-modern
	%\accidentalStyle dodecaphonic
    indent = #5
	%ragged-last = ##t
    ragged-right = ##t
    %left-margin = #15
	\context {
        \name TimeSignatureContext
        \type Engraver_group
        \numericTimeSignature
        \consists Axis_group_engraver
		\consists Bar_number_engraver
        \consists Time_signature_engraver
		\consists Mark_engraver
		\consists Metronome_mark_engraver
		\override BarNumber.Y-extent = #'(0 . 0)
		\override BarNumber.Y-offset = 0
		\override BarNumber.extra-offset = #'(-4 . 0)
		%\override BarNumber.font-name = "Didot"
		\override BarNumber.stencil = #(make-stencil-boxer 0.1 0.7 ly:text-interface::print)
		\override BarNumber.font-size = 1
		\override BarNumber.padding = 4
		\override MetronomeMark.X-extent = #'(0 . 0)
		\override MetronomeMark.Y-extent = #'(0 . 0)
		\override MetronomeMark.break-align-symbols = #'(left-edge)
		\override MetronomeMark.extra-offset = #'(0 . 4)
		%\override MetronomeMark.font-size = 30
		\override RehearsalMark.stencil = #(make-stencil-circler 0.1 0.7 ly:text-interface::print)
		\override RehearsalMark.X-extent = #'(0 . 0)
		\override RehearsalMark.X-offset = 6
		\override RehearsalMark.Y-offset = -2.25
		\override RehearsalMark.break-align-symbols = #'(time-signature)
		\override RehearsalMark.break-visibility = #end-of-line-invisible
		\override RehearsalMark.font-name = "Didot"
		\override RehearsalMark.font-size = 8
		\override RehearsalMark.outside-staff-priority = 500
		\override RehearsalMark.self-alignment-X = #center
        \override TimeSignature.X-extent = #'(0 . 0)
        \override TimeSignature.X-offset = #ly:self-alignment-interface::x-aligned-on-self
        \override TimeSignature.Y-extent = #'(0 . 0)
		\override TimeSignature.Y-offset = -3
        \override TimeSignature.break-align-symbol = ##f
        \override TimeSignature.break-visibility = #end-of-line-invisible
        %\override TimeSignature.font-size = #6
        \override TimeSignature.self-alignment-X = #center
		\override TimeSignature.whiteout = ##t
        \override VerticalAxisGroup.default-staff-staff-spacing = #'((basic-distance . 0) (minimum-distance . 10) (padding . 6) (stretchability . 0))
    }
    \context {
        \Score
        \remove Bar_number_engraver
		\remove Mark_engraver
        \accepts TimeSignatureContext
		%{ \override BarLine.bar-extent = #'(-2 . 2)
        \override Beam.breakable = ##t
		\override Beam.concaveness = #10000
        \override Beam.beam-thickness = #0.7
        \override Beam.length-fraction = #1.4
        \override DynamicText.font-size = #-3
		\override Glissando.breakable = ##t
		\override MetronomeMark.font-size = 3
        \override SpacingSpanner.strict-grace-spacing = ##t
        \override SpacingSpanner.strict-note-spacing = ##t
        \override SpacingSpanner.uniform-stretching = ##t
        \override StaffGrouper.staff-staff-spacing = #'((basic-distance . 16) (minimum-distance . 16) (padding . 3))
		\override Stem.thickness = #0.55
        \override TupletBracket.bracket-visibility = ##t
        \override TupletBracket.minimum-length = #3
        \override TupletBracket.padding = #2
        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
		\override TextSpanner.Y-offset = 9
		\override TextSpanner.padding = #3
		proportionalNotationDuration = #(ly:make-moment 1 40)
        autoBeaming = ##f
        tupletFullLength = ##t %}
    }
	\context {
        \Voice
        \remove Forbid_line_break_engraver
    }
    \context {
        \Staff
        \remove Time_signature_engraver
    }
    \context {
        \RhythmicStaff
        \remove Time_signature_engraver
    }
       \context {
        \StaffGroup
    }
}

\paper {
	score-system-spacing = #'((basic-distance . 15) (minimum-distance . 15) (padding . 1))
	top-margin = 1.5\cm
	bottom-margin = 1.5\cm

	%top-margin = .90\in
	oddHeaderMarkup = \markup ""
	evenHeaderMarkup = \markup ""
	%{ oddFooterMarkup = \markup \fill-line {
    ""
    \concat {
      "Hamon shū ~"
	  \fontsize #2
	  \fromproperty #'page:page-number-string "~ Evans"
     }
    ""
  }
  evenFooterMarkup = \markup \fill-line {
    ""
	\concat { "Hamon shū ~" \fontsize #2
	\fromproperty #'page:page-number-string "~ Evans"
    } ""
  } %}
}
