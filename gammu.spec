Summary:	GNU tool suite for mobile phones
Summary(pl.UTF-8):	Zestaw narzędzi GNU dla telefonów komórkowych
Name:		gammu
Version:	1.10.3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.cihar.com/gammu/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	a7657a6053bcb6212c7287ac99d21015
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-no_nss.patch
Patch2:		%{name}-libpq_dir.patch
URL:		http://www.gammu.org/
BuildRequires:	autoconf
BuildRequires:	bluez-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
Provides:	mygnokii2
Obsoletes:	mygnokii2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gammu (formerly known as MyGnokii2) is cellular manager for various
mobile phones and modems. It currently supports Nokia 3210, 33xx,
3410, 3510, 51xx, 5210, 5510, 61xx, 62xx, 63xx, 6510, 7110, 82xx,
8310, 9110, and 9210, and AT devices (such as Siemens, Alcatel,
WaveCom, IPAQ, and other). It has a command line version with many
functions for ringtones, phonebook, SMS, logos, WAP, date/time, alarm,
calls, etc. It can also make full backups and restore them.

%description -l pl.UTF-8
Gammu (poprzednio znany jako MyGnokii2) jest narzędziem do zarządzania
różnymi telefonami komórkowymi i modemami. Aktualnie obsługuje Nokie
3210, 33xx, 3410, 51xx, 5210, 5510, 61xx, 62xx, 63xx, 6510, 7110,
82xx, 8310, 9110 i 3210 oraz urządzenia AT (takie jak Siemens,
Alcatel, WaveCom, IPAQ i inne). Ma wersję działającą z linii poleceń z
wieloma funkcjami do dzwonków, książki telefonicznej, SMS-ów, logo,
WAP, daty/czasu, budzika, dzwonienia itp. Może także wykonywać pełne
kopie zapasowe danych i odtwarzać je.

%package devel
Summary:	Header files for Gammu tool suite for mobile phones
Summary(pl.UTF-8):	Pliki nagłówkowe zestawu narzędzi dla telefonów komórkowych Gammu
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for Gammu tool suite for mobile phones.

%description devel -l pl.UTF-8
Pliki nagłówkowe zestawu narzędzi dla telefonów komórkowych Gammu.

%package libs
Summary:	Gammu library
Summary(pl.UTF-8):	Biblioteka Gammu
Group:		Libraries

%description libs
Gammu tool suite library.

%description devel -l pl.UTF-8
Biblioteka zestawu narzędzi dla telefonów komórkowych Gammu.

%package static
Summary:	Gammu static library
Summary(pl.UTF-8):	Biblioteka statyczna Gammu
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description static
Gammu static library.

%description devel -l pl.UTF-8
Biblioteka statyczna zestawu narzędzi dla telefonów komórkowych Gammu.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -f VERSION cfg/autoconf/VERSION
mv docs/user/gammu.1 .

%build
cd cfg/autoconf
%{__autoconf}
%configure \
	--disable-static \
	--without-rpmdir \
	--enable-cb \
	--enable-7110incoming \
	--enable-6210calendar \
	--with-localedir=%{_datadir}/%{name}
cd ../..
%{__make} shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_examplesdir}/%{name}-%{version},%{_datadir}/%{name}}
%{__make} installlibonly installlocales \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	INSTALL_LIB_DIR=%{_libdir} \
	INSTALL_MAN_DIR=%{_mandir}/man1 \
	FIND=find

install -D gammu.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install docs/examples/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}
cp -r docs/{examples,develop} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%find_lang %{name}
cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libGammu.so.1.0 libGammu.so

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog docs/user/gammu.htm docs/user/readme.htm other/bash README
%doc %lang(it) docs/user/gammu.it.txt docs/user/readme.it.txt
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gammurc
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/*
%{_pkgconfigdir}/*

%files libs
%defattr(755,root,root,755)
%{_libdir}/*.so.*

%files static
%defattr(755,root,root,755)
%{_libdir}/*.a
