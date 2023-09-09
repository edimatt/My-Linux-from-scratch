%global debug_package %{nil}
%define _build_id_links none
%define system_name rpmreaper

Name:           EDO%{system_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Display rpm dependencies.
License:        GPL
URL:            https://github.com/mlichvar/rpmreaper
Source:         %{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build EDOncurses-devel rpm-devel
Requires:       glibc rpm >= 4.6 EDOncurses-libs
AutoReqProv:    no

%description
rpmreaper is a simple ncurses application with a mutt-like interface that
allows removing unnecessary packages and their dependencies from the system.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
# Needed to to find rpm.pc in rpm-devel
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig
%make_build


%install
%make_install prefix=%{buildroot}%_prefix


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
