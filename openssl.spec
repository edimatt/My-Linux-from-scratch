%global debug_package %{nil}
%define _build_id_links none
%define system_name openssl

Name:           EDO%{system_name}
Version:        3.3.1
Release:        1%{?dist}
Summary:        Utilities from the general purpose cryptography library with TLS implementation.
License:        GPL
URL:            https://www.openssl.org
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel
Requires:       %{name}-libs = %{version}
AutoReqProv:    no


%package libs
Summary:        Libraries
Requires:       glibc
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Development tools.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  OpenSSL  toolkit  provides support for secure communications
between machines. OpenSSL includes a certificate management  tool
and  shared  libraries  which provide various cryptographic algo‐
rithms and


%description libs
OpenSSL  is  a  toolkit for supporting cryptography. The openssl‐
libs package contains the libraries that are used by various  ap‐
plications which support cryptographic algorithms and protocols.


%description devel
OpenSSL is a toolkit for supporting cryptography. The openssl‐de‐
vel package contains include files needed to develop applications
which support various cryptographic algorithms and protocols.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export CFLAGS="-O3 -m64 -Wall -g"
export CXXFLAGS="$CFLAGS"
./Configure --prefix=%_prefix --openssldir=%_sysconfdir/pki/tls --libdir=%_lib shared zlib-dynamic
%make_build


%install
%make_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_bindir/c_rehash
%_mandir/man1/*.1ossl
%_mandir/man5/*.5ossl
%_mandir/man7/*.7ossl
%_docdir/%{system_name}/*


%files libs
%_libdir/libcrypto.so.3*
%_libdir/libssl.so.3*
%_libdir/libcrypto.a
%_libdir/libssl.a
%_libdir/engines-3/*
%_libdir/ossl-modules/legacy.so
%_sysconfdir/pki/tls/*


%files devel
%_libdir/libcrypto.so
%_libdir/libssl.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/OpenSSL/*.cmake
%_includedir/%{system_name}/*
%_mandir/man3/*.3ossl



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
