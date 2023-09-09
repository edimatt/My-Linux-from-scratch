%global debug_package %{nil}
%define _build_id_links none
%define system_name task

Name:           EDO%{system_name}
Version:        2.6.2
Release:        1%{?dist}
Summary:        Manages your TODO list from the command line.
License:        GPL
URL:            https://taskwarrior.org
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOgcc EDOlibuuid-devel EDOgnutls-devel
Requires:       glibc EDOgcc EDOlibuuid EDOgnutls
AutoReqProv:    no

%description


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_C_COMPILER=%_bindir/gcc -DCMAKE_CXX_COMPILER=%_bindir/g++ -DCMAKE_CXX_FLAGS_RELEASE="$CXXFLAGS" -DCMAKE_C_FLAGS_RELEASE="$CFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" .
%make_build


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_mandir/man5/%{system_name}*.5
%_datadir/zsh/site-functions/_%{system_name}
%_docdir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
