%global debug_package %{nil}
%define _build_id_links none
%define system_name xz

Name:           EDO%{system_name}
Version:        5.4.4
Release:        1%{?dist}
Summary:        xz compression library.
License:        GPL
URL:            https://github.com/tukaani-project/xz
Source0:        %{system_name}-%{version}.tar.xz
BuildRequires:  glibc-devel
Requires:       glibc %{name}-libs = %{version}
Provides:       %{name} = %{version}
AutoReqProv:    no

%package libs
Summary:        Libraries for decoding LZMA compression.
Requires:       bzip2-libs openssl-libs libxcrypt glibc libffi xz-libs ncurses-libs ncurses-libs readline sqlite-libs zlib expat libuuid gdbm libnsl2
Provides:       %{name}-libs = %{version}
AutoReqProv:    no

%package devel
Summary:        Devel libraries and headers for liblzma.
Requires:       %{name}-libs = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no

%description
XZ  Utils provide a general‐purpose data‐compression library plus
command‐line tools. The native file format is the .xz format, but
also  the  legacy  .lzma format is supported. The .xz format sup‐
ports multiple compression algorithms, which are called "filters"
in  the  context of XZ Utils. The primary filter is currently LZ‐
MA2. With typical files, XZ Utils create about 30 % smaller files
than gzip.

To  ease adapting support for the .xz format into existing appli‐
cations and scripts, the API of liblzma is  somewhat  similar  to
the  API  of  the  popular zlib library. For the same reason, the
command‐line tool xz has a command‐line syntax similar to that of
gzip.

When  aiming for the highest compression ratio, the LZMA2 encoder
uses a lot of CPU time and may use, depending  on  the  settings,
even  hundreds  of  megabytes of RAM. However, in fast modes, the
LZMA2 encoder competes with bzip2 in compression speed,  RAM  us‐
age, and compression ratio.

LZMA2  is  reasonably  fast  to decompress. It is a little slower
than gzip, but a lot faster than bzip2. Being fast to  decompress
means  that  the .xz format is especially nice when the same file
will be decompressed very many times (usually on  different  com‐
puters),  which is the case e.g. when distributing software pack‐
ages. In such situations, it’s not too  bad  if  the  compression
takes some time, since that needs to be done only once to benefit
many people.

With some file types, combining (or "chaining") LZMA2 with an ad‐
ditional filter can improve the compression ratio. A filter chain
may contain up to four filters, although usually only one or  two
are  used.   For example, putting a BCJ (Branch/Call/Jump) filter
before LZMA2 in the filter chain can improve compression ratio of
executable files.

Since the .xz format allows adding new filter IDs, it is possible
that some day there will be a filter that is, for  example,  much
faster  to  compress than LZMA2 (but probably with worse compres‐
sion ratio).  Similarly, it is possible that some day there is  a
filter that will compress better than LZMA2.

XZ  Utils  supports  multithreaded  compression. XZ Utils doesn’t
support multithreaded decompression  yet.  It  has  been  planned
though and taken into account when designing the .xz file format.
In the future, files that were created in threaded  mode  can  be
decompressed in threaded mode too.


%description libs
Libraries for decoding files compressed with LZMA or XZ utils.


%description devel
Devel libraries and headers for liblzma.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%configure --enable-static --disable-doc
%make_build


%install
%{make_install}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/lz*
%_bindir/xz*
%_bindir/un*
%_mandir/*/man1/lz*.1
%_mandir/*/man1/xz*.1
%_mandir/*/man1/un*.1
%_mandir/man1/lz*.1
%_mandir/man1/xz*.1
%_mandir/man1/un*.1
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%files libs
%_libdir/liblzma.a
%_libdir/liblzma.so.5
%_libdir/liblzma.so.5.4.4


%files devel
%_libdir/liblzma.so
%_libdir/liblzma.la
%_libdir/pkgconfig/liblzma.pc
%_includedir/lzma/*.h
%_includedir/lzma.h


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
