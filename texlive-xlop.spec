Name:		texlive-xlop
Version:	56910
Release:	2
Summary:	Calculates and displays arithmetic operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/xlop
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Xlop (eXtra Large OPeration) will typeset arithmetic problems
either in-line or "as in school" (using French school
conventions). So for example, \opadd{2}{3} can give either
$2+3=5$ or something similar to: \begin{tabular}{r} 2\\ +3\\
\hline 5\end{tabular}. Furthermore, numbers may be very large,
e.g 200 figures (with a very long compilation time). Many other
features allow to deal with numbers (tests, display, some high
level operations, etc.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xlop
%doc %{_texmfdistdir}/doc/generic/xlop

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
