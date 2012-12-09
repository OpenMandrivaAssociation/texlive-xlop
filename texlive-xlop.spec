# revision 22096
# category Package
# catalog-ctan /macros/generic/xlop
# catalog-date 2011-04-16 11:58:01 +0200
# catalog-license lppl
# catalog-version 0.24
Name:		texlive-xlop
Version:	0.24
Release:	2
Summary:	Calculates and displays arithmetic operations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/xlop
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xlop.source.tar.xz
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
%{_texmfdistdir}/tex/generic/xlop/xlop.sty
%{_texmfdistdir}/tex/generic/xlop/xlop.tex
%doc %{_texmfdistdir}/doc/generic/xlop/LISEZ.MOI
%doc %{_texmfdistdir}/doc/generic/xlop/README
%doc %{_texmfdistdir}/doc/generic/xlop/xlop-doc-fr.pdf
%doc %{_texmfdistdir}/doc/generic/xlop/xlop-doc-fr.tex
%doc %{_texmfdistdir}/doc/generic/xlop/xlop-doc.pdf
%doc %{_texmfdistdir}/doc/generic/xlop/xlop-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/xlop/manual.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.24-2
+ Revision: 757661
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.24-1
+ Revision: 719942
- texlive-xlop
- texlive-xlop
- texlive-xlop

