%define		ver		3.20
%define		rel		4

Summary:	WideStudio Application Builder
Summary(ja):	WideStudio ¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¥Ó¥ë¥À
Summary(pl):	WideStudio - ¶rodowisko do budowania aplikacji
Name:		WideStudio
Version:	%{ver}.%{rel}
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/widestudio/ws-v%{ver}-%{rel}-src.tar.gz
# Source0-md5:	2a360360f146d1b022db8410010917b8
Source1:	http://dl.sourceforge.net/widestudio/WSClassReference-je.pdf
# Source1-md5:	ad329917e61fbf28f1c60b17243f45bd
Source2:	http://dl.sourceforge.net/widestudio/WSProgrammingGuide-ee.pdf
# Source2-md5:	57018c9330b9779b2d99b6b39b28522c
Source3:	http://dl.sourceforge.net/widestudio/WSProgrammingGuide-je.pdf
# Source3-md5:	02ac28043c0c3c283de8839c357b0490
Source4:	http://dl.sourceforge.net/widestudio/WSUsersGuide-ee.pdf
# Source4-md5:	976d79e1217c0a1b3711581cd028eb71
Source5:	http://dl.sourceforge.net/widestudio/WSUsersGuide-je.pdf
# Source5-md5:	4338a9fdb505521bdc9ada0d28d155f6
Source6:	http://dl.sourceforge.net/widestudio/WSclassReference-en.pdf
# Source6-md5:	6b643a84e05872451437f155894298d7
Source7:	http://dl.sourceforge.net/widestudio/WSprogrammingGuide-en.pdf
# Source7-md5:	a4d598200abf4b805d3cfb64066a355b
Source8:	http://dl.sourceforge.net/widestudio/WSprogrammingGuide-jp.pdf
# Source8-md5:	bca138add0ee623486558de91b68d7ea
Source9:	http://dl.sourceforge.net/widestudio/WSquickReference-en.pdf
# Source9-md5:	4cfdfc6ac0906fffd12efa79ee4825fa
Source10:	http://dl.sourceforge.net/widestudio/WSuoTutorial1-ee.pdf
# Source10-md5:	4cdb925d3033abd4a93f8e423a1f28f4
Source11:	http://dl.sourceforge.net/widestudio/WSuoTutorial2-en.pdf
# Source11-md5:	221161ca6c400227ba1b8590aeb9ba5a
Source12:	http://dl.sourceforge.net/widestudio/WSusersGUide-en.pdf
# Source12-md5:	5234a8290741403ef950bafc120e5c17
Source13:	http://dl.sourceforge.net/widestudio/WSusersGuide-jp.pdf
# Source13-md5:	a1f8686f942a8d555e9cab6b3a8d40fb
Patch0:		%{name}-paths.patch
URL:		http://www.widestudio.org/
BuildRequires:	XFree86-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel
BuildRequires:	ruby
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WideStudio is an integrated development environment(IDE) to build GUI
applications for Linux, FreeBSD, Solaris, Windows95/98/ME, Windows NT,
Win2K.

%description -l ja
WideStudio¤Ï¡¢Windows95,98,WindowsNT,Windows2000,Linux,FreeBSD,SOLARIS
¾å¤ÇÆ°ºî¤¹¤ë¡¢C/C++¤Î½ã¹ñ»º¤Î´°Á´¥Õ¥ê¡¼¤Î¥¦¥£¥ó¥É¥¦¥¢¥×¥ê¥±¡¼¥·¥ç¥óÅý¹ç³«È¯´Ä¶­¤Ç¤¹¡£

%description -l pl
WideStudio jest zintegrowanym ¶rodowiskiem programistycznym (IDE) do
tworzenia aplikacji z graficznym interfejsem u¿utkownika (GUI) pod
Linuksa, FreeBSD, Solarisa, Windows95/98/ME, Windows NT i Win2K.

%package pdfdoc
Summary:	WideStudio documentation
Summary(pl):	Dokumentacja do WideStudio
Group:		X11/Development/Tools

%description pdfdoc
WideStudio documentation.

%description pdfdoc -l pl
Dokumentacja do WideStudio.

%package opengl
Summary:	WideStudio OpenGL library
Summary(ja):	WideStudio OpenGL ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka OpenGL do WideStudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	glut-devel

%description opengl
The WideStudio-opengl package provides library for OpenGL.

%description opengl -l ja
WideStudio-opengl¤Ï¡¢OpenGLÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description opengl -l pl
Pakiet WideStudio-opengl dostarcza bibliotekê do OpenGL.

%package mysql
Summary:	WideStudio MySQL library
Summary(ja):	WideStudio MySQL ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka MySQL do WideStudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	mysql-devel

%description mysql
The WideStudio-mysql package provides library for MySQL.

%description mysql -l ja
WideStudio-mysql¤Ï¡¢MySQLÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description mysql -l pl
Pakiet WideStudio-mysql dostarcza bibliotekê do MySQL.

%package postgresql
Summary:	WideStudio PostgreSQL library
Summary(ja):	WideStudio PostgreSQL ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka PostgreSQL do Widestudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel

%description postgresql
The WideStudio-postgresql package provides library for PostgreSQL.

%description postgresql -l ja
WideStudio-postgresql¤Ï¡¢PostgreSQLÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description postgresql -l pl
Pakiet WideStudio-postgresql dostarcza bibliotekê do PostgreSQL.

%package unixodbc
Summary:	WideStudio unixODBC library
Summary(ja):	WideStudio unixODBC ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka unixODBC do WideStudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	unixODBC-devel

%description unixodbc
The WideStudio-unixodbc package provides library for unixODBC.

%description unixodbc -l ja
WideStudio-unixodbc¤Ï¡¢unixODBCÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description unixodbc -l pl
Pakiet WideStudio-unixodbc dostarcza bibliotekê do unixODBC.

%package python
Summary:	WideStudio python library
Summary(ja):	WideStudio python ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka python do WideStudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	python

%description python
The WideStudio-python package provides library for python.

%description python -l ja
WideStudio-python¤Ï¡¢pythonÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description python -l pl
Pakiet WideStudio-python dostarcza bibliotekê do pythona.

%package ruby
Summary:	WideStudio ruby library
Summary(ja):	WideStudio ruby ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka ruby do WideStudio
Group:		X11/Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	ruby

%description ruby
The WideStudio-ruby package provides library for ruby.

%description ruby -l ja
WideStudio-ruby¤Ï¡¢rubyÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description ruby -l pl
Pakiet WideStudio-ruby dostarcza bibliotekê do ruby'ego.

%package perl
Summary:	WideStudio perl library
Summary(ja):	WideStudio perl ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka perl do WideStudio
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl

%description perl
The WideStudio-perl package provides library for perl.

%description perl -l ja
WideStudio-perl¤Ï¡¢perlÍÑ¤Î¥é¥¤¥Ö¥é¥ê¤òÄó¶¡¤·¤Þ¤¹¡£

%description perl -l pl
Pakiet WideStudio-perl dostarcza bibliotekê do perla.

%prep
%setup -q -n ws-v%{ver}-%{rel}
%patch0 -p1
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
cp %{SOURCE6} .
cp %{SOURCE7} .
cp %{SOURCE8} .
cp %{SOURCE9} .
cp %{SOURCE10} .
cp %{SOURCE11} .
cp %{SOURCE12} .
cp %{SOURCE13} .

%build
CXXFLAGS="%{rpmcflags}" ./configure
%{__make} runtime \
	WS_DEFAULT_DIR=%{_datadir}/ws
%{__make} debug \
	WS_DEFAULT_DIR=%{_datadir}/ws

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ws,%{_bindir},%{_libdir},%{_includedir}/ws}

cp bin/* $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_datadir}/ws/bin/.gdb_history
cp lib/* $RPM_BUILD_ROOT%{_libdir}
cp -a doc samples sys $RPM_BUILD_ROOT%{_datadir}/ws
cp -a include/* $RPM_BUILD_ROOT%{_includedir}/ws

ln -sf %{_includedir}/ws $RPM_BUILD_ROOT%{_datadir}/ws/include
ln -sf %{_bindir} $RPM_BUILD_ROOT%{_datadir}/ws/bin
ln -sf %{_libdir} $RPM_BUILD_ROOT%{_datadir}/ws/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT Changelog README README.eucjp
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/jpg.so
%attr(755,root,root) %{_libdir}/libws.so*
%attr(755,root,root) %{_libdir}/libwsad.so*
%attr(755,root,root) %{_libdir}/libwsadd.so*
%attr(755,root,root) %{_libdir}/libwsb.so*
%attr(755,root,root) %{_libdir}/libwsbd.so*
%attr(755,root,root) %{_libdir}/libwsd.so*
%attr(755,root,root) %{_libdir}/libwsj3w.so*
%attr(755,root,root) %{_libdir}/libwsj3wd.so*
%attr(755,root,root) %{_libdir}/libwsr.so*
%attr(755,root,root) %{_libdir}/libwsrd.so*
%attr(755,root,root) %{_libdir}/libwsx11.so*
%attr(755,root,root) %{_libdir}/libwsx11d.so*
%attr(755,root,root) %{_libdir}/png.so
%attr(755,root,root) %{_libdir}/xpm.so
%dir %{_datadir}/ws
%{_datadir}/ws/bin
%{_datadir}/ws/lib
%{_datadir}/ws/include
%{_datadir}/ws/doc
%dir %{_datadir}/ws/samples
%{_datadir}/ws/samples/C
%{_datadir}/ws/samples/class
%{_datadir}/ws/samples/EUCJP
%{_datadir}/ws/samples/graphics
%{_datadir}/ws/samples/net
%{_datadir}/ws/samples/print
%{_datadir}/ws/samples/remote_instance
%{_datadir}/ws/samples/README
%{_datadir}/ws/samples/share
%{_datadir}/ws/samples/SJIS
%{_datadir}/ws/samples/UTF8
%{_datadir}/ws/samples/UTF8-JP
%{_datadir}/ws/sys
%{_includedir}/ws

%files pdfdoc
%defattr(644,root,root,755)
%doc *.pdf

%files opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwsopengl.so*
%attr(755,root,root) %{_libdir}/libwsopengld.so*

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwsmysql.so*
%attr(755,root,root) %{_libdir}/libwsmysqld.so*

%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwspostgres.so*
%attr(755,root,root) %{_libdir}/libwspostgresd.so*

%files unixodbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwsodbc.so*
%attr(755,root,root) %{_libdir}/libwsodbcd.so*
%{_datadir}/ws/samples/database

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/_mpfcmodule.so
%{_libdir}/mpfc.py
%{_datadir}/ws/samples/Python

%files ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpfc.so
%{_datadir}/ws/samples/Ruby

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mpfc_perl.so
%{_libdir}/mpfc.pm
%{_datadir}/ws/samples/Perl
