Summary:	Cursor themes
Summary(pl.UTF-8):	Motywy kursorów
Name:		xorg-data-xcursor-themes
Version:	1.0.2
Release:	1
License:	MIT
Group:		Themes
Source0:	http://xorg.freedesktop.org/releases/individual/data/xcursor-themes-%{version}.tar.bz2
# Source0-md5:	e8929a1bb4d98d1a3991fd340d0b5f09
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-xcursorgen
# to get icondir from xcursor.pc
BuildRequires:	xorg-lib-libXcursor-devel >= 1.1.5.2
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cursor themes.

%description -l pl.UTF-8
Motywy kursorów.

%package -n xcursor-theme-handhelds
Summary:	Cursors Theme "handhelds"
Summary(pl.UTF-8):	Motyw kursorów "handhelds"
Group:		Themes
Obsoletes:	XcursorTheme-handhelds

%description -n xcursor-theme-handhelds
Cursors theme "handhelds" for X11.

%description -n xcursor-theme-handhelds -l pl.UTF-8
Motyw kursorów "handhelds" dla X11.

%package -n xcursor-theme-redglass
Summary:	Cursors theme "redglass"
Summary(pl.UTF-8):	Motyw kursorów "redglass"
Group:		Themes
Obsoletes:	XcursorTheme-redglass

%description -n xcursor-theme-redglass
Cursors theme "redglass" for X11.

%description -n xcursor-theme-redglass -l pl.UTF-8
Motyw kursorów "redglass" dla X11.

%package -n xcursor-theme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl.UTF-8):	Motyw kursorów "whiteglass"
Group:		Themes
Obsoletes:	XcursorTheme-whiteglass

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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n xcursor-theme-handhelds
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_iconsdir}/handhelds

%files -n xcursor-theme-redglass
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_iconsdir}/redglass

%files -n xcursor-theme-whiteglass
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_iconsdir}/whiteglass
