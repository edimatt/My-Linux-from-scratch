%global debug_package %{nil}
%define _build_id_links none
%define system_name btop

Name:           EDO%{system_name}
Version:        1.2.13
Release:        1%{?dist}
Summary:        Btop resource monitor.

License:        GPL
URL:            https://github.com/aristocratos/btop
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build
Requires:       glibc libgcc libstdc++
Provides:       %{name} = %{version}
AutoReqProv:    no

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%setup -n %{system_name}-%{version}

%build
%set_build_flags_with_rpath
%make_build


%install
%__make install PREFIX=%{buildroot}%{_prefix} INSTALL='/usr/bin/install -p'


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_datadir/%{system_name}/*
%_datadir/applications/%{system_name}.desktop
%_datadir/icons/hicolor/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
