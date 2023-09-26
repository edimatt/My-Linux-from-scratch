%global debug_package %{nil}
%define _build_id_links none
%define system_name ninja

Name:           EDO%{system_name}
Version:        1.11.1
Release:        1%{?dist}
Summary:        A small build system with a focus on speed.
License:        Apache 2.0
URL:            https://github.com/ninja-build/ninja
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc
Requires:       glibc EDOgcc
AutoReqProv:    no

%description
See the manual or doc/manual.asciidoc included in  the  distribu‐
tion for background and more details.
Binaries  for Linux, Mac and Windows are available on GitHub. Run
./ninja ‐h for Ninja help.
Installation is not necessary because the only required  file  is
the resulting ninja binary. However, to enable features like Bash
completion and Emacs and Vim editing modes, some files  in  misc/
must be copied to appropriate locations.
If  you’re interested in making changes to Ninja, read CONTRIBUT‐
ING.md first.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" .
%make_build


%install
%make_install


%check
./ninja_test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
