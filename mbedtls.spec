%global debug_package %{nil}
%global _lto_cflags %{nil}
%define _build_id_links none
%define system_name mbedtls

Name:           EDO%{system_name}
Version:        3.5.0
Release:        1%{?dist}
Summary:        Light-weight cryptographic and SSL/TLS library
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/Mbed-TLS/mbedtls
Source0:        %{system_name}-%{version}.tar.xz
Patch0:         %{system_name}-%{version}-makefile.patch
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
Mbed TLS is a C library that implements cryptographic primitives,
X.509 certificate manipulation and the SSL/TLS  and  DTLS  proto‐
cols.  Its  small  code  footprint makes it suitable for embedded
systems.
Mbed  TLS includes a reference implementation of the PSA Cryptog‐
raphy API. This is currently a preview  for  evaluation  purposes
only.


%description devel


%prep
%setup -q -n %{system_name}-%{version}
%patch0 -p1


%build
%set_build_flags_with_rpath
mkdir _build && cd _build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DUSE_SHARED_MBEDTLS_LIBRARY=ON -DUSE_STATIC_MBEDTLS_LIBRARY=OFF ..
%make_build 


%check
# make check


%install
%make_install LIB=%_lib PREFIX=%_prefix


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}_*
%_libdir/libmbed*.a


%files devel
%_includedir/%{system_name}/*.h
%_includedir/psa/*.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
/home/edoardo/rpmbuild/BUILDROOT/EDOmbedtls-3.5.0-1.el9.x86_64/lib
/home/edoardo/rpmbuild/BUILDROOT/EDOmbedtls-3.5.0-1.el9.x86_64/lib/libmbedtls.a
/home/edoardo/rpmbuild/BUILDROOT/EDOmbedtls-3.5.0-1.el9.x86_64/lib/libmbedx509.a
/home/edoardo/rpmbuild/BUILDROOT/EDOmbedtls-3.5.0-1.el9.x86_64/lib/libmbedcrypto.a
