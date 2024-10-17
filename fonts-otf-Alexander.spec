%define fontname	Alexander
%define name		fonts-otf-%{fontname}
%define version		3.01
%define release		3

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Alexander fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		https://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
A text typeface using the Greek letters designed by Alexander Wilson
(1714-1786), a Scottish doctor, astronomer, and typefounder. The type
was especially designed for an edition of Homer's epics, published in
1756-8 by Andrew and Robert Foulis, printers to the University of
Glasgow. A modern revival, Wilson Greek, has been designed by Matthew
Carter in 1995. Peter S. Baker is also using Wilson's Greek type in
his Junicode font for medieval scholars (2007). Latin and Cyrillic are
based on a Garamond typeface. The font covers the Windows Glyph List,
IPA Extensions, Greek Extended, Ancient Greek Numbers, Byzantine and
Ancient Greek Musical Notation, various typographic extras and several
Open Type features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures,
Historical Forms, Stylistic Alternates, Ligatures).

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 3.01-2mdv2011.0
+ Revision: 675503
- br fontconfig for fc-query used in new rpm-setup-build

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 3.01-1mdv2011.0
+ Revision: 562703
- import fonts-otf-Alexander

