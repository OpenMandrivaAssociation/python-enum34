Name:           python-enum34
Version:        1.1.4
Release:        1
Group:          Development/Python
Summary:        Backport of Python 3.4 Enum
License:        BSD
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/enum34
Source0:        https://pypi.python.org/packages/source/e/enum34/enum34-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools


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


%prep
%setup -q -n enum34-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# remove docs from sitelib, we'll put them in doc dir instead
rm -rf %{buildroot}%{python2_sitelib}/enum/{LICENSE,README,doc}

%files
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%{python2_sitelib}/*
