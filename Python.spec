%global debug_package %{nil}
%define _build_id_links none
%define python_micro 4
%define system_name python

Name:           EDO%{system_name}
Version:        3.12
Release:        %{python_micro}%{?dist}
Summary:        python
License:        GPL
URL:            www.python.org
Source0:        Python-%{version}.%{python_micro}.tar.xz
BuildRequires:  EDOexpat-devel EDObzip2-devel EDOopenssl-devel EDOlibxcrypt-devel glibc-devel EDOlibffi-devel EDOxz-devel EDOncurses-devel EDOreadline-devel EDOsqlite-devel EDOzlib-devel EDOlibuuid-devel EDOgdbm-devel EDOtcl-devel EDOtk-devel /usr/bin/pathfix.py
Requires:       %{name}-libs = %{version}
Provides:       %{name} = %{version}
AutoReqProv:    no

%package libs
Summary:        Shared libraries.
Requires:       EDObzip2-libs EDOopenssl-libs EDOlibxcrypt glibc EDOlibffi EDOxz-libs EDOncurses-libs EDOncurses-libs EDOreadline EDOsqlite-libs EDOzlib EDOexpat EDOlibuuid EDOgdbm EDOtcl EDOtk
Provides:       %{name}-libs = %{version}
AutoReqProv:    no

%package devel
Summary:        Development tools.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no

%description

%description libs

%description devel


%prep
%setup -q -n Python-%{version}.%{python_micro}


%build
%set_build_flags_with_rpath
mkdir _build && cd _build
export BZIP2_LIBS="-L/opt/edo/lib64 -lbz2"
export LIBREADLINE_LIBS="-L/opt/edo/lib64 -lreadline -ltinfo"
%_prev_configure --enable-shared            \
           --with-platlibdir=%{_lib}   \
           --enable-loadable-sqlite-extensions \
           --with-system-expat         \
           --with-system-ffi           \
           --with-lto=yes              \
           --enable-optimizations      \
           --without-static-libpython  \
           --with-system-libmpdec      \
           --with-ssl-default-suites=openssl \
           --with-openssl=%_prefix \
           --with-readline=readline \
           --with-ensurepip=no
%make_build


%install
cd _build && %{make_install}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%_libdir/%{system_name}%{version}/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/idle*
%_bindir/pydoc*
%_bindir/%{system_name}3
%_bindir/%{system_name}%{version}
%_mandir/man1/%{system_name}*


%files libs
%_libdir/%{system_name}*
%_libdir/lib%{system_name}3.so
%_libdir/lib%{system_name}%{version}.so.1.0


%files devel
%_bindir/2to3
%_bindir/2to3-%{version}
%_bindir/%{system_name}3-config
%_bindir/%{system_name}%{version}-config
%_libdir/lib%{system_name}%{version}.so
%_libdir/pkgconfig/%{system_name}*
%_includedir/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
