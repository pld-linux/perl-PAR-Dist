#
# Conditional build:
%bcond_without	test # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PAR
%define		pnam	Dist
Summary:	PAR::Dist - create and manipulate PAR distributions
Summary(pl.UTF-8):	PAR::Dist - tworzenie i manipulacja dystrybucjami PAR
Name:		perl-PAR-Dist
Version:	0.40
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	904832a892277849aef78d07a3f8d9d7
URL:		http://par.perl.org
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Ten moduł tworzy i manipuluje dystrybucjami PAR. Są one zależnymi od
architektury plikami PAR. Zawierają wszystko to, co znajduje się
w katalogu blib/ dystrybucji CPAN po wykonaniu etapu "make" lub
"Build", plik META.yml opisujący metadane pierwotnej dystrybucji CPAN
oraz plik MANIFEST zawierający listę plików. Podpisane cyfrowo
dystrybucje PAR zawierają dodatkowo plik SIGNATURE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PAR/*.pm
%{_mandir}/man3/*
