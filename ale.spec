Summary:	Anti-Lamenessing Engine
Name:		ale
Version:	0.6.0
Release:	0.2
License:	GPL
Group:		Applications/Graphics
Source0:	http://auricle.dyndns.org/ALE/download/%{name}-%{version}.tar.gz
# Source0-md5:	a53a47dd01c66d5ea2fd6098146df99e
Patch0:		%{name}-makefile.patch
URL:		http://auricle.dyndns.org/ALE/
BuildRequires:	fftw3-devel
BuildRequires:	ImageMagick-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALE is a free software program that renders high-fidelity images of
real scenes by aligning and combining many similar images from a
camera or scanner.

%prep
%setup -q
%patch0 -p1

%build

%{__make} FFTW=1 IMAGEMAGICK=1 \
	OPT_CFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}/
install ale $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
