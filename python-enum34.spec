%define module enum34

Name:           python-%{module}
Version:        1.1.6
Release:        3
Group:          Development/Python
Summary:        Backport of Python 3.4 Enum
License:        BSD
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/enum34
Source0:        https://pypi.io/packages/source/e/enum34/%{module}-%{version}.tar.gz


%description
Python 3.4 introduced official support for enumerations.  This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.5, 2.5, and 2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.

#------------------------------------------------

%package -n     python2-%{module}
Summary:        Backport of Python 3.4 Enum
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools

Obsoletes:      python-enum34 < 1.0.4-3
Provides:       python-enum34 = %{version}-%{release}

%description -n python2-%{module}
Python 3.4 introduced official support for enumerations.  This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.5, 2.5, and 2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.
#------------------------------------------------


%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py2_build

%check
pushd %{buildroot}/%{python2_sitelib}
PYTHONPATH=".:${PYTHONPATH}" %{__python2} enum/test.py
popd


%install
%py2_install

# remove docs from sitelib, we'll put them in doc dir instead
rm -rf %{buildroot}%{python2_sitelib}/enum/{LICENSE,README,doc}


%files -n python2-%{module}
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%{python2_sitelib}/*
