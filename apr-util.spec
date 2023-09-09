%global debug_package %{nil}
%define _build_id_links none
%define system_name apr-util

Name:           EDO%{system_name}
Version:        1.6.3
Release:        1%{?dist}
Summary:        Apache Portable Runtime (APR).
License:        GPL
URL:            https://apr.apache.org/download.cgi
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel EDOapr-devel EDOunixODBC-devel EDOutil-linux-devel EDOexpat-devel
Requires:       glibc EDOapr EDOunixODBC EDOlibtool EDOutil-linux EDOexpat EDOlibxcrypt
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  mission  of  the Apache Portable Runtime (APR) project is to
create and maintain software libraries that provide a predictable
and  consistent  interface to underlying platform‐specific imple‐
mentations. The primary goal is to provide an API to which  soft‐
ware  developers  may  code  and be assured of predictable if not
identical behaviour regardless of the  platform  on  which  their
software  is  built,  relieving them of the need to code special‐
case conditions to work around or take advantage of platform‐spe‐
cific deficiencies or features.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static --with-apr=%_prefix
%make_build


%install
%make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libaprutil-1.so.0*
%_libdir/%{system_name}-1/*


%files devel
%_bindir/apu-1-config
%_libdir/libaprutil-1.so
%_libdir/libaprutil-1.la
%_libdir/aprutil.exp
%_libdir/pkgconfig/%{system_name}-1.pc
%_includedir/apr*.h
%_includedir/apu*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
