Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzêdzi dla telefonów komórkowych Nokia
Name:		gammu
Version:	0.97.7
Release:	0.1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.mwiacek.com/zips/gsm/%{name}/older/%{name}-%{version}.tar.gz
# Source0-md5:	0f3fc2bb522c9065f5d02d8dab7d0b43
Patch0:		%{name}-etc_dir.patch
URL:		http://www.mwiacek.com/english/gsm/gammu/gammu.html
BuildRequires:	autoconf
BuildRequires:	bluez-libs-devel
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

%build
cd cfg/autoconf
%{__autoconf}
%configure	\
	--enable-cb 			\
	--enable-7110incoming 		\
	--enable-6210calendar 		\
	--enable-fbus 			\
	--enable-mbus 			\
	--enable-fbusirda 		\
	--enable-phonetblue 		\
	--enable-fbusdku5 		\
	--enable-fbuspl2303 		\
	--enable-fbusdlr3  		\
	--enable-obexgen 		\
	--enable-mroutergen 		\
	--enable-mrouterblue  		\
	--enable-irdaphonet 		\
	--enable-irdaobex		
cd ../..	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name},%{_sysconfdir}}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install docs/examples/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}
mv -f docs/docs/english/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv -f docs/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}
mv -f docs/develop $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog docs/* readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gammurc
%{_examplesdir}/%{name}
%{_mandir}/man1/*.1*
