Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/uniksowy zestaw narzêdzi dla telefonów komórkowych Nokia
Name:		gammu
Version:	1.06.00
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://cihar.com/gammu/zips/gammu/stable/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	d7ad43992fbc32bd9e371afeb73e487f
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-no_nss.patch
URL:		http://www.gammu.org/
BuildRequires:	autoconf
BuildRequires:	bluez-libs-devel
BuildRequires:	mysql-devel
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

%description -l pl
Gammu (poprzednio znany jako MyGnokii2) jest narzêdziem do zarz±dzania
ró¿nymi telefonami komórkowymi i modemami. Aktualnie obs³uguje Nokie
3210, 33xx, 3410, 51xx, 5210, 5510, 61xx, 62xx, 63xx, 6510, 7110,
82xx, 8310, 9110 i 3210 oraz urz±dzenia AT (takie jak Siemens,
Alcatel, WaveCom, IPAQ i inne). Ma wersjê dzia³aj±c± z linii poleceñ z
wieloma funkcjami do dzwonków, ksi±¿ki telefonicznej, SMS-ów, logo,
WAP, daty/czasu, budzika, dzwonienia itp. Mo¿e tak¿e wykonywaæ pe³ne
kopie zapasowe danych i odtwarzaæ je.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
cp -f version cfg/autoconf/VERSION
mv docs/docs/english/gammu.1 .

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
%{__make} installlocales installlibonly \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	INSTALL_LIB_DIR=%{_libdir} \
	INSTALL_MAN_DIR=%{_mandir}/man1 \
	FIND=find

install -D gammu.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install docs/examples/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}
cp -r docs/{examples,develop} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
# anybody feels like developing gammu-based apps?
rm -rf $RPM_BUILD_ROOT{%{_includedir},%{_libdir}/{*.{so,a},pkgconfig}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc changelog docs/docs/english/gammu.htm other/bash readme.txt
%doc %lang(it) docs/docs/italian
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/*.so.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gammurc
%dir %{_datadir}/%{name}
%lang(cs) %{_datadir}/gammu/gammu_cs.txt
%lang(de) %{_datadir}/gammu/gammu_de.txt
%lang(es) %{_datadir}/gammu/gammu_es.txt
%lang(it) %{_datadir}/gammu/gammu_it.txt
%lang(pl) %{_datadir}/gammu/gammu_pl.txt
%lang(ru) %{_datadir}/gammu/gammu_ru.txt
%{_datadir}/gammu/gammu_us.txt
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/*
