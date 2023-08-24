%global debug_package %{nil}
%define _build_id_links none
%define system_name ncdu

Name:           EDO%{system_name}
Version:        1.14.2
Release:        1%{?dist}
Summary:        Ncurse disk usage analyzer.

License:        GPL
URL:            https://github.com/Efreak/ncdu
Source:        %{system_name}-%{version}.tar.gz
Patch:         %{system_name}-%{version}-errorcheck.patch
BuildRequires:  rpm-build EDOncurses-devel
Requires:       EDOncurses-libs glibc
AutoReqProv:    no

%description
ncdu (NCurses Disk Usage) is a curses-based version of
the well-known 'du', and provides a fast way to see what
directories are using your disk space.


%prep
%setup -n %{system_name}-%{version}
%patch -p1
autoreconf -fi


%build
%set_build_flags_with_rpath
%configure --with-ncursesw --without-ncurses
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
