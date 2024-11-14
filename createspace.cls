\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{createspace}[2022/01/20 Create Space class]
\LoadClass[twoside, 9pt]{extarticle}

% to handle ą, ć, ę, etc.
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{polski}

% to make the text as compact as possible
\RequirePackage{Alegreya}
\RequirePackage[final]{microtype}
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

% https://tex.stackexchange.com/questions/22012/hyperref-and-imakeidx-do-not-work-together
\RequirePackage{imakeidx}

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

\usepackage[usenames, svgnames, table]{xcolor}
\definecolor{greenLeo}{RGB}{34, 139, 34} % Define the color used for highlighting throughout the book
\definecolor{purpleLeo}{RGB}{59, 40, 120} % Define the color used for highlighting throughout the book
\definecolor{orangeLeo}{RGB}{174, 118, 42} % Define the color used for highlighting throughout the book

\usepackage{mdframed}
\usepackage{xcolor}
\usepackage{tcolorbox}

\newcounter{counter}

\newtheorem{definitionT}[counter]{Definicja} % Theorems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newenvironment{definition}{\begin{definitionBox}\begin{definitionT}}{\end{definitionT}\end{definitionBox}}
\newmdenv[
	skipabove=\topskip, % Whitespace above box
	skipbelow=0pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=greenLeo, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=greenLeo!15, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=\topskip, % Inside top margin height
	innerbottommargin=\topskip, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{definitionBox}

\newtheorem{propositionT}[counter]{Fakt} % Theorems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newenvironment{proposition}{\begin{propositionBox}\begin{propositionT}}{\end{propositionT}\end{propositionBox}}
\newmdenv[
	skipabove=\topskip, % Whitespace above box
	skipbelow=0pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=purpleLeo, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=purpleLeo!30, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=10pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{propositionBox}

\newtheorem{corollaryT}[counter]{Wniosek} % Theorems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newenvironment{corollary}{\begin{corollaryBox}\begin{corollaryT}}{\end{corollaryT}\end{corollaryBox}}
\newmdenv[
	skipabove=\topskip, % Whitespace above box
	skipbelow=0pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=purpleLeo!50, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=purpleLeo!15!white, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=\topskip, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{corollaryBox}

\newtheorem{exerciseT}[counter]{Ćwiczenie} % Theorems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newenvironment{exercise}{\begin{exerciseBox}\begin{exerciseT}}{\end{exerciseT}\end{exerciseBox}}
\newmdenv[
	skipabove=\topskip, % Whitespace above box
	skipbelow=0pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=orangeLeo, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=orangeLeo!15, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=\topskip, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{exerciseBox}

\newenvironment{workinprogress}{\begin{tobedoneBox}\textbf{\color{red}{Do zrobienia}}. }{\end{tobedoneBox}}
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=red, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=red!15, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{tobedoneBox}

\newenvironment{clue}[1]{\begin{meaningBox}\textbf{\color{orangeLeo}{#1}} }{\end{meaningBox}}
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=orangeLeo, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=orangeLeo!15, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{meaningBox}

\newenvironment{fact}[1]{\begin{factBox}\textbf{\color{purpleLeo}{#1}}. }{\end{factBox}}
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=purpleLeo, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=purpleLeo!15, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{factBox}

\theoremstyle{plain}
\numberwithin{counter}{section}
\newtheorem{conjecture}[counter]{Hipoteza}
\newtheorem{example}[counter]{Przyk\l{}ad}
\newtheorem{lemma}[counter]{Lemat}
\newtheorem{theorem}[counter]{Twierdzenie}
\newtheorem{warning}[counter]{Uwaga}
\newtheorem{tobedone}[counter]{Wymaga przeredagowania}


% clickable links
% add [backref] for links from bib entries to citations
% add [pdfusetitle] for metadata
\RequirePackage[pdfusetitle]{hyperref}
\hypersetup{
    colorlinks,
    linkcolor={red!50!black},
    citecolor={blue!50!black},
    urlcolor={blue!80!black}
}

% https://www.reddit.com/r/LaTeX/comments/athzn1/replacing_leq_and_geq_with_leqslant_and_geqslant/
\let\savedleq=\leq %
\let\savedgeq=\geq %
\let\le=\leqslant %
\let\ge=\geqslant %