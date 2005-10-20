# TODO: which package should own %{_iconsdir}???
Summary:	Cursor themes
Summary(pl):	Motywy kursorów
Name:		xorg-data-xcursor-themes
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Themes
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/data/xcursor-themes-%{version}.tar.bz2
# Source0-md5:	a86608399b872b9ca3ed56d864918794
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-xcursorgen
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cursor themes.

%description -l pl
Motywy kursorów.

%package -n xcursor-theme-handhelds
Summary:	Cursors Theme "handhelds"
Summary(pl):	Motyw kursorów "handhelds"
Group:		Themes
Obsoletes:	XcursorTheme-handhelds

%description -n xcursor-theme-handhelds
Cursors theme "handhelds" for X11.

%description -n xcursor-theme-handhelds -l pl
Motyw kursorów "handhelds" dla X11.

%package -n xcursor-theme-redglass
Summary:	Cursors theme "redglass"
Summary(pl):	Motyw kursorów "redglass"
Group:		Themes
Obsoletes:	XcursorTheme-redglass

%description -n xcursor-theme-redglass
Cursors theme "redglass" for X11.

%description -n xcursor-theme-redglass -l pl
Motyw kursorów "redglass" dla X11.

%package -n xcursor-theme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl):	Motyw kursorów "whiteglass"
Group:		Themes
Obsoletes:	XcursorTheme-whiteglass

%description -n xcursor-theme-whiteglass
Cursors theme "whiteglass" for X11.

%description -n xcursor-theme-whiteglass -l pl
Motyw kursorów "whiteglass" dla X11.

%prep
%setup -q -n xcursor-themes-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc ChangeLog
%{_iconsdir}/handhelds

%files -n xcursor-theme-redglass
%defattr(644,root,root,755)
%doc ChangeLog
%{_iconsdir}/redglass

%files -n xcursor-theme-whiteglass
%defattr(644,root,root,755)
%doc ChangeLog
%{_iconsdir}/whiteglass
