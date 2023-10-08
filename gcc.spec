%global debug_package %{nil}
%global _annobin_gcc_plugin %{nil}
# Format security breaks compilation
%global _warning_options %{nil}
%global _lto_cflags %{nil}
%define _build_id_links none
%define system_name gcc
%define _build x86_64-edo-linux-gnu
%define _host x86_64-edo-linux-gnu
%define _target x86_64-edo-linux-gnu
%global optflags %(echo %{optflags} | sed -e 's/-m[a-z0-9=-]* //g')

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
The  GNU  Compiler Collection includes front ends for C, C++, Ob‐
jective‐C, Fortran, Ada, Go, and D,  as  well  as  libraries  for
these  languages  (libstdc++,...).  GCC was originally written as
the compiler for the GNU operating system. The GNU system was de‐
veloped  to  be 100% free software, free in the sense that it re‐
spects the user’s freedom.

We strive to provide regular, high  quality  releases,  which  we
want  to  work well on a variety of native and cross targets (in‐
cluding GNU/Linux), and encourage everyone to contribute  changes
or help testing GCC. Our sources are readily and freely available
via Git and weekly snapshots.

Major decisions about GCC are made  by  the  steering  committee,
guided by the mission statement.

NOTE. Uninstall libiconv-devel otherwise libstdc++ will have a
runtime dependeny to libiconv!


%prep
if rpm -q EDOlibiconv-devel; then
    echo "Remove libiconv devel before building gcc."
    exit 1
fi
%setup -q -n %{system_name}-%{version}
# ./contrib/download_prerequisites 


%build
%set_build_flags_with_rpath
mkdir gcc-objdir && cd gcc-objdir
%_prev_configure --with-local-prefix=%_prefix --with-gpm=%_prefix --with-mpfr=%_prefix --with-mpc=%_prefix --with-isl=%_prefix --enable-languages=c,c++,jit,fortran --enable-host-shared --enable-threads=posix --enable-multilib --enable-lto --enable-host-shared --enable-shared --disable-bootstrap
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
%_includedir/libgccjit*.h
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

