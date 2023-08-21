%global debug_package %{nil}
%define _build_id_links none
%define python_micro 4

Name:           python
Version:        3.11
Release:        %{python_micro}%{?dist}
Summary:        python
License:        GPL
URL:            www.python.org
Source0:        Python-%{version}.%{python_micro}.tgz
BuildRequires:  expat-devel bzip2-devel openssl-devel libxcrypt-devel glibc-devel libffi-devel xz-devel ncurses-devel readline-devel sqlite-devel zlib-devel libuuid-devel gdbm-devel libnsl2-devel /usr/bin/pathfix.py
Requires:       python-libs = %{version}
Provides:       %{name} = %{version}
AutoReqProv:    no

%package libs
Summary:        Shared libraries.
Requires:       bzip2-libs openssl-libs libxcrypt glibc libffi xz-libs ncurses-libs ncurses-libs readline sqlite-libs zlib expat libuuid gdbm libnsl2
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
%configure --enable-shared            \
           --with-platlibdir=%{_lib}  \
           --with-system-expat        \
           --with-system-ffi          \
           --enable-optimizations     \
           --without-static-libpython \
           --disable-test-modules     \
           --with-ensurepip=no
%make_build


%install
%{make_install}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%_libdir/%{name}%{version}/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/idle*
%_bindir/pydoc*
%_bindir/%{name}3
%_bindir/%{name}%{version}
%_mandir/man1/%{name}*


%files libs
%_libdir/%{name}*
%_libdir/lib%{name}3.so
%_libdir/lib%{name}%{version}.so.1.0


%files devel
%_bindir/2to3
%_bindir/2to3-%{version}
%_bindir/%{name}3-config
%_bindir/%{name}%{version}-config
%_libdir/lib%{name}%{version}.so
%_libdir/pkgconfig/%{name}*
%_includedir/%{name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
