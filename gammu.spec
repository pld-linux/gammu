Summary:	Tool suite for mobile phones
Summary(pl.UTF-8):	Zestaw narzędzi do telefonów komórkowych
Name:		gammu
Version:	1.23.1
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.cihar.com/gammu/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	bb1d23eb766ecd9d21bc79c2f8a1d480
Patch0:		%{name}-etc_dir.patch
URL:		http://www.gammu.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake >= 2.4.6
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	rpm-pythonprov
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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

%package -n python-gammu
Summary:	Python bingings for Gammu library
Summary(pl.UTF-8):	Wiązania języka Python dla biblioteki Gammu
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
%requires_eq	gammu-libs

%description -n python-gammu
Python bingings for Gammu library.

%description -l pl.UTF-8 -n python-gammu
Wiązania języka Python dla biblioteki Gammu.

%package static
Summary:	Gammu static library
Summary(pl.UTF-8):	Biblioteka statyczna Gammu
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gammu static library.

%description static -l pl.UTF-8
Biblioteka statyczna zestawu narzędzi dla telefonów komórkowych Gammu.

%prep
%setup -q
%patch0 -p1

%build
mkdir -p build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DBUILD_SHARED_LIBS=OFF \
	-DINSTALL_LIB_DIR=%{_lib} \
	-DINSTALL_LIBDATA_DIR=%{_libdir} \
	%{?debug:-DCMAKE_BUILD_TYPE="Debug"}
%{__make}
mv libgammu/libGammu.a ..
mv smsd/libgsmsd.a ..
%cmake .. \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DBUILD_SHARED_LIBS=ON \
	-DINSTALL_LIB_DIR=%{_lib} \
	-DINSTALL_LIBDATA_DIR=%{_libdir} \
	%{?debug:-DCMAKE_BUILD_TYPE="Debug"}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_examplesdir}/%{name}-%{version}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}
cp -r docs/{examples,develop} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install libGammu.a $RPM_BUILD_ROOT%{_libdir}
install libgsmsd.a $RPM_BUILD_ROOT%{_libdir}

%find_lang %{name}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

# for rpm autodeps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog docs/user/gammu.html docs/user/readme.html README README.Python SUPPORTERS
%doc %lang(it) docs/user/gammu.it.txt docs/user/readme.it.txt
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/gammu-smsd
%attr(755,root,root) %{_bindir}/gammu-smsd-inject
%attr(755,root,root) %{_bindir}/gammu-smsd-monitor
%attr(755,root,root) %{_bindir}/jadmaker
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gammurc
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files libs
%defattr(755,root,root,755)
%attr(755,root,root) %{_libdir}/libGammu.so.*.*
%attr(755,root,root) %{_libdir}/libgsmsd.so.*.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsmsd.so.6
%attr(755,root,root) %ghost %{_libdir}/libGammu.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/libGammu.so
%attr(755,root,root) %{_libdir}/libgsmsd.so
%{_includedir}/*
%dir %{py_sitedir}/gammu/
%attr(755,root,root) %{py_sitedir}/gammu/_gammu.so
%{_pkgconfigdir}/gammu.pc
%{_pkgconfigdir}/gammu-smsd.pc

%files -n python-gammu
%defattr(644,root,root,755)
%dir %{py_sitedir}/gammu
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py

%files static
%defattr(755,root,root,755)
%{_libdir}/libgsmsd.a
%{_libdir}/libGammu.a
