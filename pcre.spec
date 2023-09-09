%global debug_package %{nil}
%define _build_id_links none
%define system_name pcre

Name:           EDO%{system_name}
Version:        8.45
Release:        1%{?dist}
Summary:        Perl-compatible regular expression library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.pcre.org
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOzlib-devel EDObzip2-devel
Requires:       glibc EDOzlib EDObzip2-libs
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
PCRE, Perl‐compatible regular expression, library has its own na‐
tive API, but a set of wrapper functions that are  based  on  the
POSIX  API  are  also  supplied in the libpcreposix library. Note
that this just provides a POSIX calling interface  to  PCRE:  the
regular  expressions  themselves still follow Perl syntax and se‐
mantics. This package provides support for strings in  8‐bit  and
UTF‐8  encodings.  Detailed  change  log  is provided by pcre‐doc
package.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure  --enable-unicode-properties       \
            --enable-pcre16                   \
            --enable-pcre32                   \
            --enable-pcregrep-libz            \
            --enable-pcregrep-libbz2          \
            --enable-pcretest-libreadline     \
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
%_libdir/lib%{system_name}*.so.*


%files devel
%_bindir/%{system_name}-config*
%_mandir/man1/%{system_name}-config.1
%_mandir/man3/%{system_name}*.3
%_docdir/%{system_name}/*
%_includedir/%{system_name}*.h
%_libdir/lib%{system_name}*.so
%_libdir/lib%{system_name}*.la
%_libdir/pkgconfig/lib%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
