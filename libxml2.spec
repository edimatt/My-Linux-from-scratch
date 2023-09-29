%global debug_package %{nil}
%define _build_id_links none
%define system_name libxml2

Name:           EDO%{system_name}
Version:        2.11.5
Release:        1%{?dist}
Summary:        An XML toolkit implemented in C.
License:        GPL
Vendor:         %{_vendor}
URL:            https://gitlab.gnome.org/GNOME/libxml2
Source0:        %{system_name}-%{version}.tar.xz
Patch0:         %{system_name}-%{version}-configure.patch
AutoReqProv:    no
BuildRequires:  glibc-devel EDOreadline-devel EDOncurses-devel EDOzlib-devel EDOxz-devel
Requires:       glibc EDOreadline EDOncurses-libs EDOzlib EDOxz-libs

Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libxml2 is an XML toolkit implemented in C, originally developed for
the GNOME Project.


%description devel


%prep
%setup -n %{system_name}-%{version}
%patch0 -p1


%build
%set_build_flags_with_rpath
%_configure --disable-static \
            --enable-shared  \
            --with-python_prefix=%_prefix \
            --with-history \
            --docdir=%_docdir/%{name} \
             PYTHON=%_bindir/python3
%make_build pythondir=%{_libdir}/python3.11/site-packages


%check
make check


%install
%make_install
%{__mv} %{buildroot}%{_datadir}/gtk-doc/html %{buildroot}%{_docdir}/%{name}/ 
%{__mv} %{buildroot}%{_prefix}/lib/python3.11/site-packages/* %{buildroot}%{_libdir}/python3.11/site-packages/ 


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/xml*
%_mandir/man1/xml*.1
%_libdir/%{system_name}.so.2*
%_libdir/python3.11/site-packages/%{system_name}mod.so
%_libdir/python3.11/site-packages/*%{system_name}*
%_libdir/python3.11/site-packages/__pycache__/*%{system_name}*


%files devel
%_includedir/%{system_name}/*
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/cmake/%{system_name}/*
%_libdir/pkgconfig/libxml-2.0.pc
%_datadir/aclocal/libxml.m4
%_docdir/%{name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
