Summary:	KDE System Tray with icon hiding
Summary(pl):	Zasobnik Systemowy KDE z mo¿liwo¶ci± ukrywania ikon
Name:		systemtrayapplet2
Version:	0.51
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://kde-apps.org/content/files/17732-%{name}.tar.bz2
# Source0-md5:	d6cf3d4a4129b72c014eef19dcc384a6
Patch0:		%{name}-desktop.patch
URL:		http://kde-apps.org/content/show.php?content=17732
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the KDE System Tray with icon hiding support. It works exactly
like the original tray but adds icon hiding support, smooth scrolling
and icon grouping.

%description -l pl
Zasobnik Systemowy dla KDE, który umo¿liwia ukrywanie ikon.  Dzia³a
dok³adnie jak oryginalny, ale dodaje mo¿liwo¶æ ukrywania, p³ynnego
przewijania i grupowanie ikon.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_libdir}/libsystemtrayapplet2.so
%{_libdir}/libsystemtrayapplet2.la
%{_datadir}/apps/kicker/applets/systemtrayapplet2.desktop
%{_datadir}/config.kcfg/libsystemtray2_la.kcfg
