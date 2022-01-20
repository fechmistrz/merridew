\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{createspace}[2022/01/20 Create Space class]
\LoadClass[twoside, 9pt]{extbook}

% to handle ą, ć, ę, etc.
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{polski}

% to make the text as compact as possible
\RequirePackage{Alegreya}
\RequirePackage[
    activate={true,nocompatibility},
    final,
    tracking=true,
    kerning=true,
    spacing=true,
    factor=1100,
    stretch=10,
    shrink=10
]{microtype}
\RequirePackage[compact]{titlesec}
\RequirePackage{paralist}

% popular page size in Amazon's KDP
\RequirePackage[
    paperwidth=6.14in,
    paperheight=9.21in,
    left=0.82in,
    right=0.695in,
    top=0.6in,
    bottom=0.71in,
    twoside,
    headsep=0.15in,
    includehead,
    includefoot
]{geometry}

\RequirePackage{fancyhdr}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[C]{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\pagestyle{fancy}
\fancyhead{}
\fancyfoot{}
% 341      Rozdział 7. Kalifat algebry | 7.2 Pierścień adeli              342 |
\fancyhead[LE]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RO]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.0pt}

% \DeclareMathOperator:
\RequirePackage{amsmath}
% \mathbb:
\RequirePackage{amssymb}
% \theoremstyle, \newtheorem:
\RequirePackage{amsthm}
% [H] for figure environment:
\RequirePackage{float}
% \subcaption for minipage inside figure:
\RequirePackage{subcaption} % captions to subfigures
% clickable links, add [backref] for links from bib entries to citations
\RequirePackage{hyperref}

\theoremstyle{plain}
\newcounter{counter}
\numberwithin{counter}{section}
\newtheorem{conjecture}[counter]{Hipoteza}
\newtheorem{corollary}[counter]{Wniosek}
\newtheorem{definition}[counter]{Definicja}
\newtheorem{example}[counter]{Przyk\l{}ad}
\newtheorem{lemma}[counter]{Lemat}
\newtheorem{proposition}[counter]{Fakt}
\newtheorem{theorem}{Twierdzenie}
\newtheorem{warning}[counter]{Uwaga}
\newtheorem{tobedone}[counter]{Wymaga przeredagowania}