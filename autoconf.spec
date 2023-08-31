%global debug_package %{nil}
%define _build_id_links none
%define system_name autoconf

Name:           EDO%{system_name}
Version:        2.71
Release:        1%{?dist}
Summary:        A GNU tool for automatically configuring source code.
License:        GPL
URL:            https://www.gnu.org/software/autoconf
Source0:        %{system_name}-%{version}.tar.xz
Provides:       %{name} = %{version}
BuildArch:      noarch
BuildRequires:  rpm-build EDOm4
Requires:       bash EDOm4
# Requires:     perl
AutoReqProv:    no

%description
GNU’s  Autoconf  is  a tool for configuring source code and Make‐
files.  Using Autoconf, programmers can create portable and  con‐
figurable  packages, since the person building the package is al‐
lowed to specify various configuration options.

You should install Autoconf if you are  developing  software  and
would  like  to  create  shell scripts that configure your source
code packages. If you are installing Autoconf, you will also need
to install the GNU m4 package.

Note  that  the Autoconf package is not required for the end‐user
who  may  be  configuring  software  with  an  Autoconf‐generated
script;  Autoconf  is  only  required  for  the generation of the
scripts, not their use.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
export M4=%_bindir/m4
export EMACS=%_bindir/emacs
%configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/auto*
%_bindir/ifnames
%_datadir/%{system_name}/*
%_datadir/emacs/site-lisp/auto*.el*
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_infodir/standards.info
%_mandir/man1/auto*.1
%_mandir/man1/ifnames.1



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
