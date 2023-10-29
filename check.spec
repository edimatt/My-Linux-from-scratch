%global debug_package %{nil}
%define _build_id_links none
%define system_name check

Name:           EDO%{system_name}
Version:        0.15.2
Release:        1%{?dist}
Summary:        Check is a unit testing framework for C
License:        GPL
Vendor:         %{_vendor}
URL:            https://libcheck.github.io/check
Source0:        https://github.com/libcheck/check/releases/download/%{version}/%{system_name}-%{version}.tar.gz
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
Check  is  a  unit testing framework for C.  It features a simple
interface for defining unit tests, putting little in the  way  of
the developer. Tests are run in a separate address space, so both
assertion failures and code errors that cause segmentation faults
or  other  signals  can be caught. Test results are reportable in
the following: Subunit, TAP, XML, and a generic logging format.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
# export CFLAGS="-O3 -g -Wall"
# export CXXFLAGS="$CFLAGS"
%_configure --enable-only64bit --enable-lto --enable-tls
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}mk
%_mandir/man1/%{system_name}mk.1
%_datadir/aclocal/%{system_name}.m4
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_libdir/lib%{system_name}.so.0*
%_docdir/%{system_name}/*


%files devel
%_includedir/%{system_name}*.h
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/pkgconfig/%{system_name}.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
