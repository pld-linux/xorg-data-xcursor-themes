Summary:	Cursor themes
Summary(pl.UTF-8):	Motywy kursorów
Name:		xorg-data-xcursor-themes
Version:	1.0.7
Release:	1
License:	MIT
Group:		Themes
Source0:	https://xorg.freedesktop.org/releases/individual/data/xcursor-themes-%{version}.tar.xz
# Source0-md5:	070993be1f010b09447ea24bab2c9846
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-xcursorgen
# to get icondir from xcursor.pc
BuildRequires:	xorg-lib-libXcursor-devel >= 1.1.5.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a default set of cursor themes for use with libXcursor,
originally created for the XFree86 Project, and now shipped as part
of the X.Org software distribution.

%description -l pl.UTF-8
Tak pakiet zawiera domyślny zestaw motywów kursorów do używania z
libXcursor, oryginalnie stworzonych dla projektu XFree86, a teraz
dołączanych jako część dystrybucji oprogramowania X.Org.

%package -n xcursor-theme-handhelds
Summary:	Cursors Theme "handhelds"
Summary(pl.UTF-8):	Motyw kursorów "handhelds"
Group:		Themes
Obsoletes:	XcursorTheme-handhelds < 1:7

%description -n xcursor-theme-handhelds
Cursors theme "handhelds" for X11.

%description -n xcursor-theme-handhelds -l pl.UTF-8
Motyw kursorów "handhelds" dla X11.

%package -n xcursor-theme-redglass
Summary:	Cursors theme "redglass"
Summary(pl.UTF-8):	Motyw kursorów "redglass"
Group:		Themes
Obsoletes:	XcursorTheme-redglass < 1:7

%description -n xcursor-theme-redglass
Cursors theme "redglass" for X11.

%description -n xcursor-theme-redglass -l pl.UTF-8
Motyw kursorów "redglass" dla X11.

%package -n xcursor-theme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl.UTF-8):	Motyw kursorów "whiteglass"
Group:		Themes
Obsoletes:	XcursorTheme-whiteglass < 1:7

%description -n xcursor-theme-whiteglass
Cursors theme "whiteglass" for X11.

%description -n xcursor-theme-whiteglass -l pl.UTF-8
Motyw kursorów "whiteglass" dla X11.

%prep
%setup -q -n xcursor-themes-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_host_cpu}" != "x32"
	--host=%{_host} \
	--build=%{_host}
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n xcursor-theme-handhelds
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_iconsdir}/handhelds

%files -n xcursor-theme-redglass
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_iconsdir}/redglass

%files -n xcursor-theme-whiteglass
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_iconsdir}/whiteglass
