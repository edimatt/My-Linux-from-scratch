%global debug_package %{nil}
%define _build_id_links none
%define system_name valgrind

Name:           EDO%{system_name}
Version:        3.21.0
Release:        1%{?dist}
Summary:        Instrumentation framework for building dynamic analysis tools
License:        GPL
Vendor:         %{_vendor}
URL:            https://valgrind.org
Source0:        %{system_name}-%{version}.tar.bz2
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc EDOpython
Provides:       %{name} = %{version}


%description
Valgrind  is  an  instrumentation  framework for building dynamic
analysis tools. There are Valgrind tools that  can  automatically
detect  many  memory  management  and threading bugs, and profile
your programs in detail. You can also use Valgrind to  build  new
tools.

The  Valgrind  distribution  currently includes seven production‐
quality tools: a memory error detector, two thread  error  detec‐
tors, a cache and branch‐prediction profiler, a call‐graph gener‐
ating cache and branch‐prediction  profiler,  and  two  different
heap  profilers.  It also includes an experimental SimPoint basic
block vector generator.  It  runs  on  the  following  platforms:
X86/Linux,   AMD64/Linux,  ARM/Linux,  ARM64/Linux,  PPC32/Linux,
PPC64/Linux,    PPC64LE/Linux,     S390X/Linux,     MIPS32/Linux,
MIPS64/Linux,  X86/Solaris, AMD64/Solaris, ARM/Android (2.3.x and
later), ARM64/Android, X86/Android (4.0  and  later),  MIPS32/An‐
droid,  X86/FreeBSD,  AMD64/FreeBSD,  X86/Darwin and AMD64/Darwin
(Mac OS X 10.12).


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export CFLAGS="-O3 -g -Wall"
export CXXFLAGS="$CFLAGS"
%_configure --enable-only64bit --enable-lto --enable-tls
%make_build


%check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_bindir/cg_*
%_bindir/callgrind*
%_bindir/vgdb
%_bindir/ms_print
%_includedir/%{system_name}/*
%_libdir/%{system_name}/*
%_libdir/pkgconfig/%{system_name}.pc
%_docdir/%{system_name}/*
%_mandir/man1/%{system_name}*
%_mandir/man1/cg_*
%_mandir/man1/callgrind*
%_mandir/man1/vgdb.1
%_mandir/man1/ms_print.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
