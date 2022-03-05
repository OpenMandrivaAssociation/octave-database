%global octpkg database

Summary:	Interface to SQL databases, currently only postgresql using libpq
Name:		octave-%{octpkg}
Version:	2.4.4
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	octave-struct
BuildRequires:	pkgconfig(libpq)

Requires:	octave(api) = %{octave_api}
Requires:	octave-struct >= 1.0.12

Requires(post): octave
Requires(postun): octave

%description
Interface to SQL databases, currently only postgresql using libpq.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

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

