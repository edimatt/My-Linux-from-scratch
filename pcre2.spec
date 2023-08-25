%global debug_package %{nil}
%define _build_id_links none
%define system_name pcre2

Name:           EDO%{system_name}
Version:        10.42
Release:        1%{?dist}
Summary:        PCRE2 - Perl-Compatible Regular Expressions.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/PCRE2Project/pcre2
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOzlib-devel bzip2-devel
Requires:       glibc EDOzlib bzip2-libs
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The  PCRE2 library is a set of C functions that implement regular
expression pattern matching using the same syntax  and  semantics
as  Perl  5.  PCRE2  has  its own native API, as well as a set of
wrapper functions that correspond to the POSIX regular expression
API.  The  PCRE2  library  is free, even for building proprietary
software. It comes in three forms, for processing 8‐bit,  16‐bit,
or 32‐bit code units, in either literal or UTF encoding.

PCRE2 was first released in 2015 to replace the API in the origi‐
nal PCRE library, which is now obsolete and no longer maintained.
As  well  as a more flexible API, the code of PCRE2 has been much
improved since the fork.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure  --enable-jit                        \
            --enable-pcre2-16                   \
            --enable-pcre2-32                   \
            --enable-pcre2grep-libz             \
            --enable-pcre2grep-libbz2           \
            --enable-pcre2test-libreadline      \
            --disable-static           
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}test
%_bindir/%{system_name}grep
%_mandir/man1/%{system_name}*.1
%_libdir/lib%{system_name}-*.so.0
%_libdir/lib%{system_name}-*.so.0.11.2
%_libdir/lib%{system_name}-posix.so.3
%_libdir/lib%{system_name}-posix.so.3.0.4


%files devel
%_bindir/%{system_name}-config*
%_mandir/man1/%{system_name}-config.1
%_mandir/man3/%{system_name}*.3
%_docdir/%{system_name}/*
%_includedir/%{system_name}*.h
%_libdir/lib%{system_name}-*.so
%_libdir/lib%{system_name}-*.la
%_libdir/lib%{system_name}-posix.la
%_libdir/lib%{system_name}-posix.so
%_libdir/pkgconfig/lib%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
