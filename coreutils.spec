%global debug_package %{nil}
%define _build_id_links none
%define _build x86_64-edo-linux-gnu
%define _host x86_64-edo-linux-gnu
%define system_name coreutils

Name:           EDO%{system_name}
Version:        9.4
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities.
License:        GPL
URL:            https://www.gnu.org/software/binutils
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build glibc-devel libselinux-devel EDOpcre2-devel EDOgmp-devel EDOopenssl-devel EDOlibcap-devel EDOattr-devel EDOacl-devel
Requires:       glibc libselinux EDOpcre2 EDOgmp EDOopenssl-libs EDOlibcap EDOattr EDOacl
AutoReqProv:    no

%description


%prep
%setup -n %{system_name}-%{version}
./bootstrap


%build
%set_build_flags_with_rpath
export CFLAGS="-O3 -m64 -g -Wall"
export CXXFLAGS="$CFLAGS"
%_configure --build=%_build --host=%_host --enable-install-program=hostname
%make_build


%install
%make_install
# We use kill from util-linux.
rm %{buildroot}%{_bindir}/kill


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/*
%_libdir/%{system_name}/lib*.so
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/locale/*/LC_*/%{system_name}.mo
%_mandir/man1/*.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
-
