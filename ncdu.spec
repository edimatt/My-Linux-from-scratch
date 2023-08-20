%global debug_package %{nil}
%define _build_id_links none

Name:           ncdu
Version:        1.14.2
Release:        1%{?dist}
Summary:        Ncurse disk usage analyzer.

License:        GPL
URL:            https://github.com/Efreak/ncdu
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rpm-build ncurses-devel
Requires:       ncurses-libs glibc
AutoReqProv:    no

%description
ncdu (NCurses Disk Usage) is a curses-based version of
the well-known 'du', and provides a fast way to see what
directories are using your disk space.


%prep
%autosetup -n %{name}-%{version}
autoreconf -fi
%configure

%build
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%name
%_mandir/man1/%name.1

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
