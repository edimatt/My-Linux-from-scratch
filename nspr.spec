%global debug_package %{nil}
%define _build_id_links none
%define system_name nspr

Name:           EDO%{system_name}
Version:        4.35
Release:        1%{?dist}
Summary:        NetScape Portable Runtime (NSPR).
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.nico.schottelius.org/software/gpm
Source0:        %{system_name}-%{version}.tar.gz
Patch0:         %{system_name}-%{version}-remove.patch
AutoReqProv:    no
BuildRequires:  glibc-devel 
Requires:       glibc 
Provides:       %{name} = %{version}


%package devel
Summary:        Libraries and header files to develop applications using nspr.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
NetScape  Portable  Runtime (NSPR) provides platform independence
for non‐GUI operating system facilities. These facilities include
threads, thread synchronization, normal file and network I/O, in‐
terval timing and calendar time, basic memory management  (malloc
and free) and shared library linking.


%description devel


%prep
%setup -q -n %{system_name}-%{version}
%patch0 -p1


%build
%set_build_flags_with_rpath
pushd %{system_name} 
%_configure --with-mozilla --with-pthreads --enable-64bit
%make_build
popd


%check


%install
cd %{system_name} && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%license nspr/LICENSE
%_libdir/lib*4.so


%files devel
%_bindir/%{system_name}-config
%_libdir/pkgconfig/%{system_name}.pc
%_datadir/aclocal/%{system_name}.m4
%_includedir/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
