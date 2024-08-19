%global debug_package %{nil}
%define _build_id_links none
%define system_name libjson

Name:           EDO%{system_name}
Version:        0.8
Release:        1%{?dist}
Summary:        Simple and efficient json parser and printer in C.
License:        GPL
Vendor:         %{_vendor}
URL:            https://github.com/vincenthz/libjson
Source0:        %{system_name}-%{version}.tar.gz
Patch0:         %{system_name}-%{version}-perm.patch
AutoReqProv:    no
BuildRequires:  glibc-devel
Requires:       glibc
Provides:       %{name} = %{version}


%package devel
Summary:        Development tools for the %{system_name} library.
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch
AutoReqProv:    no


%description
libjson is a simple library without any dependancies to parse and
pretty print the JSON format (RFC 4627). The  JSON  format  is  a
concise and structured data format.  Features

    interruptible  parser:  append data to the state how you want
it.
    No object model integrated
    Small codebase: handcoded parser and efficient  factorisation
make the code smalls and perfect for embedding.
    Fast: use efficient code and small parsing tables for maximum
efficiency.
    Full JSON support.
    UTF8 validation of the input.
    No number conversion: user convert data the way they want.
    Secure: optional limits on nesting level, and on data size.
    Optional comments: in YAML/python style and C style.
    Optional user defined allocation functions.

libjson parser is an interruptible  handcoded  state  parse.  the
parser  takes character or string as input. Since it’s interrupt‐
ible, it’s up to the user to feed the stream to the parser, which
permits  complete  flexibility  as  to whether the data is coming
from a pipe, a network socket, a file on disk, a serial line,  or
crafted by the user.

The  parser  doesn’t create an object tree for you, but each time
it comes up with an element in this data, it just callback to the
user  with  the type found and for some type, the data associated
with it. It can be compared to the SAX way  of  XML,  hence  it’s
called SAJ (Simple API for JSon).

The parser doesn’t convert number to any native C format, but in‐
stead callback with a string that is a valid  JSon  number.  JSon
number can be of any size, so that’s up to user to decide whetev‐
er or not, the number can map to native C type int32_t,  int64_t,
or  a  complex  integer  type.  As  well the user has a choice to
refuse the integer at the callback stage if the length is not ap‐
propriate.

The parser optionally allows YAML and/or C comments to be ignored
if the config structure is set accordingly, otherwise a  JSON_ER‐
ROR_COMMENT_NOT_ALLOWED is returned.


%description devel


%prep
%setup -n %{system_name}-%{version}
%patch -p1


%build
%set_build_flags_with_rpath
%make_build


%check


%install
%make_install PREFIX=%_prefix LIBDIR=%_libdir


%clean
rm -rf $RPM_BUILD_ROOT


%files
%_bindir/jsonlint
%_libdir/%{system_name}.so.0*
%_libdir/%{system_name}.a


%files devel
%_includedir/json.h
%_libdir/%{system_name}.so
%_libdir/pkgconfig/%{system_name}.pc



%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
