%global debug_package %{nil}
%define _build_id_links none
%define system_name libffi

Name:           EDO%{system_name}
Version:        3.4.6
Release:        1%{?dist}
Summary:        A portable foreign function interface library.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/libffi/libffi
Source0:        %{system_name}-%{version}.tar.gz
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
Compilers for high level languages generate code that follow cer‐
tain conventions. These conventions are necessary, in  part,  for
separate compilation to work. One such convention is the "calling
convention". The "calling convention" is essentially a set of as‐
sumptions  made  by  the  compiler about where function arguments
will be found on entry to a function. A "calling convention" also
specifies where the return value for a function is found.

Some  programs may not know at the time of compilation what argu‐
ments are to be passed to a function.  For  instance,  an  inter‐
preter  may be told at run‐time about the number and types of ar‐
guments used to call a given function. Libffi can be used in such
programs to provide a bridge from the interpreter program to com‐
piled code.

The libffi library provides a portable,  high  level  programming
interface  to various calling conventions. This allows a program‐
mer to call any function specified by a call  interface  descrip‐
tion at run time.

FFI stands for Foreign Function Interface. A foreign function in‐
terface is the popular name for the interface  that  allows  code
written in one language to call code written in another language.
The libffi library really only provides the lowest,  machine  de‐
pendent  layer  of a fully featured foreign function interface. A
layer must exist above libffi that handles type  conversions  for
values passed between the two languages.


%description devel


%prep
%setup -n %{system_name}-%{version}
./autogen.sh


%build
%set_build_flags_with_rpath
%_configure --disable-static            \
            --with-gcc-arch=native      \
            --disable-exec-static-tramp
%make_build


%check
make check


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_libdir/%{system_name}.so.8*


%files devel
%_mandir/man3/ffi*.3
%_includedir/ffi*.h
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_libdir/%{system_name}*.so
%_libdir/%{system_name}*.la
%_libdir/pkgconfig/%{system_name}*.pc


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
