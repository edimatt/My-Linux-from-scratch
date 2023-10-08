%global debug_package %{nil}
%define _build_id_links none
%define system_name libb2

Name:           EDO%{system_name}
Version:        0.98.1
Release:        1%{?dist}
Summary:        C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/BLAKE2/libb2
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgcc
Requires:       glibc EDOgcc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-shared --enable-profile
%make_build


%check
# make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}.so.1*


%files devel
%_includedir/blake2.h
%_libdir/%{system_name}.so
%_libdir/%{system_name}.la
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/libb2.so.1.0.4
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/libb2.so.1
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/libb2.so
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/libb2.la
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/pkgconfig
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/lib64/pkgconfig/libb2.pc
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/include
/home/edoardo/rpmbuild/BUILDROOT/EDOlibb2-0.98.1-1.el9.x86_64/opt/edo/include/blake2.h
