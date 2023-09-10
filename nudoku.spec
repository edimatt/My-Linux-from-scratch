%global debug_package %{nil}
%define _build_id_links none
%define system_name nudoku

Name:           EDO%{system_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Ncurses base sudoku game.

License:        GPL
URL:            http://jubalh.github.io/nudoku/
Source0:        %{system_name}-%{version}.tar.xz

BuildRequires:  rpm-build EDOncurses-devel
Requires:       EDOncurses-libs glibc
Provides:       %{name} = %{version}
AutoReqProv:    no

%description
Can't  code?  Can't  hack?  Canât do anything cool on the command
line? This game will give you an excuse to spend some time in the
terminal nevertheless.
Be a cool kid, be in the terminal. Play nudoku!
As  a  bonus  you will even learn the basic vi movement commands.
Features
nudoku can also generate PDF files, like this, containing sudokus
and create single sudoku PNGs like the following:


%prep
%setup -n %{system_name}-%{version}
%autoreconf


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
%_mandir/man6/%{system_name}.6
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
