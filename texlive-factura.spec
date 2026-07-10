%global tl_name factura
%global tl_revision 61697

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.32
Release:	%{tl_revision}.1
Summary:	Typeset and calculate invoices according to Venezuelan law
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/factura
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/factura.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/factura.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/factura.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
'factura' is the Spanish word for 'invoice', so this is a LaTeX class
for typesetting and calculating invoices, taking into account
requirements of SENIAT legislation (tax collector entity on the
Bolivarian Republic of Venezuela). However, its use is not restricted to
Venezuela because all variables and the displayed text can be redefined
by invoking commands or editing.

