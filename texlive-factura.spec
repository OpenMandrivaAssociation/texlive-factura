# revision 30167
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-factura
Version:	20131012
Release:	4
Summary:	TeXLive factura package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/factura.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/factura.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive factura package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/factura/factura.cls
%{_texmfdistdir}/tex/latex/factura/factura.def
%doc %{_texmfdistdir}/doc/latex/factura/README
%doc %{_texmfdistdir}/doc/latex/factura/factura-modelo-ya.tex
%doc %{_texmfdistdir}/doc/latex/factura/factura-modelo.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
