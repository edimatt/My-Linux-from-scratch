%global debug_package %{nil}
%define _build_id_links none
%define system_name libtasn1

Name:           EDO%{system_name}
Version:        4.19.0
Release:        1%{?dist}
Summary:        ASN.1 library used by GnuTLS, p11-kit and some other packages.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/libffi/libffi
Source0:        %{system_name}-%{version}.tar.gz
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
Libtasn1  is  the  ASN.1 library used by GnuTLS, p11‐kit and some
other packages. It was originally written by Fabio  Fiorina,  and
now maintained as a GNU package.  The goal of this implementation
is to be highly portable, and only require an ANSI C99 platform.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --disable-static
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/asn1*
%_mandir/man1/asn1*.1
%_libdir/%{system_name}.so.6*


%files devel
%_mandir/man3/asn1*.3
%_includedir/%{system_name}.h
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
