%global debug_package %{nil}
%define _build_id_links none
%define system_name liquidprompt

Name:           EDO%{system_name}
Version:        2.1.2
Release:        1%{?dist}
Summary:        A useful adaptive prompt for Bash & Zsh.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/liquidprompt/liquidprompt
Source0:        %{system_name}-%{version}.tar.xz
AutoReqProv:    no
BuildRequires:  glibc-devel
BuildArch:      noarch
Requires:       glibc bash
Provides:       %{name} = %{version}


%description
Liquid  Prompt  gives you a carefully designed prompt with useful
information. It shows you what you need when  you  need  it.  You
will  notice  what changes when it changes, saving time and frus‐
tration. You can even use it with your favorite shell â  Bash  or
zsh.


%prep
%setup -q -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%check


%install
%__mkdir_p %{buildroot}%{_datadir}/%{system_name}
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
cp -pr liquid* themes tools tests* shellcheck.sh %{buildroot}%{_datadir}/%{system_name}/
cp liquidpromptrc-dist %{buildroot}%{_sysconfdir}/liquidpromptrc
cp %{system_name} %{buildroot}%{_sysconfdir}/profile.d/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%license LICENSE
%_datadir/%{system_name}/*
%_sysconfdir/%{system_name}*
%_sysconfdir/profile.d/%{system_name}


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
