%global debug_package %{nil}
%define _build_id_links none
%define system_name readline

Name:           EDO%{system_name}
Version:        8.2
Release:        1%{?dist}
Summary:        A library for editing typed command lines.
License:        GPL
Vendor:         %{_vendor}
URL:            https://ftp.gnu.org/gnu/readline
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOncurses-devel
Requires:       glibc EDOncurses-libs
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
The Readline library provides a set of functions that allow users
to edit command lines. Both Emacs and vi editing modes are avail‐
able.  The  Readline  library  includes  additional functions for
maintaining a list of previously‐entered command  lines  for  re‐
calling  or editing those lines, and for performing csh‐like his‐
tory expansion on previous commands.


%description devel
The Readline library provides a set of functions that allow users
to edit typed command lines. If you want to develop programs that
will use the readline library, you need to have the readline‐dev‐
el package installed. You also need to have the readline  package
installed.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure --enable-multibyte --with-curses
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_docdir/%{system_name}/*
%_libdir/lib%{system_name}.so.8
%_libdir/lib%{system_name}.so.8.2
%_libdir/libhistory.so.8
%_libdir/libhistory.so.8.2


%files devel
%_includedir/%{system_name}/*.h
%_libdir/lib%{system_name}.so
%_libdir/libhistory.so
%_libdir/pkgconfig/%{system_name}.pc
%_libdir/pkgconfig/history.pc
%_mandir/man3/%{system_name}.3
%_mandir/man3/history.3
%_infodir/%{system_name}.info
%_infodir/history.info
%_infodir/rluserman.info
%ghost %{_infodir}/dir


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
