Summary:	Anti-Lamenessing Engine
Summary(pl):	Anti-Lamenessing Engine - silnik poprawiaj±cy zdjêcia
Name:		ale
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://auricle.dyndns.org/ALE/download/%{name}-%{version}.tar.gz
# Source0-md5:	d4a4e474ea4ceef2278f36019ac4daf8
Patch0:		%{name}-makefile.patch
URL:		http://auricle.dyndns.org/ALE/
BuildRequires:	ImageMagick-devel
BuildRequires:	fftw3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALE is a free software program that renders high-fidelity images of
real scenes by aligning and combining many similar images from a
camera or scanner.

%description -l pl
ALE to wolnodostêpny program tworz±cy wysokiej jako¶ci obrazy
prawdziwych scen poprzez wyrównywanie i ³±czenie wielu podobnych
obrazów z aparatu lub skanera.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	FFTW=1 \
	IMAGEMAGICK=1 \
	OPT_CFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ale $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
