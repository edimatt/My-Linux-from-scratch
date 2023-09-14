%global debug_package %{nil}
%define _build_id_links none
%define system_name gnutls

Name:           EDO%{system_name}
Version:        3.7.10
Release:        1%{?dist}
Summary:        A TLS protocol implementation.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gnutls.org
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibunistring-devel EDOgmp-devel EDOlibffi-devel EDOlibiconv-devel EDOlibtasn1-devel EDOnettle-devel EDOp11-kit-devel EDOzlib-devel EDOzstd-devel
Requires:       glibc EDOlibunistring EDOgmp EDOlibffi EDOlibiconv EDOlibtasn1 EDOnettle EDOp11-kit EDOzlib EDOzstd
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
GnuTLS  is  a secure communications library implementing the SSL,
TLS and DTLS protocols and technologies around them. It  provides
a  simple  C  language application programming interface (API) to
access the secure communications protocols as  well  as  APIs  to
parse  and  write  X.509,  PKCS  #12,  OpenPGP and other required
structures.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_libdir/lib%{system_name}*.so.30*


%files devel
%_mandir/man3/*
%_docdir/%{name}/*
%_includedir/%{system_name}/*
%_libdir/lib%{system_name}*.so
%_libdir/lib%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc
%ghost %_infodir/dir
%_infodir/%{system_name}*
%_infodir/pkcs11-vision.png
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-

