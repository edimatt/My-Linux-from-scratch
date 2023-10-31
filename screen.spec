%global debug_package %{nil}
%define _build_id_links none
%define system_name screen

Name:           EDO%{system_name}
Version:        4.9.1
Release:        1%{?dist}
Summary:        https://www.gnu.org/software/screen
License:        GPL
URL:            https://git.savannah.gnu.org/cgit/screen.git
Source0:        %{system_name}-%{version}.tar.gz
Provides:       %{name} = %{version}
BuildRequires:  glibc-devel EDOncurses-devel EDOlibutempter-devel EDOlibxcrypt-devel
Requires:       glibc EDOncurses-libs EDOlibutempter EDOlibxcrypt
AutoReqProv:    no


%description
Screen  is a full‐screen window manager that multiplexes a physi‐
cal terminal between  several  processes,  typically  interactive
shells.  Each  virtual terminal provides the functions of the DEC
VT100 terminal and, in addition, several control  functions  from
the  ANSI  X3.64  (ISO  6429)  and  ISO 2022 standards (e.g., in‐
sert/delete line and support for multiple character sets).  There
is  a  scrollback  history buffer for each virtual terminal and a
copy‐and‐paste mechanism that allows the user to  move  text  re‐
gions between windows. When screen is called, it creates a single
window with a shell in it (or the  specified  command)  and  then
gets  out of your way so that you can use the program as you nor‐
mally would. Then, at any time, you can create new  (full‐screen)
windows with other programs in them (including more shells), kill
the current window, view a list of the active windows, turn  out‐
put  logging  on  and  off,  copy  text between windows, view the
scrollback history, switch between windows, etc. All windows  run
their  programs  completely  independent  of each other. Programs
continue to run when their window is currently  not  visible  and
even  when  the  whole  screen session is detached from the users
terminal.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
%_configure
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/%{system_name}*
%_mandir/man1/%{system_name}.1
%ghost %_infodir/dir
%_infodir/%{system_name}.info
%_datadir/%{system_name}/*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
