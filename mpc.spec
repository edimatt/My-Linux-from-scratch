%global debug_package %{nil}
%define _build_id_links none
%define system_name mpc

Name:           EDO%{system_name}
Version:        1.3.1
Release:        1%{?dist}
Summary:        C library for multiple precision complex arithmetic.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.mpfr.org
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel EDOmpfr-devel
Requires:       glibc EDOgmp EDOmpfr
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
AutoReqProv:    no


%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as Mpfr.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/lib%{system_name}.a
%_libdir/lib%{system_name}.la
%_libdir/lib%{system_name}.so.3
%_libdir/lib%{system_name}.so.3.3.1


%files devel
%_includedir/%{system_name}.h
%_libdir/lib%{system_name}.so
# %_libdir/pkgconfig/%{system_name}.pc
%_infodir/%{system_name}.info*
%ghost %{_infodir}/dir


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
