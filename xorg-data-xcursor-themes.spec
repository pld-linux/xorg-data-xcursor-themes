Summary:	Cursor themes
Summary(pl):	Motywy kursorów
Name:		xorg-data-xcursor-themes
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		Themes
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/data/xcursor-themes-%{version}.tar.bz2
# Source0-md5:	70895b66058b37f9c90c9a0f5b26d22c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
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

%description -n xcursor-theme-handhelds
Cursors theme "handhelds" for X11.

%description -n xcursor-theme-handhelds -l pl
Motyw kursorów "handhelds" dla X11.

%package -n xcursor-theme-redglass
Summary:	Cursors theme "redglass"
Summary(pl):	Motyw kursorów "redglass"
Group:		Themes

%description -n xcursor-theme-redglass
Cursors theme "redglass" for X11.

%description -n xcursor-theme-redglass -l pl
Motyw kursorów "redglass" dla X11.

%package -n xcursor-theme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl):	Motyw kursorów "whiteglass"
Group:		Themes

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
%{_iconsdir}/handhelds

%files -n xcursor-theme-redglass
%defattr(644,root,root,755)
%{_iconsdir}/redglass

%files -n xcursor-theme-whiteglass
%defattr(644,root,root,755)
%{_iconsdir}/whiteglass
