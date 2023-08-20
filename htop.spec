%global debug_package %{nil}
%define _build_id_links none

Name:           htop
Version:        3.2.1
Release:        1%{?dist}
Summary:        htop is a cross-platform interactive process viewer.

License:        GPL
URL:            https://github.com/htop-dev/htop
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build ncurses-devel
Requires:       glibc ncurses-libs
AutoReqProv:    no

%description
top is a cross-platform interactive process viewer.

htop allows scrolling the list of processes vertically and horizontally
to see their full command lines and related information like memory and
CPU consumption. Also system wide information, like load average or swap
usage, is shown.

The information displayed is configurable through a graphical setup and
can be sorted and filtered interactively.

Tasks related to processes (e.g. killing and renicing) can be done without
entering their PIDs.

Running htop requires ncurses libraries, typically named libncurses(w).

htop is written in C.

For more information and details visit htop.dev.

%prep
%autosetup -n %{name}-%{version}
./autogen.sh
%configure

%build
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license htop
%doc htop
%_bindir/%name
%_mandir/man1/%name.1
%_datadir/applications/*
%_datadir/pixmaps/*
%_datadir/icons/*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
