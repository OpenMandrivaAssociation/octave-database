%global octpkg database

Summary:	Interface to SQL databases, currently only postgresql using libpq
Name:		octave-database
Version:	2.4.4
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/database/
Source0:	https://downloads.sourceforge.net/octave/database-%{version}.tar.gz
# (upstream) https://savannah.gnu.org/bugs/index.php?61567
Patch0:		octave-database-2.4.4-port-to-octave8.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  octave-struct >= 1.0.12
BuildRequires:  pkgconfig(libpq)

Requires:	octave(api) = %{octave_api}
Requires:  	octave-struct >= 1.0.12

Requires(post): octave
Requires(postun): octave

%description
Interface to SQL databases, currently only postgresql using libpq.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml
#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

