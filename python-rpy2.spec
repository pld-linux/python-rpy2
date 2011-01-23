%define module rpy2
Summary:	Simple and robust Python interface to the R Programming Language
Name:		python-%{module}
Version:	2.1.8
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/rpy/%{module}-%{version}.tar.gz
# Source0-md5:	378c053f5eac7e96c500c8ebcac00a42
URL:		http://rpy.sourceforge.net/
BuildRequires:	R
BuildRequires:	python-devel
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

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
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

%dir %{py_sitedir}/%{module}/rinterface
%attr(755,root,root) %{py_sitedir}/%{module}/rinterface/*.so
%{py_sitedir}/%{module}/rinterface/*.py[co]
%{py_sitedir}/%{module}/rinterface/tests
