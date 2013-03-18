%define module rpy2
Summary:	Simple and robust Python interface to the R Programming Language
Name:		python-%{module}
Version:	2.3.4
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/r/rpy2/%{module}-%{version}.tar.gz
# Source0-md5:	38fa0fb1b2543e65655ced3d6741ba68
URL:		http://rpy.sourceforge.net/rpy2.html
BuildRequires:	R
BuildRequires:	blas-devel
BuildRequires:	lapack-devel
BuildRequires:	python-devel
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	R
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RPy is a very simple, yet robust, Python interface to the R
Programming Language. It can manage all kinds of R objects and can
execute arbitrary R functions (including the graphic functions). All
errors from the R language are converted to Python exceptions. Any
module installed for the R system can be used from within Python.

%package -n python3-%{module}
Summary:	Simple and robust Python interface to the R Programming Language
Group:          Development/Languages/Python
%pyrequires_eq	python3-modules

%description -n python3-%{module}
RPy is a very simple, yet robust, Python interface to the R
Programming Language. It can manage all kinds of R objects and can
execute arbitrary R functions (including the graphic functions). All
errors from the R language are converted to Python exceptions. Any
module installed for the R system can be used from within Python.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build --build-base py2
%{__python3} setup.py build --build-base py3

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py build \
	--build-base py2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__python3} setup.py build \
	--build-base py3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{py_sitedir}/%{module}
%{py_sitedir}/*.egg-info

%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/rlike
%{py_sitedir}/%{module}/robjects

%{py_sitedir}/%{module}/interactive

%dir %{py_sitedir}/%{module}/rinterface
%attr(755,root,root) %{py_sitedir}/%{module}/rinterface/*.so
%{py_sitedir}/%{module}/rinterface/*.py[co]
%{py_sitedir}/%{module}/rinterface/tests

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/*.egg-info

%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/interactive
%{py3_sitedir}/%{module}/rlike
%{py3_sitedir}/%{module}/robjects

%dir %{py3_sitedir}/%{module}/rinterface
%attr(755,root,root) %{py3_sitedir}/%{module}/rinterface/*.so
%{py3_sitedir}/%{module}/rinterface/*.py
%{py3_sitedir}/%{module}/rinterface/__pycache__
%{py3_sitedir}/%{module}/rinterface/tests
