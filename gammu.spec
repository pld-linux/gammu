Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzêdzi dla telefonów komórkowych Nokia
Name:		mygnokii2
Version:	0.58
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://marcin-wiacek.fkn.pl/english/zips/%{name}.tar.gz
Source1:	%{name}-config.h
Source2:	%{name}-manpage
URL:		http://marcin-wiacek.topnet.pl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyGnokii2 is a Linux/Unix tool suite and (eventually) modem/fax driver
for Nokia's mobile phones, released under the GPL. See
docs/develop.txt: and Q. Why mygnokii2, not gnokii?

%description -l pl
Gnokii jest zestawem narzêdzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefonów komórkowych Nokia, dostêpnym na
licencji GPL. Przeczytaj docs/develop.txt:Q. Why mygnokii2, not
gnokii?

%prep
%setup -q -n %{name}
cp %{SOURCE1} config.h
cp %{SOURCE2} %{name}.1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1/,%{_prefix}/src/examples,%{name}}

install mygnokii/mygnokii $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/
mv -f docs/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}
mv -f docs/default $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs
%doc readme.txt
%{_bindir}/mygnokii
%{_examplesdir}/%{name}
%{_mandir}/man1/
