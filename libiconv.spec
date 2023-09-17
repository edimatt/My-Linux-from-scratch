%global debug_package %{nil}
%define _build_id_links none
%define system_name libiconv

Name:           EDO%{system_name}
Version:        1.17
Release:        2%{?dist}
Summary:        GNU libiconv conversion library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://www.gnu.org/software/libiconv
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
AutoReqProv:    no


%description
International  text  is mostly encoded in Unicode. For historical
reasons, however, it is sometimes still encoded using a  language
or  country  dependent character encoding. With the advent of the
internet and the frequent exchange of  text  across  countries  ‐
even  the viewing of a web page from a foreign country is a "text
exchange" in this context ‐, conversions between these  encodings
have become a necessity.

In  particular, computers with the Windows operating system still
operate in locale with a traditional (limited)  character  encod‐
ing.  Some  programs, like mailers and web browsers, must be able
to convert between a given text encoding and the user’s encoding.
Other programs internally store strings in Unicode, to facilitate
internal processing, and need to convert between internal  string
representation  (Unicode)  and  external string representation (a
traditional encoding) when they are doing I/O. GNU libiconv is  a
conversion library for both kinds of applications.


%description devel


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --docdir=%_docdir/%{name}
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/iconv
%_libdir/%{system_name}.so.2*
%_libdir/libcharset.so.1*
%_mandir/man1/iconv.1
%_docdir/%{name}/iconv*
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%files devel
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/libcharset.so
%_libdir/libcharset.la
%_mandir/man3/iconv*.3
%_includedir/*charset.h
%_includedir/iconv.h


%changelog
* Sun Aug 09 2023 edimatt <edoardo.dimatteo@gmail.com> 1.17-2
- Move linker library name to devel package.
- Fix documentation path.

* Thu Jan 26 2023 Edoardo Di Matteo
- 
