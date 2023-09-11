%global debug_package %{nil}
%define _build_id_links none
%define system_name fortune-mod

Name:           EDO%{system_name}
Version:        3.20.0
Release:        1%{?dist}
Summary:        Display a pseudorandom message.
License:        GPL
URL:            https://github.com/shlomif/fortune-mod
Source:         %{system_name}-%{version}.tar.xz
Patch:          %{system_name}-%{version}-paths.patch
BuildRequires:  rpm-build
Requires:       glibc
AutoReqProv:    no

%description
fortune  is a command‐line utility which displays a random quota‐
tion from a collection of quotes. This collection  is  read  from
the  local  file  system  and  does not require network access. A
large collection of quotes is provided in the  download  and  in‐
stalled  by  default,  but more quote collections can be added by
the user.
The   canonical   repository   for    the    time    being    is:
https://github.com/shlomif/fortune‐mod  .  In  the future, we may
create a GitHub organization for it and move the sources there.


%prep
%setup -n %{system_name}-%{version}
%patch -p1
# sed -i '/CMAKE_INSTALL_PREFIX/s/games\///' CMakeLists.txt


%build
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_INSTALL_DOCDIR=%_docdir/%{name} -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DENABLE_STATIC=0 ..
%make_build


%install
cd build && %make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*str*
%_bindir/rot
%_bindir/fortune
%_mandir/man1/*str*.1
%_mandir/man6/fortune.6
%_datadir/fortunes/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
