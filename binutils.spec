%global debug_package %{nil}
%define _build_id_links none
%define _build x86_64-edo-linux-gnu
%define _host x86_64-edo-linux-gnu
%define system_name binutils

Name:           EDO%{system_name}
Version:        2.41
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities.
License:        GPL
URL:            https://www.gnu.org/software/binutils
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build autoconf = 2.69
Requires:       glibc
AutoReqProv:    no

%description
Binutils  is  a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as  (a  family
of  GNU assemblers), gprof (for displaying call graph profile da‐
ta), ld (the GNU linker), nm (for  listing  symbols  from  object
files),  objcopy (for copying and translating object files), obj‐
dump (for displaying information from object files), ranlib  (for
generating an index for the contents of an archive), readelf (for
displaying detailed information about binary  files),  size  (for
listing  the section sizes of an object or archive file), strings
(for listing printable strings from files), strip (for discarding
symbols),  and  addr2line  (for  converting addresses to file and
line).


%prep
%setup -n %{system_name}-%{version}
autoreconf -fi


%build
%set_build_flags_with_rpath
%_configure --build=%_build --host=%_host --enable-shared --with-mpc=%_prefix --with-gmp=%_prefix --with-mpfr=%_prefix --with-isl=%_prefix --with-system-zlib --enable-lto --with-static-standard-libraries
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/libsframe.so.1.0.0
%_libdir/libsframe.so.1
%_libdir/libsframe.so
%_libdir/libsframe.la
%_libdir/libsframe.a
%_libdir/libbfd-2.41.so
%_libdir/libbfd.so
%_libdir/libbfd.la
%_libdir/libbfd.a
%_libdir/libopcodes-2.41.so
%_libdir/libopcodes.so
%_libdir/libopcodes.la
%_libdir/libopcodes.a
%_libdir/gprofng/libgp-collector.so
%_libdir/gprofng/libgp-collectorAPI.so
%_libdir/gprofng/libgp-collectorAPI.la
%_libdir/gprofng/libgp-heap.so
%_libdir/gprofng/libgp-sync.so
%_libdir/gprofng/libgp-iotrace.so
%_libdir/gprofng/libgp-collectorAPI.a
%_libdir/libgprofng.so.0.0.0
%_libdir/libgprofng.so.0
%_libdir/libgprofng.so
%_libdir/libgprofng.la
%_libdir/libgprofng.a
%_libdir/libctf.so.0.0.0
%_libdir/libctf.so.0
%_libdir/libctf.so
%_libdir/libctf.la
%_libdir/libctf-nobfd.so.0.0.0
%_libdir/libctf-nobfd.so.0
%_libdir/libctf-nobfd.so
%_libdir/libctf-nobfd.la
%_libdir/libctf.a
%_libdir/libctf-nobfd.a
%_libdir/bfd-plugins/libdep.so
%_includedir/sframe.h
%_includedir/sframe-api.h
%_includedir/bfd.h
%_includedir/ansidecl.h
%_includedir/symcat.h
%_includedir/diagnostics.h
%_includedir/bfdlink.h
%_includedir/plugin-api.h
%_includedir/dis-asm.h
%_includedir/collectorAPI.h
%_includedir/libcollector.h
%_includedir/libfcollector.h
%_includedir/ctf.h
%_includedir/ctf-api.h
%_infodir/sframe-spec.info
%ghost %_infodir/dir
%_infodir/bfd.info
%_infodir/binutils.info
%_infodir/as.info
%_infodir/gprof.info
%_infodir/gprofng.info
%_infodir/ctf-spec.info
%_infodir/ld.info
%_infodir/ldint.info
%_datadir/locale/*/LC_MESSAGES/*.mo
%_datadir/man/man1/addr2line.1
%_datadir/man/man1/ar.1
%_datadir/man/man1/dlltool.1
%_datadir/man/man1/nm.1
%_datadir/man/man1/objcopy.1
%_datadir/man/man1/objdump.1
%_datadir/man/man1/ranlib.1
%_datadir/man/man1/readelf.1
%_datadir/man/man1/size.1
%_datadir/man/man1/strings.1
%_datadir/man/man1/strip.1
%_datadir/man/man1/elfedit.1
%_datadir/man/man1/windres.1
%_datadir/man/man1/windmc.1
%_datadir/man/man1/c++filt.1
%_datadir/man/man1/as.1
%_datadir/man/man1/gprof.1
%_datadir/man/man1/gprofng.1
%_datadir/man/man1/gp-archive.1
%_datadir/man/man1/gp-collect-app.1
%_datadir/man/man1/gp-display-html.1
%_datadir/man/man1/gp-display-src.1
%_datadir/man/man1/gp-display-text.1
%_datadir/man/man1/ld.1
%_bindir/size
%_bindir/objdump
%_bindir/ar
%_bindir/strings
%_bindir/ranlib
%_bindir/objcopy
%_bindir/addr2line
%_bindir/readelf
%_bindir/elfedit
%_bindir/nm
%_bindir/strip
%_bindir/c++filt
%_bindir/as
%_bindir/gprof
%_bindir/gp-archive
%_bindir/gp-collect-app
%_bindir/gprofng
%_bindir/gp-display-text
%_bindir/gp-display-src
%_bindir/gp-display-html
%_bindir/ld.bfd
%_bindir/ld
%_sysconfdir/gprofng.rc
%_prefix/%_host/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-

