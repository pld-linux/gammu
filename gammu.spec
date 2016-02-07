# TODO: gammu-smsd-inject should be in seperate package
Summary:	Tool suite for mobile phones
Summary(pl.UTF-8):	Zestaw narzędzi do telefonów komórkowych
Name:		gammu
Version:	1.37.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dl.cihar.com/gammu/releases/%{name}-%{version}.tar.xz
# Source0-md5:	6e249e6f93461f1fc215ec85cec67740
Source1:	%{name}-smsd.init
Source2:	%{name}-smsd.sysconfig
Source3:	%{name}.tmpfiles
Patch0:		%{name}-etc_dir.patch
URL:		http://www.gammu.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake >= 2.4.6
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Suggests:	%{name}-smsd = %{epoch}:%{version}-%{release}
Provides:	mygnokii2
Obsoletes:	mygnokii2
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

%package smsd
Summary:	Gammu SMS Daemon
Summary(pl.UTF-8):	Demon SMS Gammu
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description smsd
Gammu SMS Daemon is a program that periodically scans GSM modem for
received messages, stores them in defined storage and also sends
messages enqueued in this storage. It is perfect tool for managing big
amounts of received or sent messages and automatically process them.

%description smsd -l pl.UTF-8
Demon SMS Gammu jest programem, który okresowo sprawdza czy modem GSM
odebrał jakieś wiadomości, przechowuje je w zdefiniowanym zasobie a
także wysyła wiadomości skolejkowane w tym zasobie. Jest idealnym
narzędziem do zarządzania dużą ilością otrzymanych lub wysyłanych
wiadomości i automatycznego przetwarzania ich.

%package libs
Summary:	Gammu library
Summary(pl.UTF-8):	Biblioteka Gammu
Group:		Libraries

%description libs
Gammu tool suite library.

%description libs -l pl.UTF-8
Biblioteka zestawu narzędzi dla telefonów komórkowych Gammu.

%package devel
Summary:	Header files for Gammu tool suite for mobile phones
Summary(pl.UTF-8):	Pliki nagłówkowe zestawu narzędzi dla telefonów komórkowych Gammu
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	bluez-libs-devel

%description devel
Header files for Gammu tool suite for mobile phones.

%description devel -l pl.UTF-8
Pliki nagłówkowe zestawu narzędzi dla telefonów komórkowych Gammu.

%package static
Summary:	Gammu static library
Summary(pl.UTF-8):	Biblioteka statyczna Gammu
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gammu static library.

%description static -l pl.UTF-8
Biblioteka statyczna zestawu narzędzi dla telefonów komórkowych Gammu.

%package -n bash-completion-gammu
Summary:	bash-completion for gammu
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla gammu
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-gammu
This package provides bash-completion for gammu.

%description -n bash-completion-gammu -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla gammu.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"                                                                                                                                                                                        
export CXXFLAGS="%{optflags}"                                                                                                                                                                                      
mkdir -p build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF \
	-DINSTALL_LIB_DIR=%{_lib} \
	-DINSTALL_LIBDATA_DIR=%{_libdir}
%{__make}
mv libgammu/libGammu.a ..
mv smsd/libgsmsd.a ..
%cmake .. \
	-DBUILD_SHARED_LIBS=ON \
	-DINSTALL_LIB_DIR=%{_lib} \
	-DINSTALL_LIBDATA_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_examplesdir}/%{name}-%{version}} \
	$RPM_BUILD_ROOT/usr/lib/tmpfiles.d

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}
#cp -r docs/develop $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install libGammu.a $RPM_BUILD_ROOT%{_libdir}
install libgsmsd.a $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-smsd $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install docs/config/smsdrc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-smsd/ttyS0.conf
install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}-smsd
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}-smsd
install -d $RPM_BUILD_ROOT/%{_varrun}/%{name}-smsd
install -d $RPM_BUILD_ROOT/%{_sharedstatedir}/%{name}-smsd

install %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

%find_lang %{name}
%find_lang libgammu

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# for rpm autodeps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%pre smsd
%groupadd -g 251 gammu-smsd
%useradd -u 251 -d /var/lib/gammu-smsd -s /bin/false -c "Gammu SMSD user" -G dialout -g gammu-smsd gammu-smsd

%post smsd
/sbin/chkconfig --add gammu-smsd
%service gammu-smsd restart "Gammu SMSD"

%preun smsd
if [ "$1" = "0" ]; then
        %service gammu-smsd stop
        /sbin/chkconfig --del gammu-smsd
fi

%postun smsd
if [ "$1" = "0" ]; then
        %groupremove gammu-smsd
        %userremove gammu-smsd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog docs/manual/Gammu.htm
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-detect
%attr(755,root,root) %{_bindir}/jadmaker
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gammurc
%{_examplesdir}/%{name}-%{version}
%{_datadir}/gammu
%{_mandir}/man[157]/*

%files smsd
%defattr(644,root,root,755)
%doc docs/sql/*.sql
%attr(755,root,root) %{_bindir}/gammu-smsd
%attr(755,root,root) %{_bindir}/gammu-smsd-inject
%attr(755,root,root) %{_bindir}/gammu-smsd-monitor
%attr(754,root,root) /etc/rc.d/init.d/%{name}-smsd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}-smsd
%{_sysconfdir}/%{name}-smsd
/usr/lib/tmpfiles.d/%{name}.conf
%attr(750,root,gammu-smsd) %{_varrun}/%{name}-smsd
%attr(750,gammu-smsd,gammu-smsd) %{_sharedstatedir}/%{name}-smsd

%files libs -f libgammu.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGammu.so.*.*
%attr(755,root,root) %{_libdir}/libgsmsd.so.*.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsmsd.so.7
%attr(755,root,root) %ghost %{_libdir}/libGammu.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/libGammu.so
%attr(755,root,root) %{_libdir}/libgsmsd.so
%{_includedir}/*
%{_pkgconfigdir}/gammu.pc
%{_pkgconfigdir}/gammu-smsd.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsmsd.a
%{_libdir}/libGammu.a

%files -n bash-completion-gammu
%defattr(644,root,root,755)
%{bash_compdir}/gammu
