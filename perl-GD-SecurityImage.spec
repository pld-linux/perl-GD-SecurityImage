#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	SecurityImage
Summary:	GD::SecurityImage - Security image (captcha) generator.
#Summary(pl):	
Name:		perl-GD-SecurityImage
Version:	1.55
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65399f762e6958f29929f8b390739cb9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(GD)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		_noautoreq	'perl(Image::Magick)'

%description
The (so called) "Security Images" are so popular. Most internet 
software use these in their registration screens to block robot programs
(which may register tons of  fake member accounts). Security images are
basicaly, graphical CAPTCHAs (Completely Automated Public Turing Test to 
Tell Computers and Humans Apart). This module gives you a basic interface 
to create such an image. The final output is the actual graphic data, 
the mime type of the graphic and the created random string.

The module also has some "styles" that are used to create the background 
of the image.

If you are an Authen::Captcha user, see GD::SecurityImage::AC
for migration from Authen::Captcha to GD::SecurityImage.



# %description -l pl
# TODO

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GD/*.pm
%{perl_vendorlib}/GD/SecurityImage
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}