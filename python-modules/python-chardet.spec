%global debug_package %{nil}
%define _build_id_links none
%define system_name chardet

Name:           EDOpython-%{system_name}
Version:        5.2.0
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 3
License:        MIT 
URL:            https://pypi.org/project/%{system_name}/
Source:         %{system_name}-%{version}.tar.gz
BuildRequires:  rpm-build glibc-devel EDOpython
Requires:       glibc EDOpython
AutoReqProv:    no
BuildArch:      noarch


%description
Detects
ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
EUC-KR, ISO-2022-KR, Johab (Korean)
KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
ISO-8859-5, windows-1251 (Bulgarian)
ISO-8859-1, windows-1252, MacRoman (Western European languages)
ISO-8859-7, windows-1253 (Greek)
ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
TIS-620 (Thai)
Note:
Our ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
disabled until we can retrain the models.
Requires Python 3.7+.


%prep
%setup -n %{system_name}-%{version}


%build
%set_build_flags_with_rpath


%install
%pip_install


%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/%{system_name}*
%{_libdir}/python3.12/site-packages/%{system_name}*


%changelog
* Thu Jan 26 2023 Edoardo Di Matteo
- 
