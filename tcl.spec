%global debug_package %{nil}
%define _build_id_links none
%define system_name tcl

Name:           EDO%{system_name}
Version:        8.6.13
Release:        1%{?dist}
Summary:        C library for multiple precision complex arithmetic.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.tcl.tk
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel EDOmpfr-devel
Requires:       glibc EDOgmp EDOmpfr
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
export TCL_LIBRARY=%_libdir/%{system_name}8.6
export CFLAGS_OPTIMIZE=
export CFLAGS="$CFLAGS -lm"
cd unix && %_configure --enable-64bit --enable-shared --enable-threads && %make_build


%install
cd unix && %make_install
chmod +w %{buildroot}%{_libdir}/lib%{system_name}8.6.so
cd %{buildroot}%{_bindir} && ln -sfv %{system_name}sh8.6 %{system_name}sh && cd -
cd %{buildroot}%{_mandir}/man3 && mv Thread.3 Tcl_Thread.3 && cd -
cd %{buildroot}%{_libdir} && ln -sfv lib%{system_name}8.6.so lib%{system_name}.so && cd -


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/tclsh*
%_mandir/man1/tclsh.1
%_libdir/lib%{system_name}8.6.so
%_libdir/lib%{system_name}stub8.6.a
%_libdir/tcl8.6/*
%_libdir/tcl8/*
%_libdir/tdbc*
%_libdir/itcl*
%_libdir/sqlite*
%_libdir/thread*


%files devel
%_bindir/sqlite3_analyzer
%_includedir/*%{system_name}*.h
%_includedir/tdbc*.h
%_includedir/*Stubs.h
%_includedir/fake*.h
%_libdir/lib%{system_name}.so
%_libdir/pkgconfig/%{system_name}.pc
%_libdir/tcl*.sh
%_mandir/man3/Tcl_*.3
%_mandir/man3/ck*.3
%_mandir/man3/attemptck*.3
%_mandir/man3/T*.3
%_mandir/man3/DString.3
%_mandir/man3/Notifier.3
%_mandir/man3/RegExp.3
%_mandir/mann/*.n


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
