%global debug_package %{nil}
%define _build_id_links none
%define system_name liburcu

Name:           EDO%{system_name}
Version:        0.14
Release:        1%{?dist}
Summary:        Userspace RCU
License:        GPL
Vendor:         %{_vendor}
URL:            https://lttng.org/files/urcu
Source0:        userspace-rcu-latest-%{version}.tar.bz2
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  userspace‐rcu package provides a set of userspace RCU (read‐
copy‐update) libraries. These data synchronization libraries pro‐
vide  read‐side  access  which scales linearly with the number of
cores. It does so by allowing multiples copies of  a  given  data
structure  to  live  at the same time, and by monitoring the data
structure accesses to detect grace  periods  after  which  memory
reclamation is possible.


%description devel


%prep
%setup -n userspace-rcu-%{version}.0


%build
%set_build_flags_with_rpath
%_configure --build=%_build
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}*.so.8*
%_libdir/%{system_name}*.a


%files devel
%_includedir/urcu*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc
%_docdir/userspace-rcu/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
