%global debug_package %{nil}
%define _build_id_links none
%define system_name bitwise

Name:           EDO%{system_name}
Version:        0.50
Release:        1%{?dist}
Summary:        Terminal based bitwise calculator in curses.
License:        GPL
URL:            https://github.com/mellowcandle/bitwise
Source0:        %{system_name}-v%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  rpm-build EDOncurses-devel EDOreadline-devel
Requires:       glibc EDOncurses-libs EDOreadline
AutoReqProv:    no

%description
Bitwise  is  multi base interactive calculator supporting dynamic
base conversion and bit manipulation. It’s a handy tool  for  low
level hackers, kernel developers and device drivers developers.

Some of the features include:

  - Interactive ncurses interface
  - Command line calculator supporting all bitwise operations.
  - Individual bit manipulator.
  - Bitwise operations such as NOT, OR, AND, XOR, and shifts.


%prep
%setup -n %{system_name}-v%{version}


%build
%set_build_flags_with_rpath
%configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
