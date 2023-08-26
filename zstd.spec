%global debug_package %{nil}
%define _build_id_links none
%define system_name zstd

Name:           EDO%{system_name}
Version:        1.5.5
Release:        1%{?dist}
Summary:        Zstd shared library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/facebook/zstd
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOzlib-devel EDOxz-devel
Requires:       glibc EDOzlib EDOxz-libs
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Zstandard,  or zstd as short version, is a fast lossless compres‐
sion algorithm,  targeting  real‐time  compression  scenarios  at
zlib‐level  and  better compression ratios. It’s backed by a very
fast entropy stage, provided by Huff0 and FSE library.

Zstandard’s format is stable and documented in RFC8878.  Multiple
independent implementations are already available. This reposito‐
ry represents the reference implementation, provided as an  open‐
source  dual  BSD OR GPLv2 licensed C library, and a command line
utility producing and decoding .zst, .gz,  .xz  and  .lz4  files.
Should  your project require another programming language, a list
of known ports and bindings is provided on Zstandard homepage.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%make_build


%check
make check


%install
%make_install prefix=%_prefix libdir=%_libdir


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_bindir/un%{system_name}
%_mandir/man1/%{system_name}*.1
%_mandir/man1/un%{system_name}.1
%_libdir/lib%{system_name}.so.*
%_libdir/lib%{system_name}.a


%files devel
%_includedir/%{system_name}*.h
%_includedir/zdict.h
%_libdir/lib%{system_name}*.so
%_libdir/pkgconfig/lib%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
