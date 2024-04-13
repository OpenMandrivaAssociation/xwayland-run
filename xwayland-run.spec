Name:           xwayland-run
Version:        0.0.3
Release:        1
Summary:        Set of utilities to run headless X/Wayland clients
Group:          System/X11/Wayland
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
Source0:        https://gitlab.freedesktop.org/ofourdan/xwayland-run/-/archive/%{version}/%{name}-%{version}.tar.bz2

# Upstream patch

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(python)
Requires:       (weston or cage or kwin-wayland or mutter or gnome-kiosk)
Requires:       xwayland

# Other utilities merged inside this project
Provides:       wlheadless-run = %{EVRD}
Provides:       xwfb-run = %{EVRD}

%description
xwayland-run contains a set of small utilities revolving around running
Xwayland and various Wayland compositor headless.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wlheadless-run
%{_bindir}/xwayland-run
%{_bindir}/xwfb-run
%{_datadir}/wlheadless/
%{_mandir}/man1/wlheadless-run.1*
%{_mandir}/man1/xwayland-run.1*
%{_mandir}/man1/xwfb-run.1*
%{python_sitelib}/wlheadless/

