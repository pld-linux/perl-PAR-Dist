#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PAR
%define	pnam	Dist
Summary:	Create and manipulate PAR distributions
Name:		perl-%{pdir}-%{pnam}
Version:	0.05
Release:	1
License:	Same as Perl itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://par.perl.org
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates and manipulates PAR distributions.  They are archi-
tecture-specific PAR files, containing everything under blib/ of CPAN
distributions after their "make" or "Build" stage, a META.yml describ-
ing metadata of the original CPAN distribution, and a MANIFEST detail-
ing all files within it.  Digitally signed PAR distributions will also
contain a SIGNATURE file.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/PAR
%{perl_vendorlib}/PAR/*.pm
%{_mandir}/man3/*
