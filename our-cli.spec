Name:           our-cli
Version:        0.0.1~0
Release:        0
Summary:        Command line interface for OUR (openSUSE User Repository)
License:        MPL-2.0
Url:            https://github.com/YoukouTenhouin/our-cli
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Command line interface for OUR (openSUSE User Repository).

%prep
%autosetup -p1 -a1

%build
export CARGO_HOME=$PWD/.cargo
%{cargo_build}

%install
export CARGO_HOME=$PWD/.cargo
%{cargo_install}

%check
export CARGO_HOME=$PWD/.cargo
%{cargo_test}

%files
# %license LICENSE-FILE
%{_bindir}/our

%changelog
