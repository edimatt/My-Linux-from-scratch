%global debug_package %{nil}
%define _build_id_links none
%define system_name tar

Name:           EDO%{system_name}
Version:        1.35
Release:        1%{?dist}
Summary:        GNU file archiving program.
License:        GPL
URL:            https://www.gnu.org/software/tar
Source:         https://ftp.gnu.org/gnu/tar/%{system_name}-%{version}.tar.xz
BuildRequires:  rpm-build glibc-devel libselinux-devel EDOacl-devel EDOattr-devel EDOpcre2-devel
Requires:       glibc libselinux EDOacl-libs EDOattr-libs EDOpcre2

AutoReqProv:    no

%description
The  GNU tar program saves many files together in one archive and
can restore individual files (or all of the files) from that  ar‐
chive.  Tar  can also be used to add supplemental files to an ar‐
chive and to update or list files in the  archive.  Tar  includes
multivolume support, automatic archive compression/decompression,
the ability to perform remote archives, and the ability  to  per‐
form incremental and full backups.

If  you  want to use tar for remote backups, you also need to in‐
stall the rmt package on the remote box.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath
# Remove EDOlibiconv-devel and comment the following.
# export LIBS="-liconv"
%_configure --with-libintl-prefix=%_prefix
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/%{system_name}
%_mandir/man1/%{system_name}.1
%_mandir/man8/rmt.8
%ghost %_infodir/dir
%_infodir/%{system_name}.info*
%_libdir/rmt
%_datadir/locale/*/LC_MESSAGES/%{system_name}.mo


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
