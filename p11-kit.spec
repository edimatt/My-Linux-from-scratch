%global debug_package %{nil}
%define _build_id_links none
%define system_name p11-kit

Name:           EDO%{system_name}
Version:        0.25.0
Release:        1%{?dist}
Summary:        PKCS#11 kit.
License:        GPL
Vendor:         %{_vendor}
URL:            https://p11-glue.github.io/p11-glue/p11-kit.html
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOlibffi-devel EDOlibtasn1-devel
Requires:       glibc EDOlibffi EDOlibtasn1
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
p11‐kit  aims to solve problems with coordinating the use of PKCS
\#11 by different components  or  libraries living  in  the  same
process,  by  providing a way to load and enumerate PKCS #11 mod‐
ules, as well as a standard configuration  setup  for  installing
PKCS #11 modules in such a way that they’re discoverable.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%meson_setup
%meson_build


%check
%meson_test


%install
%meson_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_bindir/trust
%_libexecdir/%{system_name}/*
%_libdir/lib%{system_name}*.so.0*
%_libdir/pkcs11/*


%files devel
%_includedir/%{system_name}-1/*
%_libdir/lib%{system_name}*.so
%_libdir/%{system_name}-proxy.so
%_libdir/pkgconfig/%{system_name}*.pc
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo
%_datadir/%{system_name}/modules/%{system_name}-trust.module
%_sysconfdir/pkcs11*

%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
