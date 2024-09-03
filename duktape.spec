%global debug_package %{nil}
%define _build_id_links none
%define system_name duktape

Name:           EDO%{system_name}
Version:        2.7.0
Release:        1%{?dist}
Summary:        Embeddable Javascript engine, with focus on portability and compact footprint.
License:        MIT
URL:            https://duktape.org/
Source:         https://duktape.org/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel
Requires:       glibc
AutoReqProv:    no


%package devel
Summary:        Development tools for %{system_name}.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Duktape  is  an  embeddable  Javascript  engine,  with a focus on
portability and compact footprint.

Duktape is easy to integrate into a C/C++ project: add duktape.c,
duktape.h,  and  duk_config.h  to your build, and use the Duktape
API to call ECMAScript functions from C code and vice versa.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%make_build -f Makefile.sharedlibrary INSTALL_PREFIX=%_prefix LIBDIR=/%_lib


%install
%make_install -f Makefile.sharedlibrary INSTALL_PREFIX=%_prefix LIBDIR=/%_lib


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_libdir/lib%{system_name}.so.*
%_libdir/lib%{system_name}d.so.*


%files devel
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}d.so
%_libdir/pkgconfig/%{system_name}.pc
%_includedir/duk*.h



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
