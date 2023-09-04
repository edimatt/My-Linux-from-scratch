%global debug_package %{nil}
%define _build_id_links none
%define system_name gcc
%define _build x86_64-edo-linux-gnu
%define _host x86_64-edo-linux-gnu

Name:           EDO%{system_name}
Version:        13.2.0
Release:        1%{?dist}
Summary:        GNU compiler collection.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/vim/vim
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel EDOgmp-devel EDOmpfr-devel EDOmpc-devel
Requires:       glibc EDOgmp EDOmpfr EDOmpc
Provides:       %{name} = %{version}

%description


%prep
%setup -n %{system_name}-%{version}
./contrib/download_prerequisites 


%build
%set_build_flags_with_rpath
export CFLAGS="-O3 -g -Wall"
export CXXFLAGS="$CFLAGS"
mkdir gcc-objdir && cd gcc-objdir
%_prev_configure --with-local-prefix=%_prefix --with-gpm=%_prefix --with-mpfr=%_prefix --with-mpc=%_prefix --enable-languages=c,c++,fortran --enable-threads=posix --enable-multilib --enable-lto --enable-host-shared --enable-shared --disable-bootstrap
%make_build


%install
cd gcc-objdir && %make_install
%{buildroot}%_bindir/gcc -dumpspecs > specs
sed '/*link:/ {N;s_$_ %{m32:-rpath=\$ORIGIN/../lib:/opt/edo/lib} %{m64:-rpath=\$ORIGIN/../lib64:/opt/edo/lib64} %{!m32:%{!m64:-rpath=\$ORIGIN/../lib64:/opt/edo/lib64}}_}' specs > %{buildroot}%{_libdir}/%{system_name}/%{_build}/%{version}/specs


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}/%{_build}/%{version}/*
%_libdir/libcc1*
%_libdir/libgcc*
%_libdir/libsupc*
%_libdir/libstdc++*
%_libdir/liblsan*
%_libdir/libasan*
%_libdir/libubsan*
%_libdir/libtsan*
%_libdir/libhwasan*
%_libdir/libssp*
%_libdir/libquadmath*
%_libdir/libgfortran*
%_libdir/libgomp*
%_libdir/libitm*
%_libdir/libatomic*
%_libdir/libsanitizer*
%_bindir/*
%_includedir/c++/%{version}/*
%ghost %_infodir/dir
%_infodir/*.info
%_mandir/man*/*
%_datadir/%{system_name}-%{version}/*
%_prefix/lib/libgcc*
%_prefix/lib/libsupc*
%_prefix/lib/libstdc++*
%_prefix/lib/libasan*
%_prefix/lib/libubsan*
%_prefix/lib/libssp*
%_prefix/lib/libquadmath*
%_prefix/lib/libgfortran*
%_prefix/lib/libgomp*
%_prefix/lib/libitm*
%_prefix/lib/libatomic*
%_prefix/lib/libsanitizer*
%_datadir/locale/*/LC_MESSAGES/*.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-

