%global debug_package %{nil}
%define _build_id_links none
%define system_name xapian

Name:           EDO%{system_name}
Version:        1.4.25
Release:        1%{?dist}
Summary:        Open Source Search Engine Library.
License:        GPL
URL:            https://xapian.org/
Source0:        %{system_name}-%{version}.tar.xz
BuildRequires:  glibc-devel EDOgcc EDOutil-linux-devel EDOzlib-devel
Requires:       glibc %{name}-libs = %{version}
Provides:       %{name} = %{version}
AutoReqProv:    no


%package libs 
Summary:        Libraries for %{system_name}.
Requires:       glibc EDOgcc EDOutil-linux EDOzlib
Provides:       %{name}-libs = %{version}
AutoReqProv:    no


%package devel
Summary:        Devel libraries and headers for %{system_name}.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Xapian  is  an  Open Source Search Engine Library, released under
the GPL v2+. It’s written in C++, with bindings to allow use from
Perl  Python  2, Python 3, PHP, Java, Tcl, C#, Ruby, Lua, Erlang,
Node.js and R (so far!)

Xapian is a highly adaptable toolkit which allows  developers  to
easily  add  advanced indexing and search facilities to their own
applications. It has built‐in support  for  several  families  of
weighting  models  and  also supports a rich set of boolean query
operators.

If you’re after a packaged search engine for  your  website,  you
should  take a look at Omega: an application we supply built upon
Xapian. Unlike most other website search solutions, Xapian’s ver‐
satility  allows  you  to extend Omega to meet your needs as they
grow.


%description libs
Library files for %{system_name}.


%description devel
Devel libraries and headers for %{system_name}.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%{make_install}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_bindir/simple*
%_bindir/quest
%_bindir/copydatabase
%_mandir/man1/%{system_name}*.1
%_mandir/man1/quest.1
%_mandir/man1/copydatabase.1


%files libs
%_libdir/lib%{system_name}.so.*


%files devel
%_libdir/lib%{system_name}.so
%_libdir/lib%{system_name}.la
%_libdir/cmake/%{system_name}/*
%_libdir/pkgconfig/%{system_name}-core.pc
%_datadir/aclocal/%{system_name}.m4
%_datadir/%{system_name}-core/*
%_includedir/%{system_name}.h
%_includedir/%{system_name}/*
%_docdir/%{system_name}-core/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
