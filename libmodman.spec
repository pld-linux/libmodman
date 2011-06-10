#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Module Manager library
Summary(pl.UTF-8):	Biblioteka zarządcy modułów
Name:		libmodman
Version:	2.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://code.google.com/p/libmodman/downloads/list
Source0:	http://libmodman.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	30591745dee416331e1cf143b39e4e31
URL:		http://code.google.com/p/libmodman/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
Conflicts:	libproxy < 0.4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmodman is a simple library for managing modules.

%description -l pl.UTF-8
libmodman to prosta biblioteka do zarządzania modułami.

%package devel
Summary:	Header files for libmodman library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmodman
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libmodman library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmodman.

%prep
%setup -q

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libmodman.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmodman.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmodman.so
%{_includedir}/libmodman
%{_pkgconfigdir}/libmodman-2.0.pc
%{_datadir}/cmake/Modules/Findlibmodman.cmake
