#
# Conditional build:
%bcond_with	tests	# unit tests (some failing)

Summary:	cmd2 - a tool for building interactive command line applications in Python
Summary(pl.UTF-8):	cmd2 - narzędzie do tworzenia interaktywnych aplikacji linii poleceń w Pythonie
Name:		python-cmd2
# keep 0.8.x here for python2 support
Version:	0.8.9
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/c/cmd2/cmd2-%{version}.tar.gz
# Source0-md5:	878976772c305486dfbca3aff4b4e779
URL:		https://pypi.org/project/cmd2/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-contextlib2
BuildRequires:	python-enum34
BuildRequires:	python-mock
BuildRequires:	python-pyparsing >= 2.0.1
BuildRequires:	python-pyperclip
BuildRequires:	python-pytest
BuildRequires:	python-six
BuildRequires:	python-subprocess32
BuildRequires:	python-wcwidth
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmd2 is a tool for building interactive command line applications in
Python. Its goal is to make it quick and easy for developers to build
feature-rich and user-friendly interactive command line applications.
It provides a simple API which is an extension of Python's built-in
cmd module. cmd2 provides a wealth of features on top of cmd to make
your life easier and eliminates much of the boilerplate code which
would be necessary when using cmd.

%description -l pl.UTF-8
cmd2 to narzędzie do tworzenia interaktywnych aplikacji linii poleceń
w Pythonie. Jego celem jest ułatwienie szybkiego tworzenia bogatych
funkcjonalnie, przyjaznych dla użytkownika aplikacji linii poleceń.
Zapewnia proste API, rozszerzające wbudowany w Pythona moduł cmd; daje
bogate możliwości, ułatwiające życie i eliminujące dużą część
powtarzalnego kodu, który trzeba by było napisać, używając cmd.

%prep
%setup -q -n cmd2-%{version}

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-cmd2-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-cmd2-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python-cmd2-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python}|'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py_sitescriptdir}/cmd2.py[co]
%{py_sitescriptdir}/cmd2-%{version}-py*.egg-info
%{_examplesdir}/python-cmd2-%{version}
