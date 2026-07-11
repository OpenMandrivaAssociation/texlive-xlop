%global tl_name xlop
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.28
Release:	%{tl_revision}.1
Summary:	Calculates and displays arithmetic operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/xlop
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Xlop (eXtra Large OPeration) will typeset arithmetic problems either in-
line or "as in school" (using French school conventions). So for
example, \opadd{2}{3} can give either $2+3=5$ or something similar to:
\begin{tabular}{r} 2\\ +3\\ \hline 5\end{tabular}. Furthermore, numbers
may be very large, e.g 200 figures (with a very long compilation time).
Many other features allow to deal with numbers (tests, display, some
high level operations, etc.)

