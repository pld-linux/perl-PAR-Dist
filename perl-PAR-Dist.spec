#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PAR
%define	pnam	Dist
Summary:	PAR::Dist - create and manipulate PAR distributions
Summary(pl):	PAR::Dist - tworzenie i manipulacja dystrybucjami PAR
Name:		perl-%{pdir}-%{pnam}
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3f708ad631d1dfaf2a7600d941eae808
URL:		http://par.perl.org
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates and manipulates PAR distributions.  They are
architecture-specific PAR files, containing everything under blib/ of
CPAN distributions after their "make" or "Build" stage, a META.yml
describing metadata of the original CPAN distribution, and a MANIFEST
detailing all files within it.  Digitally signed PAR distributions
will also contain a SIGNATURE file.

%description -l pl
Ten modu³ tworzy i manipuluje dystrybucjami PAR. S± one zale¿nymi od
architektury plikami PAR. Zawieraj± wszystko to, co znajduje siê
w katalogu blib/ dystrybucji CPAN po wykonaniu etapu "make" lub
"Build", plik META.yml opisuj±cy metadane pierwotnej dystrybucji CPAN
oraz plik MANIFEST zawieraj±cy listê plików. Podpisane cyfrowo
dystrybucje PAR zawieraj± dodatkowo plik SIGNATURE.

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
%dir %{perl_vendorlib}/%{pdir}
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
