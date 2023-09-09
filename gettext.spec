%global debug_package %{nil}
%define _build_id_links none
%define system_name gettext

Name:           EDO%{system_name}
Version:        0.22
Release:        1%{?dist}
Summary:        GNU libraries and utilities for producing multi-lingual messages.
License:        GPL
URL:            https://www.gnu.org/software/gettext
Source0:        %{system_name}-%{version}.tar.xz
BuildRequires:  glibc-devel EDOgcc EDOacl-devel EDOattr-devel EDOncurses-devel EDOxz-devel
Requires:       glibc %{name}-libs = %{version}
Provides:       %{name} = %{version}
AutoReqProv:    no

%package libs
Summary:        Libraries for decoding LZMA compression.
Requires:       glibc EDOgcc EDOacl-libs EDOattr-libs EDOncurses-libs EDOxz-libs
Provides:       %{name}-libs = %{version}
AutoReqProv:    no

%package devel
Summary:        Devel libraries and headers for liblzma.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no

%description
The GNU gettext package provides a set of tools and documentation
for producing multi‐lingual messages in programs. Tools include a
set  of  conventions about how programs should be written to sup‐
port message catalogs, a directory and file  naming  organization
for  the  message  catalogs, a runtime library which supports the
retrieval of translated messages, and  stand‐alone  programs  for
handling  the  translatable  and  the already translated strings.
Gettext provides an easy to use library and tools  for  creating,
using,  and modifying natural language catalogs and is a powerful
and simple method for internationalizing programs.


%description libs


%description devel


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export CFLAGS=$(echo $CFLAGS | sed 's/-Werror=format-security//')
export CXXFLAGS="$CFLAGS"
%_configure --disable-static --disable-nls --enable-threads=posix --disable-java
%make_build


%install
%{make_install}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_mandir/man1/*.1
%_docdir/%{system_name}/*
%_docdir/libasprintf/*
%_docdir/libtextstyle/*
%_datadir/%{system_name}/*
%_datadir/%{system_name}-%{version}/*
%_datadir/emacs/site-lisp/*


%files libs
%_libdir/libasprintf.so.0*
%_libdir/libgettextlib-%{version}.so
%_libdir/libgettextpo.so.0*
%_libdir/libgettextsrc-%{version}.so
%_libdir/libtextstyle.so.0*
%_libexecdir/%{system_name}/*


%files devel
%_bindir/autopoint
%_bindir/gettextize
%_libdir/*.la
%_libdir/libasprintf.so
%_libdir/libgettextpo.so
%_libdir/libtextstyle.so
%_libdir/libgettextlib.so
%_libdir/libgettextsrc.so
%_libdir/preloadable_libintl.so
%_includedir/*
%_datadir/aclocal/*
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_infodir/libtextstyle.info
%_infodir/autosprintf.info
%_mandir/man1/autopoint.1
%_mandir/man1/gettextize.1
%_mandir/man3/*.3


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
